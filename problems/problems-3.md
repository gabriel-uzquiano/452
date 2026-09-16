### problem set 3 (axioms for propositional logic)

*Justify the numbered claims below.*

Consider the axiom system that results from our official system when $\textsf{A3}$ is replaced with the axiom:
   
   $$
   (\neg p \to \neg q) \to (q \to p) \tag{$\textsf{A3}^\ast$}
   $$

We write $\Gamma \vdash^\ast \varphi$ to indicate that $\varphi$ is derivable from $\Gamma$ in the new system. Now:


  $$
   \Gamma \vdash \varphi \ \Leftrightarrow \ \Gamma \vdash^\ast \varphi.
   $$

   
1. From left to right:

   For all $\Gamma$ and $\varphi$:
   
   $$
   \Gamma \vdash \varphi \ \Rightarrow \ \Gamma \vdash^\ast \varphi.
   $$
   
2. The Deduction Theorem for $\vdash^\ast$:

   For all $\Gamma$ and $\varphi$ and $\psi$:
  
   $$
   \Gamma, \varphi \vdash^\ast \psi \ \Leftrightarrow \ \Gamma \vdash^\ast \varphi \to \psi.
   $$
   
3. Lemma:

    For all $\varphi$, 
      
   $$
    \vdash^\ast  \varphi \to (\neg \varphi \to \bot)
    $$
   
4. Lemma:

    For all $\varphi$, 
    
   $$
   \vdash^\ast (\neg \varphi \to \varphi) \to \varphi
   $$
   
   
5. From right to left:

    For all $\Gamma$ and $\varphi$:
   
   $$
   \Gamma \vdash^\ast \varphi \ \Rightarrow \ \Gamma \vdash \varphi.
   $$


