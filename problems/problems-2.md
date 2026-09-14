### problem set 2 (basic language)

*True or false? If true, please provide an argument. If false, provide a counterexample.*

1. Positive formulas

   Call a formula $\varphi$ *positive* iff there are no occurrences of $\neg$ in $\varphi$.

   1. The length of a positive formula must be odd.

   2. Every positive formula is satisfiable.

   3. Not every formula is equivalent to a positive formula.

2. Logical consequence

   Let $\Gamma$ be a set of formulas and let $\varphi$ and $\psi$ be formulas.

   1. If $\Gamma \not\models \varphi$ or $\Gamma \models \psi$, then $\Gamma \models \varphi \to \psi$.

   2. If $\Gamma \models \varphi \to \psi$, then $\Gamma \not\models \varphi$ or $\Gamma \models \psi$.

   3. If $\Gamma \models \varphi$ and $\Gamma \not \models \psi$, then $\Gamma \models \neg (\varphi \to \psi)$.
   
   4. If $\Gamma \models \neg (\varphi \to \psi)$, then $\Gamma \models \varphi$ or $\Gamma \not \models \psi$.

3. Satisfiability

   1. For every natural number $n > 1$, there is a set $\Gamma$ of exactly $n$ formulas such that

      - $\Gamma$ is unsatisfiable, but

      - every subset $\Delta \subseteq \Gamma$ with fewer than $n$ formulas is satisfiable.
      
   2. There is an *infinite* set $\Gamma$ such that

      - $\Gamma$ is unsatisfiable, but

      - every *finite* subset $\Delta \subseteq \Gamma$ is satisfiable.
      
      *Please feel free to help yourself to completeness.*
