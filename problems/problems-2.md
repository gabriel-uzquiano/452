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


### propositional logic: syntax and semantics

1. Call a formula $$\varphi$$ of propositional logic *positive* if, and only if, there are no occurrences of negation $$\neg$$ in $$\varphi$$. Justify each of the following claims:&nbsp;

   1. Every positive formula has an odd number of symbols.

   2. Every positive formula is satisfiable.&nbsp;

      

2. True or false? If true, please provide an argument. If false, provide a counterexample.&nbsp;

   1. Given a set of formulas $$\Gamma$$ and two formulas $$\varphi$$ and $$\psi$$, 

      if $$\Gamma \not \models \varphi$$ or $$\Gamma \models \psi$$, then $$\Gamma \models \varphi \to \psi$$.

   2. Given a set of formulas $$\Gamma$$ and two formulas $$\varphi$$ and $$\psi$$, 

      if $$\Gamma \models \varphi \to \psi$$, then $$\Gamma \not \models \varphi$$ or $$\Gamma \models \psi$$.&nbsp;
      
      

3. Show that for every natural number $$n > 1$$, there is a set $$\Gamma$$ of exactly $$n$$ formulas such that&nbsp;

   1. $$\Gamma$$ is unsatisfiable, but

   2. Every subset $$\Delta \subseteq \Gamma$$ with fewer than $$n$$ formulas is satisfiable.&nbsp;

