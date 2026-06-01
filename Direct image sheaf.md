# Direct Image Sheaf

## Definition

Let $f: X \to Y$ be a morphism of schemes, $\mathcal{F}$ a quasi-coherent sheaf on $X$. The **direct image** (or **pushforward**) $f_*\mathcal{F}$ is the sheaf on $Y$ defined by

$$(f_*\mathcal{F})(U) := \mathcal{F}(f^{-1}(U))$$

for every open $U \subset Y$. Restriction maps: for $V \subset U$, $f^{-1}(V) \subset f^{-1}(U)$, so the restriction of $\mathcal{F}$ gives a map $(f_*\mathcal{F})(U) \to (f_*\mathcal{F})(V)$.

**This is a definition, not a theorem.** The sheaf axioms for $f_*\mathcal{F}$ follow immediately from those of $\mathcal{F}$: since $f^{-1}$ commutes with unions and intersections, any open cover $U = \bigcup U_i$ gives an open cover $f^{-1}(U) = \bigcup f^{-1}(U_i)$, and gluing for $\mathcal{F}$ on the latter implies gluing for $f_*\mathcal{F}$ on the former.

---

## Algebraic description in the affine case

Let $f: X = \operatorname{Spec}(A) \to Y = \operatorname{Spec}(B)$, induced by a ring map $f^\#: B \to A$. Let $\mathcal{F} = \widetilde{M}$ for an $A$-module $M$.

**Claim:** $f_*\widetilde{M} \cong \widetilde{M_B}$, where $M_B$ denotes $M$ viewed as a $B$-module via restriction of scalars along $f^\#$.

**Verification.** A sheaf on $\operatorname{Spec}(B)$ is determined by its sections on basic opens $D(g) = \{\mathfrak{p}: g \notin \mathfrak{p}\}$ for $g \in B$. We check both sides agree on every $D(g)$.

*Left side* (definition of pushforward): Since $\mathfrak{q} \in f^{-1}(D(g))$ iff $f(\mathfrak{q}) = f^{\#,-1}(\mathfrak{q}) \in D(g)$ iff $g \notin f^{\#,-1}(\mathfrak{q})$ iff $f^\#(g) \notin \mathfrak{q}$, we have
$$f^{-1}(D(g)) = D(f^\#(g)) \subset \operatorname{Spec}(A).$$
Therefore
$$(f_*\widetilde{M})(D(g)) = \widetilde{M}(D(f^\#(g))) = M_{f^\#(g)},$$
the localization of $M$ at the element $f^\#(g) \in A$.

*Right side* (sheaf associated to $M_B$):
$$\widetilde{M_B}(D(g)) = (M_B)_g,$$
the localization of $M$ at $g \in B$.

It remains to show $(M_B)_g \cong M_{f^\#(g)}$.

### Universal property of localization

Let $R$ be a ring, $S \subset R$ a multiplicative set, $M$ an $R$-module. The **localization** $S^{-1}M$ is an $R$-module together with an $R$-linear map $\iota: M \to S^{-1}M$ satisfying:

> For any $R$-module $N$ and $R$-linear $\phi: M \to N$ such that every $s \in S$ acts invertibly on $N$, there exists a **unique** $R$-linear $\bar\phi: S^{-1}M \to N$ with $\bar\phi \circ \iota = \phi$.

Any two objects satisfying this property are canonically isomorphic.

### $(M_B)_g \cong (M_{f^\#(g)})_B$

Write **$A$-UP** for the universal property of $M_{f^\#(g)}$ as an $A$-module localization (inverting $f^\#(g) \in A$), and **$B$-UP** for the universal property of $(M_B)_g$ as a $B$-module localization (inverting $g \in B$). Both are instances of the general universal property stated above.

Let $\iota_A: M \to M_{f^\#(g)}$ and $\iota_B: M \to (M_B)_g$ denote the two localization maps.

**Step 1. Construct $\alpha: M_{f^\#(g)} \to (M_B)_g$** via the $A$-UP.
$(M_B)_g$ is an $A$-module and $f^\#(g)$ acts invertibly there (as $g$, which is invertible). So the $A$-UP applied to the $A$-linear map $\iota_B: M \to (M_B)_g$ gives a unique $A$-linear
$$\alpha: M_{f^\#(g)} \longrightarrow (M_B)_g \quad\text{with}\quad \alpha\circ\iota_A = \iota_B.$$

**Step 2. Construct $\beta: (M_B)_g \to (M_{f^\#(g)})_B$** via the $B$-UP.
$(M_{f^\#(g)})_B$ is a $B$-module and $g$ acts invertibly there (as $f^\#(g)$, which is invertible). So the $B$-UP applied to the $B$-linear map $\iota_A: M_B \to (M_{f^\#(g)})_B$ gives a unique $B$-linear
$$\beta: (M_B)_g \longrightarrow (M_{f^\#(g)})_B \quad\text{with}\quad \beta\circ\iota_B = \iota_A.$$

**Step 3. $\alpha\circ\beta = \mathrm{id}_{(M_B)_g}$.**
Both $\alpha\circ\beta$ and $\mathrm{id}$ are $B$-linear maps $(M_B)_g \to (M_B)_g$. Apply $B$-UP uniqueness with $N = (M_B)_g$ and $\phi = \iota_B$: the unique factorization satisfies $(-)\circ\iota_B = \iota_B$. Check both sides:
$$(\alpha\circ\beta)\circ\iota_B = \alpha\circ(\beta\circ\iota_B) = \alpha\circ\iota_A = \iota_B, \qquad \mathrm{id}\circ\iota_B = \iota_B.$$
By uniqueness, $\alpha\circ\beta = \mathrm{id}$.

**Step 4. $\beta$ is $A$-linear.**
Fix $a\in A$. The maps $x\mapsto\beta(ax)$ and $x\mapsto a\beta(x)$ are both $B$-linear $(M_B)_g\to (M_{f^\#(g)})_B$. Apply $B$-UP uniqueness with $N = (M_{f^\#(g)})_B$ and $\phi: m\mapsto\iota_A(am)$: the unique factorization satisfies $(-)\circ\iota_B = \phi$. Check both sides:
$$\beta(a\cdot\iota_B(m)) = \beta(\iota_B(am)) = \iota_A(am), \qquad a\cdot\beta(\iota_B(m)) = a\cdot\iota_A(m) = \iota_A(am).$$
By uniqueness, $\beta(ax) = a\beta(x)$ for all $x$.

**Step 5. $\beta\circ\alpha = \mathrm{id}_{M_{f^\#(g)}}$.**
Both $\beta\circ\alpha$ and $\mathrm{id}$ are $A$-linear maps $M_{f^\#(g)}\to (M_{f^\#(g)})_B$ (the former by Steps 1 and 4). Apply $A$-UP uniqueness with $P = M_{f^\#(g)}$ and $\phi = \iota_A$: the unique factorization satisfies $(-)\circ\iota_A = \iota_A$. Check both sides:
$$(\beta\circ\alpha)\circ\iota_A = \beta\circ(\alpha\circ\iota_A) = \beta\circ\iota_B = \iota_A, \qquad \mathrm{id}\circ\iota_A = \iota_A.$$
By uniqueness, $\beta\circ\alpha = \mathrm{id}$. $\square$

**In words:** The pushforward is literally just restriction of scalars — forget the full $A$-module structure on $M$, keep only the $B$-module structure inherited via $f^\#: B \to A$.

---

## The fiber of $f_*\mathcal{F}$

Using your existing knowledge: the fiber of a $B$-module $N$ at a point $\mathfrak{p} \in \operatorname{Spec}(B)$ is $N \otimes_B \kappa(\mathfrak{p})$, where $\kappa(\mathfrak{p}) = \operatorname{Frac}(B/\mathfrak{p})$.

So the fiber of $f_*\widetilde{M}$ at $\mathfrak{p}$ is
$$\left(f_*\widetilde{M}\right)\big|_{\mathfrak{p}} = M_B \otimes_B \kappa(\mathfrak{p}) = M \otimes_A \left(A \otimes_B \kappa(\mathfrak{p})\right) = M \otimes_A \mathcal{O}_{X_\mathfrak{p}},$$
where $X_\mathfrak{p} = \operatorname{Spec}(A \otimes_B \kappa(\mathfrak{p}))$ is the scheme-theoretic fiber of $f$ over $\mathfrak{p}$.

When $M = \mathcal{O}_X$ (the structure sheaf), this gives $A \otimes_B \kappa(\mathfrak{p})$ — the ring of functions on the fiber, as expected.   ✓ 

When $M$ is a line bundle $\mathcal{L}$ on a projective family $f: X \to Y$ (so each fiber $X_\mathfrak{p}$ is a compact variety), the fiber of $f_*\mathcal{L}$ is $H^0(X_\mathfrak{p}, \mathcal{L}|_{X_\mathfrak{p}})$ — the global sections of $\mathcal{L}$ on the fiber.  ✓
This is a finite-dimensional $\kappa(\mathfrak{p})$-vector space.  ✓
When its dimension is constant across all fibers, $f_*\mathcal{L}$ is a locally free sheaf (= vector bundle) on $Y$, of rank equal to that dimension.  ✓

*Note:* The equality $\left(f_*\mathcal{L}\right)|_\mathfrak{p} = H^0(X_\mathfrak{p}, \mathcal{L}|_{X_\mathfrak{p}})$ requires a base change theorem (Grauert's theorem in the complex setting; cohomology and base change in the algebraic setting). It holds when $H^1$ of the fiber vanishes, or more generally when the higher direct images vanish. ?

---

## Example: $\mathbb{P}^1$-bundle over $\mathbb{A}^1$

$B = k[t]$, $X = \mathbb{P}^1_B = \operatorname{Proj}(B[s_0, s_1])$, $f: X \to \operatorname{Spec}(B)$, $\mathcal{L} = \mathcal{O}(d)$ for $d \geq 0$.

**Global sections:**
$$\Gamma(X, \mathcal{O}(d)) = \bigoplus_{j=0}^d B \cdot s_0^j s_1^{d-j} \cong B^{d+1}$$
*   **Family Interpretation:** On a single $\mathbb{P}^1$, global sections of $\mathcal{O}(d)$ are homogeneous polynomials of degree $d$ with coefficients in $k$. In a family over $B=k[t]$, the coefficients are no longer just numbers ($k$), but functions of $t$ (elements of $B$).
as a $B$-module (the degree-$d$ homogeneous polynomials in $s_0, s_1$ with coefficients in $B$).  ✓
So $f_*\mathcal{O}(d) = \mathcal{O}_Y^{d+1}$, the free rank-$(d+1)$ sheaf on $Y$. 
*   **Geometric Meaning:** Since the pushforward is a free $B$-module of rank $d+1$, the direct image sheaf is geometrically the **trivial vector bundle** $\mathcal{O}_Y^{\oplus (d+1)}$.

**Fiber at $t = t_0$:**
$$B^{d+1} \otimes_{k[t]} \frac{k[t]}{(t-t_0)} = k^{d+1} = H^0(\mathbb{P}^1_k, \mathcal{O}(d)).$$

The fiber is $(d+1)$-dimensional, consistent with $h^0(\mathbb{P}^1, \mathcal{O}(d)) = d+1$.
*   **Analytic Link (Berndtsson):** While algebraically this produces a trivial flat bundle of vector spaces, in the complex analytic setting, equipping $\mathcal{O}(d)$ with a metric $e^{-\phi}$ gives this space an $L^2$ inner product. This $L^2$ metric on the trivial bundle varies with $t$ and possesses Nakano positive curvature, which is the core subject of your RWOT computations.

---

(not read below)
## What the direct image retains and loses

**Retained:** For each $y \in Y$, the vector space $H^0(X_y, \mathcal{L}|_{X_y})$, and its variation as a $\mathcal{O}_Y$-module (i.e., the flat structure over $Y$).

**Lost:** Everything in higher cohomology $H^i$ for $i > 0$; all internal geometry of $X_y$ beyond its global sections of $\mathcal{L}$; the multiplicative structure (if $\mathcal{L} \neq \mathcal{O}_X$, then $f_*\mathcal{L}$ is just a module, not an algebra).

**Recovered in the complex analytic setting:** The $L^2$ metric
$$\|u\|^2_y = \int_{X_y} |u|^2 e^{-\phi_y}\,\omega_y^n, \qquad u \in H^0(X_y, K_{X_y} \otimes \mathcal{L}|_{X_y}),$$
equips the algebraically trivial vector bundle $E = f_*(K_{X/Y} \otimes \mathcal{L})$ with a Hermitian metric that varies with $y$, and has curvature. Berndtsson's theorem (B2, Annals 2009) says this curvature is Nakano $\geq 0$ when $\mathcal{L}$ is semipositive. This curvature is invisible to the pure algebra — it lives entirely in the metric.

---

## Summary table

| Object | Algebra | Geometry |
|---|---|---|
| $f_*\widetilde{M}$ | $B$-module $M$ via restriction of scalars | Sheaf on $Y$: sections over $U$ = sections of $\mathcal{F}$ over $f^{-1}(U)$ |
| Fiber at $\mathfrak{p}$ | $M \otimes_B \kappa(\mathfrak{p})$ | $H^0(X_\mathfrak{p}, \mathcal{L}|_{X_\mathfrak{p}})$ (under base change) |
| Rank | $\dim_{\kappa(\mathfrak{p})} H^0(X_\mathfrak{p}, \mathcal{L})$ | Locally constant $\Rightarrow$ vector bundle |
| Not visible | Metric, curvature, higher $H^i$ | Berndtsson positivity lives here |
 $\Rightarrow$ vector bundle |
| Not visible | Metric, curvature, higher $H^i$ | Berndtsson positivity lives here |
