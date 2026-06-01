## Setup

Let $f: X \to Y$ be a morphism of schemes. Fix a point $y \in Y$.
In the affine case, let $X = \operatorname{Spec} A$, $Y = \operatorname{Spec} B$,
and let $\varphi: B \to A$ be the corresponding ring homomorphism,
so that $y$ corresponds to a prime ideal $\mathfrak{p} \subset B$.

We want to understand the **fiber of $f$ over $y$**, written $f^{-1}(y)$.

---

## Step 1: The Naive Definition of $f^{-1}(y)$

The first definition one thinks of is purely set-theoretic:

$$f^{-1}(y) := \{ x \in X \mid f(x) = y \}.$$

Translating into algebra, $f(x) = y$ means the induced map on local rings sends
$\mathfrak{p}$ to the prime $\mathfrak{q} = f(x) \in \operatorname{Spec} A$ in the sense that

$$\varphi^{-1}(\mathfrak{q}) = \mathfrak{p}.$$

So the fiber as a **set** is

$$f^{-1}(y) = \{ \mathfrak{q} \in \operatorname{Spec} A \mid \varphi^{-1}(\mathfrak{q}) = \mathfrak{p} \}.$$

This is a perfectly good set, and with the subspace topology from $\operatorname{Spec} A$
it is a topological space. But it carries **no natural scheme structure** yet —
it is not obviously the Spec of any ring. To get a scheme, we need the fiber product.

---

## Step 2: The Residue Field and the Canonical Map $\operatorname{Spec} \kappa(y) \to Y$

Before that, we should understand first what "a point on Y" means in scheme theory.

Every point $y \in Y$ has an associated **residue field**

$$\kappa(y) := \mathcal{O}_{Y,y} / \mathfrak{m}_{Y,y}.$$

In the affine case, with $y = \mathfrak{p} \in \operatorname{Spec} B$, this is

$$\kappa(\mathfrak{p}) = B_\mathfrak{p} / \mathfrak{p} B_\mathfrak{p} = \operatorname{Frac}(B/\mathfrak{p}).$$

The residue field fits into a two-step factorization of the canonical ring map
$B \to \kappa(\mathfrak{p})$:

$$B \xrightarrow{\text{quotient}} B/\mathfrak{p} \xrightarrow{\text{localize}} \operatorname{Frac}(B/\mathfrak{p}) = \kappa(\mathfrak{p}).$$

This ring map $B \to \kappa(\mathfrak{p})$ corresponds geometrically to a morphism
of schemes

$$i_y : \operatorname{Spec} \kappa(y) \longrightarrow Y,$$

whose image is the single point $\{y\}$. Intuitively, $\operatorname{Spec} \kappa(y)$ is the "scheme-theoretic incarnation of the point $y$."

More precisely, we get 
* A point $y$ on $Y$ is a $Y$-scheme $\operatorname{Spec} \kappa(y)\to Y$.
The geometric intuition of this is: to locate a point $y$, we 
* first find a closed subscheme $\operatorname{Spec}(B/\mathfrak p)$ containing $y$.
* The do the localization to find where it precisely is.

---

## Step 3: The Scheme-Theoretic Fiber Is a Fiber Product

The **scheme-theoretic fiber** of $f$ over $y$ is defined as the fiber product

$$X_y := X \times_Y \operatorname{Spec} \kappa(y).$$

This is the correct definition: it pulls the scheme $X$ back to the "point" $\operatorname{Spec} \kappa(y)$,
and the result is a scheme over $\kappa(y)$. 
* Recall that: Let $X\to Y$ be a scheme over $Y$, and $Z\to Y$ be another scheme over $Y$. Then we can pullback $X$ to a scheme over $Z$ by taking the fiber product $X\times_Y Z\to Z$.

The map $X_y \to X$ is a closed immersion composed with an open immersion, and it gives $f^{-1}(y)$ its scheme structure.

In the affine case, the fiber product of rings is the tensor product, so

$$X_y = \operatorname{Spec}\!\left(A \otimes_B \kappa(\mathfrak{p})\right).$$

It remains to verify that the **underlying set** of this scheme is exactly the
set $\{\mathfrak{q} \in \operatorname{Spec} A \mid \varphi^{-1}(\mathfrak{q}) = \mathfrak{p}\}$
identified in Step 1.

---

## Step 4: Computing $A \otimes_B \kappa(\mathfrak{p})$ and Identifying Its Primes

We use the two-step factorization of $B \to \kappa(\mathfrak{p})$ from Step 2.

### Step 4a: Quotient — $B \to B/\mathfrak{p}$

Tensoring $A$ over $B$ with $B/\mathfrak{p}$ gives

$$A \otimes_B B/\mathfrak{p} \cong A / \varphi(\mathfrak{p}) A =: A/\mathfrak{p}^e,$$

where $\mathfrak{p}^e = \varphi(\mathfrak{p}) \cdot A$ is the **extended ideal** of $\mathfrak{p}$ in $A$.
- Proofs
	- **Proof via right-exactness of $\otimes$.**
		Start with the short exact sequence of $B$-modules
	  $$\mathfrak{p} \xrightarrow{\iota} B \xrightarrow{\pi} B/\mathfrak{p} \to 0.$$
	  Tensor over $B$ with $A$. Since $- \otimes_B A$ is right-exact, the sequence remains exact:
	  $$\mathfrak{p} \otimes_B A \xrightarrow{\iota \otimes 1} B \otimes_B A \xrightarrow{\pi \otimes 1} (B/\mathfrak{p}) \otimes_B A \to 0.$$
	  Use the canonical isomorphism $B \otimes_B A \cong A$ sending $b \otimes a \mapsto \varphi(b)a$.
	  Under this identification, the map $\iota \otimes 1$ becomes
	  $$\mathfrak{p} \otimes_B A \to A, \qquad b \otimes a \mapsto \varphi(b) \cdot a,$$
	  whose image is $\mathfrak{p}^e = \varphi(\mathfrak{p}) \cdot A$. Exactness gives $A/\mathfrak{p}^e \cong \operatorname{coker}(\iota \otimes 1) \cong (B/\mathfrak{p}) \otimes_B A$. $\square$
	- **Alternative: explicit maps.**
	  Define $\psi : A \to A \otimes_B B/\mathfrak{p}$ by $a \mapsto a \otimes \bar{1}$.
	  This is surjective: every generator satisfies $a \otimes \bar{b} = a\varphi(b) \otimes \bar{1} = \psi(a\varphi(b))$
	  by $B$-linearity of the tensor. The kernel is those $a$ with $a \otimes \bar{1} = 0$,
	  which are exactly the elements in the image of $\mathfrak{p} \otimes_B A \to A$, namely $\mathfrak{p}^e$.
	  So $\ker\psi = \mathfrak{p}^e$ and the first isomorphism theorem gives $A \otimes_B B/\mathfrak{p} \cong A/\mathfrak{p}^e$. $\square$


Geometrically, $\operatorname{Spec}(A/\mathfrak{p}^e) = f^{-1}(V(\mathfrak{p}))$ = $f^{-1}\overline{\{y\}}$.
* LHS = $\{\mathfrak q\in \operatorname{Spec}A:q\supset \varphi(p)\} = \{ \mathfrak{q}\in \operatorname{Spec}A:\varphi^{-1}(\mathfrak{q})\supset \mathfrak p\} = \{f(\mathfrak q)\in V(\mathfrak p)\}$ = RHS. 
is the closed subscheme of $X$ cut out by the
condition "$\mathfrak{p}$ vanishes," and is also the scheme-theoretic preimage of the closed subscheme
$\overline{\{y\}} \hookrightarrow Y$.

The primes of $A/\mathfrak{p}^e$ are the primes $\mathfrak{q}$ of $A$ with $\varphi(\mathfrak{p}) \subseteq \mathfrak{q}$,
equivalently $\varphi^{-1}(\mathfrak{q}) \supseteq \mathfrak{p}$. This is the condition that $\mathfrak{q}$
lies **over a specialization of $\mathfrak{p}$** — too broad, since it includes primes lying over ideals larger than $\mathfrak{p}$.
- The name "specialization" comes from the following geometric intuition. Work over an
  algebraically closed field $k$, so that classical points of $\mathbb{A}^2_k$ correspond
  to maximal ideals of $k[x,y]$ by the Nullstellensatz. Let $\mathfrak{p}$ be a non-maximal
  prime; it is the generic point of the irreducible curve $C \subset \mathbb{A}^2_k$ it
  defines, in the sense that $\overline{\{\mathfrak{p}\}} = V(\mathfrak{p})$. A classical
  point $\mathfrak{m}$ lies on $C$ if and only if $\mathfrak{m} \in V(\mathfrak{p})$, i.e.,
  it is a specialization of $\mathfrak{p}$. The terminology reflects that $\mathfrak{m}$ is
  a fully pinned-down point on $C$, while $\mathfrak{p}$ only knows you are somewhere on $C$.

Recall our intuition of "finding a point", this step we have find the $B/\mathfrak{p}$-algebra $\operatorname{Spec}(A/\mathfrak p^e)$, it is
* the set $f^{-1}\overline{\{y\}}$
* the fiber over a generic point with $y$ as a specialization, 
	* In other words, it is a scheme over $\operatorname{B/\mathfrak p}$.
not $f^{-1}(y)$. To locate $f^{-1}(y)$ we "shrink"(by localization) the scheme $\operatorname{Spec}(A/\mathfrak p^e)$ over $B/\mathfrak p$ to over $y$. 
### Step 4b: Localization — $B/\mathfrak{p} \to \kappa(\mathfrak{p}) = \operatorname{Frac}(B/\mathfrak{p})$

We now localize $A/\mathfrak{p}^e$ at the image of the multiplicative set $S = B \setminus \mathfrak{p}$
under $B \to B/\mathfrak{p} \to A/\mathfrak{p}^e$. This gives
$$A \otimes_B \kappa(\mathfrak{p}) \cong (A/\mathfrak{p}^e) \otimes_{B/\mathfrak{p}} \kappa(\mathfrak{p})
= S^{-1}(A/\mathfrak{p}^e),$$

where $S = \varphi(B \setminus \mathfrak{p})$ (viewed in $A$, then in $A/\mathfrak{p}^e$).
* Proof of the second identity: Recall that on the category of $R$-modules for general $R$, the localization $S^{-1}M$ is, by definition, canonically isomorphic to the extension of scalers $M\otimes_{R} S^{-1}R$. Applying this in the category of $B/\mathfrak{p}$-algebras we get $S^{-1}(A/\mathfrak p^e)\simeq A/\mathfrak{p}^e \otimes_{B/\mathfrak{p}}\kappa(p)$.
* Proof of the first identity: Before we have showed that $A/\mathfrak p^c \simeq A\otimes_B B/\mathfrak p$. Then plugin we get the middle term $\simeq A\otimes_B B/\mathfrak p \otimes_{B/\mathfrak p}\kappa(\mathfrak p) = A\otimes_B \kappa(\mathfrak p)$. 

Localization at $S$ removes all primes $\mathfrak{q}$ that meet $S$, i.e., all primes $\mathfrak{q}$
for which $\mathfrak{q} \cap \varphi(B \setminus \mathfrak{p}) \neq \emptyset$,
equivalently $\varphi^{-1}(\mathfrak{q}) \not\subseteq \mathfrak{p}$.

### The Two Conditions Together

A prime $\mathfrak{q} \in \operatorname{Spec} A$ survives both operations — the quotient and the localization — if and only if:

1. From Step 4a (quotient by $\mathfrak{p}^e$): $\varphi^{-1}(\mathfrak{q}) \supseteq \mathfrak{p}$.
2. From Step 4b (localization at $S = B \setminus \mathfrak{p}$): $\varphi^{-1}(\mathfrak{q}) \subseteq \mathfrak{p}$.

Together these force

$$\varphi^{-1}(\mathfrak{q}) = \mathfrak{p},$$

which is exactly the condition that $\mathfrak{q}$ lies in the set-theoretic fiber $f^{-1}(y)$.

**Conclusion.** The underlying set of $\operatorname{Spec}(A \otimes_B \kappa(\mathfrak{p}))$ is in natural bijection with

$$\{ \mathfrak{q} \in \operatorname{Spec} A \mid \varphi^{-1}(\mathfrak{q}) = \mathfrak{p} \} = f^{-1}(y).$$

The scheme structure on this set — which the naive set-theoretic definition could not provide — comes from the ring $A \otimes_B \kappa(\mathfrak{p})$.

---

## Summary: The Two Operations and What They Cut Out

The isomorphism $f^{-1}(y) \cong \operatorname{Spec}(A \otimes_B \kappa(\mathfrak{p}))$ is a consequence of the
two-step factorization $B \to B/\mathfrak{p} \to \kappa(\mathfrak{p})$, with each step having a geometric meaning:

| Step | Algebra | Geometry | Effect on primes |
|---|---|---|---|
| Quotient | $A \to A/\mathfrak{p}^e$ | Restrict to $\overline{\{y\}}$ | Keep $\mathfrak{q}$ with $\varphi^{-1}(\mathfrak{q}) \supseteq \mathfrak{p}$ |
| Localize | $A/\mathfrak{p}^e \to S^{-1}(A/\mathfrak{p}^e)$ | Restrict to the generic point of $\overline{\{y\}}$ | Keep $\mathfrak{q}$ with $\varphi^{-1}(\mathfrak{q}) \subseteq \mathfrak{p}$ |
| **Combined** | $A \to A \otimes_B \kappa(\mathfrak{p})$ | **The fiber $f^{-1}(y)$** | Keep $\mathfrak{q}$ with $\varphi^{-1}(\mathfrak{q}) = \mathfrak{p}$ |

---

## Relation to the Spec ℤ[x] Example

In the previous note, the two cases in the proof of Proposition 1.1 are exactly these two operations applied to the map $\mathbb{Z} \hookrightarrow \mathbb{Z}[x]$:

- **Case 1** ($\mathfrak{p} = (0) \in \operatorname{Spec} \mathbb{Z}$): the residue field is $\kappa((0)) = \mathbb{Q}$.
  Tensoring gives $\mathbb{Z}[x] \otimes_\mathbb{Z} \mathbb{Q} = \mathbb{Q}[x]$, the generic fiber.
  The localization step (inverting $\mathbb{Z} \setminus \{0\}$) is exactly what the proof calls
  "localizing at the prime (0)."

- **Case 2** ($\mathfrak{p} = (p)$): the residue field is $\kappa((p)) = \mathbb{F}_p$.
  Tensoring gives $\mathbb{Z}[x] \otimes_\mathbb{Z} \mathbb{F}_p = \mathbb{F}_p[x]$, the special fiber over $p$.
  The quotient step (modding out by $(p)$) is what the proof calls the "base change $\mathbb{Z}[x] \to \mathbb{F}_p[x]$."

The condition $\varphi^{-1}(\mathfrak{q}) = \mathfrak{p}$ is the exact equation the proof uses to determine
which prime ideals of $\mathbb{Z}[x]$ lie over a given prime of $\mathbb{Z}$ — now seen as the
characterization of points of a fiber product.
