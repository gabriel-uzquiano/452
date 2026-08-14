"""
Post-process pandoc-generated HTML to replace Carnap exercise blocks
with interactive widgets matching the USC Logic Web Unit I style.

Handles:
  * QualitativeProblem (multiple-choice, single or multi-select)
  * SynChecker (well-formed-formula input, offline PL parser check)
"""
import re
import sys
from html import escape

MC_JS = """
<script>
function checkMC(btn) {
  var ex = btn.closest('.mc-exercise');
  var correct = JSON.parse(ex.dataset.correct);
  var multi = ex.dataset.multi === "true";
  var feedback = ex.querySelector('.mc-feedback');
  feedback.removeAttribute('hidden');
  if (multi) {
    var checked = Array.from(ex.querySelectorAll('input[type=checkbox]:checked')).map(function(c){ return parseInt(c.value); });
    var ok = correct.length === checked.length && correct.every(function(v){ return checked.includes(v); });
    feedback.textContent = ok ? '✓ Correct.' : '✗ Not quite — try again.';
    feedback.className = 'mc-feedback ' + (ok ? 'fb-ok' : 'fb-err');
  } else {
    var selected = ex.querySelector('input[type=radio]:checked');
    if (!selected) { feedback.textContent = 'Please select an option.'; feedback.className = 'mc-feedback'; return; }
    var ok = correct.includes(parseInt(selected.value));
    feedback.textContent = ok ? '✓ Correct.' : '✗ Not quite — try again.';
    feedback.className = 'mc-feedback ' + (ok ? 'fb-ok' : 'fb-err');
  }
}
function revealMC(btn) {
  var ex = btn.closest('.mc-exercise');
  var ans = ex.querySelector('.mc-answer');
  ans.removeAttribute('hidden');
  if (window.MathJax) { MathJax.Hub.Queue(['Typeset', MathJax.Hub, ans]); }
}
</script>
"""

MC_CSS = """
<style>
.mc-exercise { margin: 1.2rem 0 2rem; width: 55%; margin-left: 8%; }
.mc-question { margin-bottom: 0.7rem; font-size: 1.4rem; line-height: 2rem; }
.mc-options { display: flex; flex-direction: column; gap: 0.4rem; margin-bottom: 0.8rem; }
.mc-option { display: flex; align-items: baseline; gap: 0.6rem; cursor: pointer; font-size: 1.3rem; line-height: 1.7rem; }
.mc-option input { margin: 0; flex-shrink: 0; }
.mc-controls { display: flex; gap: 0.6rem; margin-bottom: 0.5rem; }
.btn-check, .btn-reveal {
  font-family: Gill Sans, Gill Sans MT, Calibri, sans-serif;
  font-size: 0.82rem; padding: 0.22rem 0.7rem;
  border-radius: 3px; cursor: pointer; border: 1px solid #ccc;
  background: #fffff8; color: #111;
}
.btn-check:hover { background: #006666; color: #fff; border-color: #006666; }
.mc-feedback { font-family: Gill Sans, Gill Sans MT, Calibri, sans-serif; font-size: 0.9rem; margin-bottom: 0.3rem; }
.fb-ok { color: #1a6e2e; } .fb-err { color: #8b1a1a; }
.mc-answer { font-family: Gill Sans, Gill Sans MT, Calibri, sans-serif; font-size: 0.88rem; color: #555; margin-top: 0.3rem; }
.mc-explanation { margin-top: 0.4rem; font-family: et-book, Palatino, serif; font-size: 1.2rem; line-height: 1.7rem; color: #333; }
</style>
"""

def parse_carnap_block(label, lines, multi):
    """
    Parse Carnap pipe-format options.
    |* option  -> correct
    | option   -> incorrect
    Explanation: text -> explanation (may span multiple lines)
    Returns (options: list of (text, is_correct), explanation: str)
    """
    options = []
    explanation_lines = []
    in_explanation = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('Explanation:'):
            in_explanation = True
            rest = stripped[len('Explanation:'):].strip()
            if rest:
                explanation_lines.append(rest)
            continue
        if in_explanation:
            # continuation lines of the explanation
            explanation_lines.append(stripped)
            continue
        if not stripped or stripped == label + '.':
            continue
        if stripped.startswith('|*'):
            text = stripped[2:].strip()
            options.append((text, True))
        elif stripped.startswith('|'):
            text = stripped[1:].strip()
            if text:
                options.append((text, False))
    explanation = ' '.join(explanation_lines).strip()
    return options, explanation

counter = [0]

def make_widget(label, options, multi, context_question=None, explanation=''):
    counter[0] += 1
    idx = counter[0]
    name = f"ex_{idx}"
    correct = [i for i, (_, c) in enumerate(options) if c]
    correct_json = str(correct).replace(" ", "")
    multi_attr = 'data-multi="true"' if multi else ''
    
    opts_html = []
    for i, (text, _) in enumerate(options):
        input_type = "checkbox" if multi else "radio"
        opts_html.append(
            f'<label class="mc-option">'
            f'<input type="{input_type}" name="{name}_{i}" value="{i}">'
            f'<span>{escape(text)}</span></label>'
        )
    
    correct_texts = [escape(options[i][0]) for i in correct]
    answer_str = "; ".join(correct_texts)

    question_html = ""
    if context_question:
        question_html = f'<div class="mc-question">{escape(context_question)}</div>'

    explanation_html = ""
    if explanation:
        # Do not escape explanation — it may contain MathJax ($...$) and HTML
        explanation_html = f'<div class="mc-explanation">{explanation}</div>'

    return (
        f'<div class="mc-exercise" data-correct=\'{correct_json}\' {multi_attr}>\n'
        f'  {question_html}\n'
        f'  <div class="mc-options">\n    ' + "\n    ".join(opts_html) + '\n  </div>\n'
        f'  <div class="mc-controls">\n'
        f'    <button class="btn-check" onclick="checkMC(this)">Check</button>\n'
        f'    <button class="btn-reveal" onclick="revealMC(this)">Show answer</button>\n'
        f'  </div>\n'
        f'  <div class="mc-feedback" hidden></div>\n'
        f'  <div class="mc-answer" hidden><strong>Answer:</strong> {answer_str}'
        + (f'<br><br>{explanation_html}' if explanation_html else '') +
        f'</div>\n'
        f'</div>'
    )

# ─── SynChecker ──────────────────────────────────────────────────────────────
#
# A SynChecker block in Carnap looks like:
#
#   ```{.SynChecker .Match system="gamutIPND" options="check" submission="none"}
#   A. (p & - q)
#   ```
#
# The body is a Carnap-ASCII propositional formula that the student is asked
# to reproduce. In the standalone widget, we render a text input; on Check we
# parse the student's input with a tiny in-browser PL parser and compare its
# AST to the target's AST. Show-answer reveals the formula in MathJax.
#
# Carnap-ASCII conventions we accept:
#   ¬  : -   (unary, prefix)
#   ∧  : &   or  /\
#   ∨  : \/  or  v   (as a full token; not the letter inside identifiers)
#   →  : ->  or  >
#   ↔  : <-> or  <>
# Propositional variables: p q r s t (optionally followed by digits).

SYN_CSS = """
<style>
.syn-exercise { margin: 1.2rem 0 2rem; width: 55%; margin-left: 8%; }
.syn-prompt { font-size: 1.4rem; line-height: 2rem; margin-bottom: 0.6rem; }
.syn-prompt .syn-label { font-variant: small-caps; margin-right: 0.4rem; color: #555; }
.syn-input-row { display: flex; gap: 0.5rem; align-items: center; margin-bottom: 0.5rem; }
.syn-input {
  font-family: "SF Mono", Menlo, Consolas, monospace;
  font-size: 1rem; padding: 0.25rem 0.4rem;
  border: 1px solid #ccc; border-radius: 3px;
  background: #fffff8; color: #111;
  min-width: 18rem;
}
.syn-input:focus { outline: none; border-color: #006666; }
.syn-controls { display: flex; gap: 0.6rem; margin-bottom: 0.4rem; }
.syn-feedback { font-family: Gill Sans, Gill Sans MT, Calibri, sans-serif; font-size: 0.9rem; margin-bottom: 0.3rem; }
.syn-feedback.fb-ok  { color: #1a6e2e; }
.syn-feedback.fb-err { color: #8b1a1a; }
.syn-feedback.fb-note { color: #555; }
.syn-answer { font-family: Gill Sans, Gill Sans MT, Calibri, sans-serif; font-size: 0.9rem; color: #555; margin-top: 0.3rem; }
.syn-answer .syn-answer-math { font-family: et-book, Palatino, serif; font-size: 1.2rem; }
.syn-hint { font-family: Gill Sans, Gill Sans MT, Calibri, sans-serif; font-size: 0.78rem; color: #888; margin-top: 0.2rem; }
</style>
"""

SYN_JS = r"""
<script>
(function(){
  // ─── Tokenizer ───────────────────────────────────────────────────────────
  function tokenize(src) {
    var toks = [];
    var i = 0;
    while (i < src.length) {
      var c = src[i];
      if (c === ' ' || c === '\t' || c === '\n') { i++; continue; }
      if (c === '(') { toks.push({t:'('}); i++; continue; }
      if (c === ')') { toks.push({t:')'}); i++; continue; }
      // two- and three-char operators first
      if (src.substr(i,3) === '<->') { toks.push({t:'iff'}); i += 3; continue; }
      if (src.substr(i,2) === '<>')  { toks.push({t:'iff'}); i += 2; continue; }
      if (src.substr(i,2) === '->')  { toks.push({t:'imp'}); i += 2; continue; }
      if (src.substr(i,2) === '/\\') { toks.push({t:'and'}); i += 2; continue; }
      if (src.substr(i,2) === '\\/') { toks.push({t:'or'});  i += 2; continue; }
      if (c === '>') { toks.push({t:'imp'}); i++; continue; }
      if (c === '&') { toks.push({t:'and'}); i++; continue; }
      if (c === '-') { toks.push({t:'not'}); i++; continue; }
      // 'v' as a bare token means or; but 'v' inside identifier is not
      if (c === 'v' && !isVarChar(src[i+1] || '') && !isVarStart(src[i-1] || '')) {
        toks.push({t:'or'}); i++; continue;
      }
      // propositional variable: letter (p q r s t) optionally with digits
      if (isVarStart(c)) {
        var j = i + 1;
        while (j < src.length && /[0-9]/.test(src[j])) j++;
        toks.push({t:'var', v: src.substring(i,j)});
        i = j; continue;
      }
      return {error: 'Unexpected character: "' + c + '"'};
    }
    return {tokens: toks};
  }
  function isVarStart(c){ return c==='p'||c==='q'||c==='r'||c==='s'||c==='t'; }
  function isVarChar(c){ return /[0-9]/.test(c); }

  // ─── Parser (recursive-descent, precedence: ¬ > ∧,∨ > →,↔) ──────────────
  // But our Tufte notes teach *official* syntax: every binary must be wrapped
  // in explicit outer parentheses. So we accept the strict grammar first, and
  // fall back to the lax precedence-based grammar only if strict fails — that
  // lets the widget report "not a formula (missing parens)" more helpfully.
  function makeParser(tokens, strict) {
    var pos = 0;
    function peek(){ return tokens[pos]; }
    function eat(t){ if (tokens[pos] && tokens[pos].t === t) { pos++; return true; } return false; }
    function expect(t){
      if (!eat(t)) throw new Error('Expected ' + t + ' at token ' + pos);
    }
    function parseFormula(){
      if (strict) return parseStrict();
      return parseImp();
    }
    // Strict: F := var | '-' F | '(' F op F ')'
    function parseStrict(){
      var tk = peek();
      if (!tk) throw new Error('Unexpected end');
      if (tk.t === 'var') { pos++; return {k:'var', v:tk.v}; }
      if (tk.t === 'not') { pos++; return {k:'not', a: parseStrict()}; }
      if (tk.t === '(')   {
        pos++;
        var left = parseStrict();
        var op = peek();
        if (!op || (op.t !== 'and' && op.t !== 'or' && op.t !== 'imp' && op.t !== 'iff')) {
          throw new Error('Expected connective inside parens');
        }
        pos++;
        var right = parseStrict();
        expect(')');
        return {k: op.t, a: left, b: right};
      }
      throw new Error('Unexpected token');
    }
    // Lax precedence grammar (only used to distinguish "wrong formula" from
    // "garbage"): iff (right) > imp (right) > or (left) > and (left) > not > atom
    function parseImp(){
      var left = parseOr();
      var t = peek();
      if (t && (t.t === 'imp' || t.t === 'iff')) { pos++; var right = parseImp(); return {k:t.t, a:left, b:right}; }
      return left;
    }
    function parseOr(){
      var left = parseAnd();
      while (peek() && peek().t === 'or') { pos++; var right = parseAnd(); left = {k:'or', a:left, b:right}; }
      return left;
    }
    function parseAnd(){
      var left = parseNot();
      while (peek() && peek().t === 'and') { pos++; var right = parseNot(); left = {k:'and', a:left, b:right}; }
      return left;
    }
    function parseNot(){
      if (peek() && peek().t === 'not') { pos++; return {k:'not', a: parseNot()}; }
      return parseAtom();
    }
    function parseAtom(){
      var t = peek();
      if (!t) throw new Error('Unexpected end');
      if (t.t === 'var') { pos++; return {k:'var', v:t.v}; }
      if (t.t === '(') {
        pos++;
        var f = parseImp();
        expect(')');
        return f;
      }
      throw new Error('Unexpected token');
    }
    return {
      parse: function(){
        var f = parseFormula();
        if (pos !== tokens.length) throw new Error('Extra tokens after formula');
        return f;
      }
    };
  }

  function parse(src, strict){
    var tk = tokenize(src);
    if (tk.error) return {error: tk.error};
    try { return {ast: makeParser(tk.tokens, strict).parse()}; }
    catch (e) { return {error: e.message}; }
  }

  function astEq(a, b){
    if (!a || !b) return false;
    if (a.k !== b.k) return false;
    if (a.k === 'var') return a.v === b.v;
    if (a.k === 'not') return astEq(a.a, b.a);
    return astEq(a.a, b.a) && astEq(a.b, b.b);
  }

  function astToLatex(a){
    if (a.k === 'var') {
      // subscript digits
      var m = /^([pqrst])([0-9]+)$/.exec(a.v);
      if (m) return m[1] + '_{' + m[2] + '}';
      return a.v;
    }
    if (a.k === 'not') return '\\neg ' + wrap(a.a);
    var op = {and:'\\wedge', or:'\\vee', imp:'\\to', iff:'\\leftrightarrow'}[a.k];
    return '(' + astToLatex(a.a) + ' ' + op + ' ' + astToLatex(a.b) + ')';
  }
  function wrap(a){
    if (a.k === 'var' || a.k === 'not') return astToLatex(a);
    return astToLatex(a);
  }

  window.checkSyn = function(btn){
    var ex = btn.closest('.syn-exercise');
    var target = ex.dataset.target;
    var input = ex.querySelector('.syn-input');
    var feedback = ex.querySelector('.syn-feedback');
    feedback.removeAttribute('hidden');

    var raw = (input.value || '').trim();
    if (!raw) {
      feedback.textContent = 'Type a formula, then press Check.';
      feedback.className = 'syn-feedback fb-note';
      return;
    }

    // Try strict parse first
    var strict = parse(raw, true);
    var lax    = parse(raw, false);
    var targetStrict = parse(target, true);
    var targetLax    = parse(target, false);
    var targetAst = targetStrict.ast || targetLax.ast;

    if (strict.ast) {
      if (astEq(strict.ast, targetAst)) {
        feedback.textContent = '✓ Correct — that is a well-formed formula matching the target.';
        feedback.className = 'syn-feedback fb-ok';
        return;
      }
      feedback.textContent = '✓ Well-formed, but not the target formula. Try again.';
      feedback.className = 'syn-feedback fb-err';
      return;
    }
    if (lax.ast) {
      if (astEq(lax.ast, targetAst)) {
        feedback.textContent = '✗ Right shape, but missing the outer parentheses required by the official syntax.';
      } else {
        feedback.textContent = '✗ Not a formula in the official syntax (check parentheses).';
      }
      feedback.className = 'syn-feedback fb-err';
      return;
    }
    feedback.textContent = '✗ Not a well-formed formula: ' + (strict.error || lax.error || 'parse failed') + '.';
    feedback.className = 'syn-feedback fb-err';
  };

  window.revealSyn = function(btn){
    var ex = btn.closest('.syn-exercise');
    var ans = ex.querySelector('.syn-answer');
    var target = ex.dataset.target;
    var mathSpan = ans.querySelector('.syn-answer-math');
    var parsed = parse(target, true).ast || parse(target, false).ast;
    if (parsed) {
      mathSpan.innerHTML = '\\(' + astToLatex(parsed) + '\\)';
    } else {
      mathSpan.textContent = target;
    }
    ans.removeAttribute('hidden');
    if (window.MathJax) {
      if (MathJax.Hub && MathJax.Hub.Queue) {
        MathJax.Hub.Queue(['Typeset', MathJax.Hub, ans]);
      } else if (MathJax.typesetPromise) {
        MathJax.typesetPromise([ans]);
      }
    }
  };
})();
</script>
"""

def parse_synchecker_block(raw):
    """Return (label, target_formula) from a SynChecker code body.

    Body is expected to be a single line like: 'A. (p & - q)'.
    Blank lines are ignored. If no leading label, label is ''.
    """
    lines = [ln.strip() for ln in raw.split('\n') if ln.strip()]
    if not lines:
        return None, None
    line = lines[0]
    m = re.match(r'^([A-Za-z0-9]+)\.\s*(.+)$', line)
    if m:
        return m.group(1), m.group(2).strip()
    return '', line

syn_counter = [0]

def make_syn_widget(label, target):
    syn_counter[0] += 1
    idx = syn_counter[0]
    label_html = f'<span class="syn-label">{escape(label)}.</span>' if label else ''
    return (
        f'<div class="syn-exercise" data-target="{escape(target, quote=True)}">\n'
        f'  <div class="syn-prompt">{label_html}Enter the formula in the official syntax.</div>\n'
        f'  <div class="syn-input-row">\n'
        f'    <input class="syn-input" type="text" spellcheck="false" autocapitalize="off" autocomplete="off" placeholder="e.g. (p &amp; - q)" aria-label="formula input {idx}">\n'
        f'  </div>\n'
        f'  <div class="syn-controls">\n'
        f'    <button class="btn-check" onclick="checkSyn(this)">Check</button>\n'
        f'    <button class="btn-reveal" onclick="revealSyn(this)">Show answer</button>\n'
        f'  </div>\n'
        f'  <div class="syn-feedback" hidden></div>\n'
        f'  <div class="syn-answer" hidden><strong>Answer:</strong> <span class="syn-answer-math"></span></div>\n'
        f'  <div class="syn-hint">Symbols: <code>-</code> ¬ &nbsp; <code>&amp;</code> ∧ &nbsp; <code>\\/</code> ∨ &nbsp; <code>-&gt;</code> → &nbsp; <code>&lt;-&gt;</code> ↔</div>\n'
        f'</div>'
    )

def transform(html):
    mc_used = [False]
    syn_used = [False]

    # ─── QualitativeProblem → MC widget ─────────────────────────────────────
    mc_pattern = re.compile(
        r'<pre[^>]*class="([^"]*QualitativeProblem[^"]*)"[^>]*><code>(.*?)</code></pre>',
        re.DOTALL
    )

    def replace_mc(m):
        classes = m.group(1)
        raw = m.group(2)
        multi = "MultipleSelection" in classes

        # Decode HTML entities in raw content
        raw = raw.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&#39;', "'").replace('&quot;', '"')

        lines = raw.split('\n')
        # First line is the label (e.g. "1." or "A.")
        label = lines[0].strip().rstrip('.') if lines else ''
        options, explanation = parse_carnap_block(label, lines[1:], multi)

        if not options:
            return m.group(0)  # leave unchanged if parsing fails

        mc_used[0] = True
        return make_widget(label, options, multi, explanation=explanation)

    result = mc_pattern.sub(replace_mc, html)

    # ─── SynChecker → formula-input widget ───────────────────────────────
    syn_pattern = re.compile(
        r'<pre[^>]*class="([^"]*SynChecker[^"]*)"[^>]*><code>(.*?)</code></pre>',
        re.DOTALL
    )
    def replace_syn(m):
        raw = m.group(2)
        raw = raw.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&#39;', "'").replace('&quot;', '"')
        label, target = parse_synchecker_block(raw)
        if not target:
            return m.group(0)
        syn_used[0] = True
        return make_syn_widget(label, target)
    result = syn_pattern.sub(replace_syn, result)

    # Inject only the CSS/JS that got used, in a stable order.
    head_extras = ''
    body_extras = ''
    if mc_used[0]:
        head_extras += MC_CSS
        body_extras += MC_JS
    if syn_used[0]:
        head_extras += SYN_CSS
        body_extras += SYN_JS
    if head_extras:
        result = result.replace('</head>', head_extras + '\n</head>', 1)
    if body_extras:
        result = result.replace('</body>', body_extras + '\n</body>', 1)

    return result

if __name__ == "__main__":
    src = sys.argv[1]
    dst = sys.argv[2]
    with open(src, 'r') as f:
        html = f.read()
    out = transform(html)
    with open(dst, 'w') as f:
        f.write(out)
    print(f"Done: {dst}")
