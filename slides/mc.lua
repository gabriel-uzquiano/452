-- Turn ::: {.mc correct="2"} blocks into the same multiple-choice widget that
-- carnap_to_mc.py builds for the notes, so slides and notes behave identically.
--
-- Authoring:
--   ::: {.mc correct="2"}
--   Is $R$ reflexive on $W$?
--
--   - yes
--   - no
--
--   Explanation: reflexivity requires $wRw$ for every $w \in W$.
--   :::
--
-- `correct` is 1-based and may list several, e.g. correct="1,3", which switches
-- the widget to checkboxes automatically.

local counter = 0

-- Render inlines to an HTML fragment, keeping math as \( \) for MathJax.
local function inlines_to_html(inls)
  return pandoc.write(pandoc.Pandoc({ pandoc.Plain(inls) }), 'html')
end

function Div(el)
  if not el.classes:includes('mc') then return nil end

  counter = counter + 1
  local name = 'ex_' .. counter

  local correct = {}
  for tok in string.gmatch(el.attributes['correct'] or '', '%d+') do
    table.insert(correct, tonumber(tok) - 1)
  end
  if #correct == 0 then
    io.stderr:write('mc.lua: block ' .. counter .. ' has no correct="" attribute\n')
  end
  local multi = #correct > 1

  local question, explanation = nil, nil
  local options = {}

  for _, blk in ipairs(el.content) do
    if blk.t == 'BulletList' or blk.t == 'OrderedList' then
      for _, item in ipairs(blk.content) do
        local first = item[1]
        table.insert(options, first and inlines_to_html(first.content) or '')
      end
    elseif blk.t == 'Para' or blk.t == 'Plain' then
      local flat = pandoc.utils.stringify(blk)
      if flat:match('^%s*Explanation:') then
        explanation = inlines_to_html(blk.content):gsub('^%s*Explanation:%s*', '')
      elseif not question then
        question = inlines_to_html(blk.content)
      end
    end
  end

  -- data-correct wants a JSON array of 0-based indices
  local json = '[' .. table.concat(correct, ',') .. ']'
  local input_type = multi and 'checkbox' or 'radio'

  local opts = {}
  for i, text in ipairs(options) do
    -- One shared name per block: radios must share a name to be mutually
    -- exclusive. Per-input names leave every radio independently checkable.
    table.insert(opts, string.format(
      '<label class="mc-option"><input type="%s" name="%s" value="%d"><span>%s</span></label>',
      input_type, name, i - 1, text))
  end

  local answers = {}
  for _, idx in ipairs(correct) do
    if options[idx + 1] then table.insert(answers, options[idx + 1]) end
  end

  local html = {}
  table.insert(html, string.format('<div class="mc-exercise" data-correct=\'%s\'%s>',
    json, multi and ' data-multi="true"' or ''))
  if question then
    table.insert(html, '<div class="mc-question">' .. question .. '</div>')
  end
  table.insert(html, '<div class="mc-options">' .. table.concat(opts, '') .. '</div>')
  table.insert(html, '<div class="mc-controls">'
    .. '<button class="btn-check" onclick="checkMC(this)">Check</button>'
    .. '<button class="btn-reveal" onclick="revealMC(this)">Show answer</button>'
    .. '</div>')
  table.insert(html, '<div class="mc-feedback" hidden></div>')
  table.insert(html, '<div class="mc-answer" hidden><strong>Answer:</strong> '
    .. table.concat(answers, '; ')
    .. (explanation and ('<div class="mc-explanation">' .. explanation .. '</div>') or '')
    .. '</div>')
  table.insert(html, '</div>')

  return pandoc.RawBlock('html', table.concat(html, '\n'))
end
