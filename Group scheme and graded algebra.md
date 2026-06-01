# $\mathbb{G}_m$, Group Schemes, and Gradings

---

## 1. What is $\mathbb{G}_m$?

As a scheme, $\mathbb{G}_m = \operatorname{Spec}(k[u, u^{-1}])$. Its $k$-points are ring maps $k[u, u^{-1}] \to k$, each of which is determined by where $u$ goes — and since $u$ must map to an invertible element, the $k$-points are exactly $k^\times$.

So $\mathbb{G}_m$ is the algebraic geometry version of $\mathbb{C}^*$: the multiplicative group of nonzero scalars.

---

## 2. Why is the Group Law on $\mathbb{G}_m$ Ordinary Multiplication?

A group scheme is a scheme $G$ equipped with three morphisms encoding the group axioms on the level of schemes:

$$\mu: G \times G \to G \quad \text{(multiplication)}, \qquad e: \operatorname{Spec}(k) \to G \quad \text{(unit)}, \qquad \iota: G \to G \quad \text{(inverse)}.$$

For $\mathbb{G}_m$, on the level of rings these are:

$$\mu^*: k[u, u^{-1}] \to k[u, u^{-1}] \otimes_k k[u, u^{-1}], \qquad u \mapsto u \otimes u,$$
* For example, $\mu^*(u^2+2/u + 1) = u^2\otimes u^2 + 2 u^{-1}\otimes u^{-1}+1\otimes 1$. Note that it does not send $f$ to $f\otimes f$ in general.  Only the generator $u$ is important, don't care others.
$$e^*: k[u, u^{-1}] \to k, \qquad u \mapsto 1,$$ $$\iota^*: k[u, u^{-1}] \to k[u, u^{-1}], \qquad u \mapsto u^{-1}.$$

**Why does $\mu^*: u \mapsto u \otimes u$ correspond to multiplication of $\mathbb{C}^*$?**

Recall that 
* a $k$-point of $\mathbb{G}_m$ is a ring map $\phi: k[u, u^{-1}] \to k$, determined by $\phi(u) = \lambda \in k^\times$. Write $\phi_\lambda$ for this point.
And
* A $k$-point of $\mathbb{G}_m \times \mathbb{G}_m$ is a pair $(\lambda, \mu) \in k^\times \times k^\times$, corresponding to the ring map

$$\phi_\lambda \otimes \phi_\mu : k[u, u^{-1}] \otimes k[u, u^{-1}] \to k, \qquad a \otimes b \mapsto \phi_\lambda(a) \cdot \phi_\mu(b).$$

The group law on $k$-points induced by $\mu$ is the composite:

$$k[u, u^{-1}] \xrightarrow{\mu^*} k[u, u^{-1}] \otimes k[u, u^{-1}] \xrightarrow{\phi_\lambda \otimes \phi_\mu} k.$$

Tracing $u$: it goes $u \mapsto u \otimes u \mapsto \lambda \cdot \mu$. So the group law sends $(\lambda, \mu) \mapsto \lambda\mu$ — ordinary multiplication in $k^\times$. This is why $\mathbb{G}_m(k) = k^\times$ as a group, matching $\mathbb{C}^*$ when $k = \mathbb{C}$.

Similarly, $e^*: u \mapsto 1$ says the unit element is $1 \in k^\times$, and $\iota^*: u \mapsto u^{-1}$ says the inverse of $\lambda$ is $\lambda^{-1}$.

---

## 3. What is a $\mathbb{G}_m$-Action on a Scheme?

A $\mathbb{G}_m$-action on a scheme $X$ is a morphism

$$\sigma: \mathbb{G}_m \times X \to X$$

satisfying two axioms:

- **Unit:** $\sigma(1, x) = x$ for all $x \in X$.
- **Associativity:** $\sigma(\lambda\mu, x) = \sigma(\lambda, \sigma(\mu, x))$ for all $\lambda, \mu \in \mathbb{G}_m$, $x \in X$.

On $k$-points this is just an ordinary group action of $k^\times$ on the set $X(k)$, so the intuition from $\mathbb{C}^*$-actions carries over directly.

**On the level of rings**, for $X = \operatorname{Spec}(S)$, the morphism $\sigma$ corresponds to a ring homomorphism

$$\sigma^*: S \to k[u, u^{-1}] \otimes_k S = S[u, u^{-1}].$$
Let $\phi_\lambda$ be the evaluation map $u\mapsto \lambda$.
The two axioms become:

- **Unit axiom:** The composite $S \xrightarrow{\sigma^*} S[u, u^{-1}] \xrightarrow{\phi_1} S$ is the identity.
- **Associativity axiom:** $(\phi_\mu\circ\sigma^*)(\phi_\lambda\circ \sigma^*)(s)=(\phi_{\lambda\mu}\circ \sigma^*)(s)$.



---

## 4. Why a $\mathbb{G}_m$-Action is the Same as a Grading

This is the key theorem. We show the two axioms force $\sigma^*$ to be exactly a grading decomposition.

**Step 1: Decompose into $u$-degrees.**

Since $\sigma^*(s) \in S[u, u^{-1}]$, we can write

$$\sigma^*(s) = \sum_{n \in \mathbb{Z}} s_n u^n, \qquad s_n \in S,$$

where only finitely many $s_n$ are nonzero.

**Step 2: Apply the unit axiom.**

Setting $u = 1$ (applying $e^*: u \mapsto 1$) to $\sigma^*(s) = \sum_n s_n u^n$ gives

$$s = \sum_{n \in \mathbb{Z}} s_n.$$

So the $s_n$ are a decomposition of $s$ into pieces, with the pieces summing to $s$.


**Step 3: Apply the associativity axiom.**

**Claim.** Let $\sigma^*(s) = \sum_{n\in \mathbb{Z}}s_nu^n$. Then $\sigma^*(s_n) = s_n u^n$. 

*Proof of claim.* The axiom says $(\phi_\mu \circ \sigma^*) \circ (\phi_\lambda \circ \sigma^*) = \phi_{\lambda\mu} \circ \sigma^*$. Apply both sides to $s \in S$.

**Right side:** straightforward,

$$(\phi_{\lambda\mu} \circ \sigma^*)(s) = \phi_{\lambda\mu}\!\left(\sum_n s_n u^n\right) = \sum_n s_n (\lambda\mu)^n = \sum_n s_n \lambda^n \mu^n.$$

**Left side:** first apply $\phi_\lambda \circ \sigma^*$, then apply $\phi_\mu \circ \sigma^*$ to the result,

$$(\phi_\lambda \circ \sigma^*)(s) = \sum_n s_n \lambda^n \in S,$$

$$(\phi_\mu \circ \sigma^*)\!\left(\sum_n s_n \lambda^n\right) = \phi_\mu\!\left(\sigma^*\!\left(\sum_n s_n \lambda^n\right)\right) = \phi_\mu\!\left(\sum_n \lambda^n \sigma^*(s_n)\right) = \sum_n \lambda^n \phi_\mu(\sigma^*(s_n)).$$

**Matching** the two sides and comparing coefficients of $\lambda^n$:

$$\phi_\mu(\sigma^*(s_n)) = s_n \mu^n \quad \text{for all } \mu \in k^\times, \text{ all } n.$$

This says $s_n$ is homogeneous of degree $n$: $\sigma^*(s_n) = s_n u^n$.

**Step 4: Conclusion.**

Setting $S_n = {s \in S : \sigma^*(s) = s \cdot u^n}$, the decomposition $s = \sum_n s_n$ from Step 2 is exactly the grading $S = \bigoplus_{n \in \mathbb{Z}} S_n$. The ring structure is compatible with the grading because $\sigma^*$ is a ring map: $\sigma^*(ab) = \sigma^*(a)\sigma^*(b)$ forces $S_m \cdot S_n \subseteq S_{m+n}$.

**Summary:**

$$\boxed{\text{A } \mathbb{G}_m\text{-action on } \operatorname{Spec}(S) ;\longleftrightarrow; \text{A grading } S = \bigoplus_{n \in \mathbb{Z}} S_n.}$$

---

## 5. Application: The Normal Cone $C_X Y$

The normal cone is $C_X Y = \operatorname{Spec}(\operatorname{gr}_I(A))$, where $\operatorname{gr}_I(A) = \bigoplus_{n \geq 0} I^n/I^{n+1}$ is graded by vanishing order along $I$.

By the equivalence above, this grading gives a $\mathbb{G}_m$-action on $C_X Y$. On $k$-points, $\lambda \in k^\times$ acts by

$$\lambda \cdot [a] = \lambda^n [a], \qquad [a] \in I^n/I^{n+1}.$$

Since $t$ tracks vanishing order (as established in the Rees algebra note), this action is simply $\lambda \cdot t = \lambda t$ — scaling the fiber coordinate by $\lambda$. The zero section $X \hookrightarrow C_X Y$ is the fixed locus: elements of $I^0/I^1 = A/I$ are in degree $0$, scaled by $\lambda^0 = 1$.

This is the algebraic analogue of the $\mathbb{C}^*$-action on the total space of a vector bundle that scales each fiber by $\lambda$, fixing the zero section.