### problem set 5 (landscape of normal modal logics)

You may use the soundness and completeness results from the slides: each system in the landscape is sound and complete with respect to the corresponding class of frames.

A rule $\varphi/\psi$ is **admissible** in a system $\Sigma$ when the theorems of $\Sigma$ are closed under it: if $\vdash_\Sigma \varphi$, then $\vdash_\Sigma \psi$.

1. Admissibility of $\Box \varphi / \varphi$.

   1. $\Box \varphi/\varphi$ is admissible in $\textsf{K}$. That is, for each modal formula $\varphi$, if $\vdash_\textsf{K} \Box \varphi$, then $\vdash_\textsf{K} \varphi$.

      *Hint: given a countermodel for $\varphi$ at a world $w$, add a new world $w_0$ that sees only $w$.*

   2. Explain why your construction from 1.1 is not available for $\textsf{K5}$: give a euclidean frame and a world $w$ such that adding a new world $w_0$ that sees only $w$ yields a frame that is not euclidean.


2. $\textsf{KB4}$ is a *proper* extension of $\textsf{K5}$:

   1. $\textsf{K5} \sqsubseteq \textsf{KB4}$. You may give a *semantic* argument: use the fact that every symmetric and transitive frame is euclidean, and explain why that suffices.

   2. $\textsf{KB4} \not\sqsubseteq \textsf{K5}$.


3. $\textsf{K5}$ proves the *necessitation* of every axiom of $\textsf{KB4}$. That is:

   1. $\vdash_{\textsf{K5}} \Box (\varphi \to \Box \Diamond \varphi)$.

   2. $\vdash_{\textsf{K5}} \Box (\Box \varphi \to \Box \Box \varphi)$.

   *You may use the fact that $\textsf{K5}$ is sound and complete with respect to the class of euclidean frames.*


4. Use your answers to the previous problems to show:

   1. $\Box \varphi / \varphi$ is *not* admissible in $\textsf{K5}$.

   2. $\Box \varphi/\varphi$ is *not* admissible in $\textsf{KB4}$.

    
