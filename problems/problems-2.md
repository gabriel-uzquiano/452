## problem set 2 (basic language)

*For each claim below: true or false? If true, please provide an argument. If false, provide a counterexample.*

1. Positive formulas

   Call a formula $\varphi$ of propositional logic *positive* if, and only if, there are no occurrences of negation $\neg$ in $\varphi$.

   1. Every positive formula has an odd number of symbols.

   2. Every positive formula is satisfiable.

   3. Not every formula is equivalent to a positive formula.

2. Entailment and the conditional

   Let $\Gamma$ be a set of formulas and let $\varphi$ and $\psi$ be formulas.

   1. If $\Gamma \not\models \varphi$ or $\Gamma \models \psi$, then $\Gamma \models \varphi \to \psi$.

   2. If $\Gamma \models \varphi \to \psi$, then $\Gamma \not\models \varphi$ or $\Gamma \models \psi$.

   3. If $\Gamma \not\models \varphi$ or $\Gamma \models \psi$, then $\Gamma \models \varphi \to \psi$.

3. Minimally unsatisfiable sets

   For every natural number $n > 1$, there is a set $\Gamma$ of exactly $n$ formulas such that

   - $\Gamma$ is unsatisfiable, but

   - every subset $\Delta \subseteq \Gamma$ with fewer than $n$ formulas is satisfiable.
