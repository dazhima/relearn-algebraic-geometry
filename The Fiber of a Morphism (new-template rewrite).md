---
id: fiber-of-morphism
type: module
title: The fiber of a morphism and the tensor product
status: understood
parent: ../CLAUDE.md
depends_on:
  - residue-field
  - fiber-product
used_by:
  - deformation-to-normal-cone
---

# The fiber of a morphism and the tensor product

## Idea
The "right" fiber of $f:X\to Y$ over a point $y$ is **not** the naive set-theoretic preimage — that's a topological space with no scheme structure. It is the fiber product $X_y = X\times_Y \operatorname{Spec}\kappa(y)$. Morally: *incarnate the point $y$ as the tiny scheme $\operatorname{Spec}\kappa(y)$ and pull $X$ back over it.* Algebraically that pullback is "cut down to $y$" in two moves — **quotient** (restrict to the closure of $y$) then **localize** (zoom to $y$'s generic point) — and the two moves together pin the primes $\mathfrak q$ to exactly $\varphi^{-1}(\mathfrak q)=\mathfrak p$.

## Setup
$f:X\to Y$, a point $y\in Y$. Affine model: $X=\operatorname{Spec}A$, $Y=\operatorname{Spec}B$, ring map $\varphi:B\to A$, and $y\leftrightarrow$ prime $\mathfrak p\subset B$. Goal: give $f^{-1}(y)$ a scheme structure.

## Content

**C1 (naive fiber — set only).** Set-theoretically $f^{-1}(y)=\{\mathfrak q\in\operatorname{Spec}A : \varphi^{-1}(\mathfrak q)=\mathfrak p\}$.
   *Why:* $f(x)=y$ unwinds to $\varphi^{-1}(\mathfrak q)=\mathfrak p$. This is a topological subspace of $\operatorname{Spec}A$, but is not visibly $\operatorname{Spec}$ of any ring — **no scheme structure yet**.

**D1 (residue field & the point as a scheme).** $\kappa(y):=\mathcal O_{Y,y}/\mathfrak m_{Y,y}$; affinely $\kappa(\mathfrak p)=\operatorname{Frac}(B/\mathfrak p)$, via $B\xrightarrow{\text{quotient}}B/\mathfrak p\xrightarrow{\text{localize}}\operatorname{Frac}(B/\mathfrak p)$. This gives a morphism $i_y:\operatorname{Spec}\kappa(y)\to Y$ with image $\{y\}$ — the scheme-theoretic incarnation of $y$.
   *Picture:* to **locate** $y$, first cut to the closed subscheme $\operatorname{Spec}(B/\mathfrak p)$ where $y$ lives, then localize to land exactly on it.

**C2 (the right definition).** The scheme-theoretic fiber is $X_y:=X\times_Y\operatorname{Spec}\kappa(y)$; affinely $X_y=\operatorname{Spec}\!\big(A\otimes_B\kappa(\mathfrak p)\big)$.
   *Why:* the base change pulls $X$ back to the "point" $\operatorname{Spec}\kappa(y)$; affine fiber product $=$ tensor product. The map $X_y\to X$ is (closed immersion)$\circ$(open immersion) — this is what installs the scheme structure on $f^{-1}(y)$.

**C3 (move 1 — quotient = restrict to $\overline{\{y\}}$).** $A\otimes_B B/\mathfrak p\;\cong\;A/\mathfrak p^e$, where $\mathfrak p^e=\varphi(\mathfrak p)A$ is the extended ideal.
   *Why:* tensor $\mathfrak p\to B\to B/\mathfrak p\to0$ with $-\otimes_B A$ (right-exact); the image of $\mathfrak p\otimes_B A\to A$ is $\mathfrak p^e$. *(Alt: the surjection $a\mapsto a\otimes\bar1$ has kernel $\mathfrak p^e$.)* Geometrically $\operatorname{Spec}(A/\mathfrak p^e)=f^{-1}\overline{\{y\}}$; **primes kept:** $\varphi^{-1}(\mathfrak q)\supseteq\mathfrak p$.

**C4 (move 2 — localize = zoom to the generic point of $\overline{\{y\}}$).** $A\otimes_B\kappa(\mathfrak p)\;\cong\;S^{-1}(A/\mathfrak p^e)$, with $S=\varphi(B\setminus\mathfrak p)$.
   *Why:* extension of scalars to $\operatorname{Frac}(B/\mathfrak p)$ **is** localization at $S$ ($S^{-1}M\cong M\otimes_R S^{-1}R$), applied to $A/\mathfrak p^e\cong A\otimes_B B/\mathfrak p$ from C3. **Primes kept:** $\varphi^{-1}(\mathfrak q)\subseteq\mathfrak p$.

**C5 (main result — the two moves pin the fiber).** C3 forces $\varphi^{-1}(\mathfrak q)\supseteq\mathfrak p$ and C4 forces $\varphi^{-1}(\mathfrak q)\subseteq\mathfrak p$, hence $\varphi^{-1}(\mathfrak q)=\mathfrak p$. So the underlying set of $\operatorname{Spec}(A\otimes_B\kappa(\mathfrak p))$ is in natural bijection with $f^{-1}(y)$ — now carrying the scheme structure the naive definition lacked.

**E1 (example — $\operatorname{Spec}\mathbb Z[x]$ over $\operatorname{Spec}\mathbb Z$, $\varphi:\mathbb Z\hookrightarrow\mathbb Z[x]$).**
   $\mathfrak p=(0)$: $\kappa=\mathbb Q$, $\mathbb Z[x]\otimes_{\mathbb Z}\mathbb Q=\mathbb Q[x]$ — the **generic fiber** (the localization move).
   $\mathfrak p=(p)$: $\kappa=\mathbb F_p$, $\mathbb Z[x]\otimes_{\mathbb Z}\mathbb F_p=\mathbb F_p[x]$ — the **special fiber** (the quotient move).

## Conclusion

> $f^{-1}(y)\cong\operatorname{Spec}\!\big(A\otimes_B\kappa(\mathfrak p)\big)$. The scheme structure the naive set-theoretic fiber lacked comes from this ring, built by factoring $B\to B/\mathfrak p\to\kappa(\mathfrak p)$ into **quotient then localize** — restrict to $\overline{\{y\}}$, then zoom to $y$. The two moves cut primes down to exactly $\varphi^{-1}(\mathfrak q)=\mathfrak p$.

| Move | Algebra | Geometry | Primes kept |
|---|---|---|---|
| Quotient | $A\to A/\mathfrak p^e$ | restrict to $\overline{\{y\}}$ | $\varphi^{-1}(\mathfrak q)\supseteq\mathfrak p$ |
| Localize | $A/\mathfrak p^e\to S^{-1}(A/\mathfrak p^e)$ | zoom to generic point of $\overline{\{y\}}$ | $\varphi^{-1}(\mathfrak q)\subseteq\mathfrak p$ |
| **Combined** | $A\to A\otimes_B\kappa(\mathfrak p)$ | **the fiber $f^{-1}(y)$** | $\varphi^{-1}(\mathfrak q)=\mathfrak p$ |

## Connections
Builds on `residue-field`, `fiber-product`. Sibling: the `Spec ℤ[x]` note (its Prop 1.1 cases 1–2 are exactly C4 and C3). Used in fiber computations for `deformation-to-normal-cone`.
