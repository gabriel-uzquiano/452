---


---

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>
<script>
  const password = "MHP102";
  const userInput = prompt("Enter password to view this page:");
   if (userInput !== password) {
    document.body.innerHTML = "<h2>access denied</h2>";
  }
</script>

## problems

### propositional logic: axiomatic derivations

**Choose your own adventure.** Please plan to write solutions to either problems 1, 2, and 3, or to problems 2, 3, and 4.<br/><br/>



1. Show that the deductive system we have introduced is *sound*: a formula $$\varphi$$ is provable from a set of formulas $$\Gamma$$ only if $$\varphi$$ is a logical consequence of $$\Gamma$$. That is, &nbsp;

   

   $$
   \Gamma \vdash \varphi \ \text{only if} \ \Gamma \models \varphi.
   $$
   
   *Hint: Use complete induction  (without a base case) to argue that for every positive integer $$n$$, if $$\langle \chi_1, ..., \chi_n\rangle$$ is a derivation of $$\varphi$$ from $$\Gamma$$, then $$\Gamma \models \varphi$$.*&nbsp;
   
2. Show that given a set $$\Gamma$$ and formulas $$\varphi$$ and $$\psi$$​, &nbsp;

   

   $$
   \Gamma \vdash (\varphi \to \neg \varphi) \to \neg \varphi
   $$

3. Show that given a set $$\Gamma$$ and a formula $$\varphi$$, $$\Gamma$$ is inconsistent if both $$\Gamma, \varphi$$ and $$\Gamma, \neg \varphi$$ are.&nbsp;

   *Hint: Please feel free to make use of the Deduction Theorem and whatever propositions you may find helpful from the notes.*&nbsp;

4. Consider the axiomatic system that results from our axiom system when $$\textsf{A3}$$ is replaced with the axiom:&nbsp;
   $$
   (\neg p \to \neg q) \to (q \to p) \tag{$\textsf{A3}^\ast$}
   $$

   We write $$\Gamma \vdash^\ast \varphi$$ to indicate that $$\varphi$$ is derivable from $$\Gamma$$ in the new system. Justify the equivalence between the two axiom systems. That is, prove that no matter what $$\Gamma$$ and $$\varphi$$ may be,&nbsp;

   

   $$
   \Gamma \vdash \varphi \ \text{iff} \ \Gamma \vdash^\ast \varphi.
   $$
   
   *Hint: Please note that the argument for the Deduction Theorem carries over to the new system without incident. Further hints available upon request.*



