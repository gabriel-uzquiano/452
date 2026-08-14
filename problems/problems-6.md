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

### deontic logic

$$\textsf{KDU}$$ is a deontic logic that extends $$\textsf{KD}$$ with all substitution instances of the axiom:<br/>


$$
\textsf{O}(\textsf{O}p \to p) \tag{U}
$$
<br/>Justify the facts given below:<br/>

1. $$\textsf{KDU}$$ is sound and complete with respect to the class of serial and weakly reflexive frames. <br/>

   You may take for granted that (i) if $$\textsf{KDU}$$-consistent, a formula $$\varphi$$ is true at some world of the canonical model for $$\textsf{KDU}$$ and that (ii) the canonical model for $$\textsf{KDU}$$ is serial, which is a consequence of Proposition 8.2 in [section 8.2](https://gabriel-uzquiano.github.io/modal-logic/modalcompleteness.html#completeness-for-canonical-systems). <br/>

2. $$\textsf{KDU}$$ is *not* closed under the derived rule of inference $$\textsf{P}\varphi/\varphi$$.<br/>

3. $$\textsf{KD}$$ is closed under the derived rule of inference $$\textsf{P}\varphi/\varphi$$. <br/>

4. $$\textsf{KDU}$$ proves every substitution instance of $$\textsf{P}p \to \textsf{PP}p$$..<br/>

5. $$\textsf{KDU}$$ proves every substitution instance of $$\textsf{O}p \to \textsf{O}\textsf{P}p$$.<br/>

6. $$\textsf{KD5}$$ is a proper extension of $$\textsf{KDU}$$<br/>

7. Neither $$\textsf{KD4}$$  nor $$\textsf{KDU}$$ are extensions of each other.<br/>


Please feel free to draw from material drawn from the notes and/or solutions to earlier problem sets.

