er# Cohomology and Base Change

## Prerequisite: Higher Direct Images $R^i f_*$

Before stating any base change theorem, understand $R^i f_*\mathcal{F}$.

**Definition.** For a morphism $f: X \to Y$ and a sheaf $\mathcal{F}$ on $X$, the sheaf $f_*\mathcal{F}$ is the zeroth derived functor. The higher direct images $R^i f_*\mathcal{F}$ ($i \geq 1$) are the higher derived functors of $f_*$: they are the sheaves on $Y$ associated to the presheaves

$$U \mapsto H^i(f^{-1}(U), \mathcal{F}).$$

Note $R^0 f_* = f_*$, consistent with the direct image already studied.

**Why derived functors?** $f_*$ is left exact but not exact. Given a short exact sequence $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$, one gets a long exact sequence of sheaves on $Y$:

$$0 \to f_*\mathcal{F}' \to f_*\mathcal{F} \to f_*\mathcal{F}'' \to R^1f_*\mathcal{F}' \to R^1f_*\mathcal{F} \to \cdots$$

So $R^i f_*\mathcal{F}$ measure the failure of $f_*$ to preserve exactness.

**To fill in:**
- [ ] Understand derived functors (injective resolutions, the general construction). *Reference: Hartshorne, Appendix to Ch. III, §1; or Weibel, Introduction to Homological Algebra, Ch. 2.*
- [ ] Verify that $R^i f_*\mathcal{F}$ is the sheafification of $U \mapsto H^i(f^{-1}(U), \mathcal{F})$, and see why naive sections need sheafification (they fail gluing in general). *Reference: Hartshorne III.8, Proposition 8.1.*
- [ ] For $f$ proper and $\mathcal{F}$ coherent: $R^i f_*\mathcal{F}$ is coherent on $Y$ (Grauert's coherence theorem, algebraic version). *Reference: Hartshorne III.5, Theorem 5.2 (projective case).*
- [ ] Stalk formula: $(R^i f_*\mathcal{F})_y \cong \varinjlim_{U \ni y} H^i(f^{-1}(U), \mathcal{F})$. In the proper case this stabilizes (Stein factorization / proper base change for étale topology gives a cleaner statement; for now the Čech computation suffices).

---

## The Base Change Question

Once $R^i f_*\mathcal{F}$ is understood, the base change question is:

**How does $R^i f_*\mathcal{F}$ relate to $H^i(X_y, \mathcal{F}|_{X_y})$?**

There is always a natural map (the **base change map**)

$$\phi^i(y) : (R^i f_*\mathcal{F}) \otimes_{\mathcal{O}_Y} \kappa(y) \longrightarrow H^i(X_y, \mathcal{F}|_{X_y}).$$

The left side is the fiber of the sheaf $R^i f_*\mathcal{F}$ at the point $y$; the right side is sheaf cohomology on the fiber $X_y = X \times_Y \operatorname{Spec}\kappa(y)$.

**To fill in:**
- [ ] Construct $\phi^i(y)$ explicitly. It comes from functoriality of cohomology: the pullback $X_y \hookrightarrow X$ and the projection $f^{-1}(U) \supset X_y$ give a map on cohomology. After passing to the direct limit (stalk) and tensoring with $\kappa(y)$, one gets $\phi^i(y)$.

---

## Approach 1: Algebraic Approach

### Step 1 — Flat base change (Theorem 1)

**Theorem.** If $g: Y' \to Y$ is any morphism with base change $f': X' \to Y'$, and if $\mathcal{F}$ is flat over $Y$ (or $g$ is flat), then

$$g^* R^i f_*\mathcal{F} \cong R^i f'_*(g'^*\mathcal{F}).$$

In particular, taking $Y' = \operatorname{Spec}\kappa(y)$: $\phi^i(y)$ is an isomorphism for all $i$ and all $y$ when $\mathcal{F}$ is flat over $Y$.

*Reference: Hartshorne, Proposition III.9.3.*

**To fill in:**
- [ ] Understand why flatness of $\mathcal{F}$ over $Y$ is the key hypothesis (it makes the Künneth formula exact without correction terms). *Reference: Weibel §3.2 (Tor and flatness); Hartshorne III.9.*
- [ ] Work a concrete example: $f: X \to Y$ the trivial family $X = Y \times Z$, $\mathcal{F} = \mathcal{O}_X$; verify flat base change directly.

### Step 2 — Semicontinuity (Theorem 2)

**Theorem.** Assume $f$ proper, $\mathcal{F}$ coherent and flat over $Y$, $Y$ integral. Then $y \mapsto h^i(X_y, \mathcal{F}|_{X_y})$ is upper semicontinuous, and $y \mapsto \chi(X_y, \mathcal{F}|_{X_y})$ is locally constant.

*Reference: Hartshorne, Theorem III.12.8.*

**To fill in:**
- [ ] Understand the proof strategy: reduce to a complex of free $\mathcal{O}_Y$-modules computing cohomology (the "Cartan–Eilenberg complex" / "good truncation"), then rank of cohomology = dimension of a vector space over $\kappa(y)$, which is upper semicontinuous. *Reference: Hartshorne III.12, first half.*

### Step 3 — Grauert / Cohomology and Base Change (Theorem 3)

**Theorem.** Assume $f$ proper, $\mathcal{F}$ coherent and flat over $Y$, $Y$ Noetherian.

(a) If $h^i(X_y, \mathcal{F}|_{X_y})$ is constant in a neighborhood of $y$, then $R^i f_*\mathcal{F}$ is locally free near $y$ and $\phi^i(y)$ is an isomorphism.

(b) $\phi^i(y)$ is surjective iff $R^{i+1}f_*\mathcal{F}$ is locally free near $y$ (and then $\phi^{i+1}(y)$ is also an isomorphism).

**Corollary (the case we use).** If $H^i(X_y, \mathcal{F}|_{X_y}) = 0$ for all $y$, then $R^i f_*\mathcal{F} = 0$. In particular, if $H^1(X_y, \mathcal{L}|_{X_y}) = 0$ for all $y$, then $\phi^0(y)$ is an isomorphism: $(f_*\mathcal{L})|_y \cong H^0(X_y, \mathcal{L}|_{X_y})$ and $f_*\mathcal{L}$ is locally free.

*Reference: Hartshorne, Theorem III.12.11.*

---

## Approach 2: Complex Analytic Approach (Grauert's Theorem)

In the complex analytic setting, $f: X \to Y$ is a proper holomorphic map between complex manifolds (or complex spaces), $\mathcal{F}$ is a coherent analytic sheaf.

**Grauert's theorem:** The direct images $R^i f_*\mathcal{F}$ are coherent analytic sheaves on $Y$.

**Base change in the analytic setting:** The map $\phi^i(y)$ is an isomorphism when $h^i$ is locally constant, exactly as in Theorem 3 above — but now proved by analytic methods (without needing an algebraic flatness hypothesis, since proper + coherent already forces the right behavior).

**What this gives us for the $\mathbb{P}^1$-bundle example:**

Each fiber is $\mathbb{P}^1_{\kappa(y)}$ and $H^1(\mathbb{P}^1, \mathcal{O}(d)) = 0$ for $d \geq -1$ (by Serre duality: $H^1(\mathbb{P}^1, \mathcal{O}(d)) \cong H^0(\mathbb{P}^1, \mathcal{O}(-d-2))^* = 0$). So $\phi^0(y)$ is an isomorphism and $(f_*\mathcal{O}(d))|_y = H^0(\mathbb{P}^1, \mathcal{O}(d))$ for all $y$.

**To fill in:**
- [ ] Understand Grauert's original proof (uses $L^2$ methods / Oka–Cartan theory). *Reference: Grauert, "Ein Theorem der analytischen Garbentheorie," 1960; also Griffiths–Harris §5.4.*
- [ ] Alternative modern reference: Voisin, *Hodge Theory and Complex Algebraic Geometry*, Vol. I, §9.
- [ ] Understand why analytically proper + coherent replaces algebraic flat + coherent: the key is that over $\mathbb{C}$ with the usual topology, local sections of $R^i f_*\mathcal{F}$ are already controlled by $L^2$ estimates.

---

## Connection to the Direct Image Bundle in Our Paper

In the paper, $f: X_\mathbb{C} \to \mathbb{C}$ is the deformation to the normal bundle, and $\mathcal{L}$ is the pullback line bundle $L_\mathbb{C}$. We want:

$$(f_*\mathcal{L})|_s \cong H^0(X_s, L_s)$$

for each $s \in \mathbb{C}$. This is Approach 2: each fiber is a compact complex manifold, $H^1$ vanishes by positivity of $L$, and Grauert's theorem gives the isomorphism. The resulting sheaf $f_*\mathcal{L}$ is the direct image bundle $E$ to which Berndtsson's theorem (B2) applies.
