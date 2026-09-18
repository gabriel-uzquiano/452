### problem set 3 (axioms and models)


1. **Axioms for propositional logic**

   Consider the axiom system that results from our official system when $\textsf{A3}$ is replaced with the axiom:

   $$
   (\neg p \to \neg q) \to (q \to p) \tag{$\textsf{A3}^\ast$}
   $$

   We write $\Gamma \vdash^\ast \varphi$ to indicate that $\varphi$ is derivable from $\Gamma$ in the new system. Now, for all $\Gamma$ and $\varphi$:

   $$
   \Gamma \vdash \varphi \ \Leftrightarrow \ \Gamma \vdash^\ast \varphi.
   $$
   
   Justify the claims below:

   1. For all $\Gamma$ and $\varphi$:

      $$
      \Gamma \vdash \varphi \ \Rightarrow \ \Gamma \vdash^\ast \varphi.
      $$

   2. The Deduction Theorem for $\vdash^\ast$:

      For all $\Gamma$, $\varphi$, and $\psi$:

      $$
      \Gamma, \varphi \vdash^\ast \psi \ \Leftrightarrow \ \Gamma \vdash^\ast \varphi \to \psi.
      $$
      
      
   3. For all $\varphi$, $\vdash^\ast \varphi \to (\neg \varphi \to \bot)$.

     
   4. For all $\varphi$, $\vdash^\ast (\neg \varphi \to \varphi) \to \varphi$.


   5. For all $\Gamma$ and $\varphi$:

      $$
      \Gamma \vdash^\ast \varphi \ \Rightarrow \ \Gamma \vdash \varphi.
      $$

2. **Possible worlds models**

   Provide possible worlds models in order to justify that not every substitution instance of the relevant formula is true in every world of the relevant class of models.

   1. $\Diamond p \to \Box p$ / euclidean
   
   2. $\Box (\Box p \to p)$ / symmetric
   
   3. $\Diamond (p \to q) \to (\Diamond p \to \Diamond q)$ / reflexive
   
   4. $\Box \Box p \to \Box p$ / transitive
   
   5. $\Diamond p \to \Box \Diamond p$ / reflexive and transitive
