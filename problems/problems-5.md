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

### axiomatic derivations&nbsp;

1. Justify the facts given below:

   1. $$\Box \varphi/\varphi$$ is a derived rule of inference for $$\textsf{K}$$.

      

   2. $$\Box \varphi/\varphi$$ is a derived rule of inference for $$\textsf{KD}$$.

      

   3. $$\Box \varphi/\varphi$$ is a derived rule of inference for $$\textsf{KT}$$.

   **Hint**.

   Consider a transformation $$\sigma$$ from formulas of $$\mathcal{L}^{\Box}$$ into formulas of $$\mathcal{L}^{\Box}$$ defined by the recursion:<br/>

   
   $$
   \begin{array}{lll}
      \sigma(p) & = & p\\
      \sigma(\neg \varphi) & = &\neg \sigma(\varphi)\\
      \sigma(\varphi \to \psi) & = & \sigma(\varphi) \to \sigma(\varphi)\\
      \sigma (\Box \varphi) & = & \varphi\\
      \end{array}
   $$
   <br/>

   In other words, $$\sigma$$ scans a formula for subformulas of the form $$\Box \psi$$ and deletes the first occurrence of a modal operator in those formulas. Thus for example $$\sigma(\Box p \to \Box \Box p)$$ is just the formula: $$p \to \Box p$$, and $$\sigma(\Box p \to \Diamond p)$$, which is $$\sigma(\Box p \to \neg \Box \neg p)$$ becomes the formula: $$p \to \neg \neg p$$.

    When $$\Sigma$$ is $$\textsf{K}$$ or $$\textsf{KD}$$, use an induction on the length of proofs in $$\Sigma$$ to prove:<br/>
   
   
   $$
   \begin{array}{llll}
         \text{if} &  \vdash_{\Sigma} \varphi, & \text{then} &  \vdash_{\Sigma} \sigma(\varphi)\\
         \end{array}
   $$
   
   
   You will need a different strategy for $$\textsf{KT}$$.<br/><br/>

2. Prove $$\textsf{KB4}$$ is a *proper* extension of $$\textsf{K5}$$. That is, 

   1. All theorems of $$\textsf{K5}$$ are theorems of $$\textsf{KB4}$$.<br/>

      

   2. Not all theorems of $$\textsf{KB4}$$ are theorems of $$\textsf{K5}$$.<br/>

      

   <br/>

3. Prove that $$\textsf{K5}$$ proves the *necessitation* of every axiom of $$\textsf{KB4}$$. That is:

   1. $$\vdash_{\textsf{K5}} \Box (\varphi \to \Box \Diamond \varphi)$$<br/>

      

      

   2. $$\vdash_{\textsf{K5}} \Box (\Box \varphi \to \Box \Box \varphi)$$<br/>

   
   **Hint**
   
   One option is to outline proof schemas for $$\textsf{B}$$ and $$\textsf{4}$$ respectively, but another option is to reason semantically by exploiting the completeness of $$\textsf{K5}$$ with respect to the class of euclidean models.


   <br/>

4. Justify the facts given below:

   1. $$\Box \varphi / \varphi$$ is *not* a derived rule of inference for $$\textsf{K5}$$.<br/>

      

      

   2. $$\Box \varphi/\varphi$$ is *not* a derived rule of inference for $$\textsf{KB4}$$

      

   <br/>

   
