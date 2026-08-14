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

### modal propositional logic&nbsp;

1. Draw a possible world model that shows that the relevant formula is *not* true in *all* worlds of *all* models of the specified sort.

   1. $$\Diamond p \to \Box p$$ / euclidean
   2. $$\Box (\Box p \to p)$$ / symmetric
   3. $$\Diamond(p \to q) \to (\Diamond p \to \Diamond q)$$ / reflexive
   4. $$\Box \Box p \to \Box p$$ / transitive
   5. $$\Diamond p \to \Box \Diamond p$$ / reflexive and transitive

   <br/>

2. Justify the claim that no formula of the form $$\Box \Diamond \varphi$$ is valid in all frames. 

   *Hint. You should be able to find a model in which all such formulas are in fact false at some world.*

3. Call a relation $$R$$ is *serial* on $$W$$ if, and only if, for all $$u \in W$$, there is some $$v\in W$$ such that $$uRv$$. On the other hand, a relation $$R$$ is *functional* on $$W$$ if, and only if, for all $$w, u, v \in W$$, if $$wRu$$ and $$wRv$$, then $$u = v$$. Justify the claims below:

   1. $$\Box p \to \Diamond p$$ defines the class of serial frames.

   2. $$\Diamond p \to \Box p$$ defines the class of functional frames.

      

4. Find a modal formula to define the class of *identity frames*, that is, fames of the form $$(W, R)$$, where $$R = \{(u,u): u \in W\}$$.

5. Consider the rule of inference:
   $$
   \Box \varphi / \varphi
   $$
   Justify the claim that it preserves validity with respect to the class of *all* frames.

   *Hint. Take the contrapositive. That is, you can argue that if $$\varphi$$ is not valid in all frames, then neither is $$\Box \varphi$$.*







