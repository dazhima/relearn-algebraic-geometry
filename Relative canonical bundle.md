# Relative Canonical Bundle $K_{X/Y}$

## Setup

Let $f: X \to Y$ be a smooth holomorphic submersion between complex manifolds. Let $\dim X = n + m$ and $\dim Y = m$, so the fibers $X_y = f^{-1}(y)$ are complex manifolds of dimension $n$.

---

## The Canonical Bundle of a Single Manifold

Before defining the relative version, recall: the **canonical bundle** of a complex manifold $Z$ of dimension $k$ is
$$K_Z = \det(\Omega^1_Z) = \Omega^k_Z,$$
the top exterior power of the cotangent bundle. A section of $K_Z$ over an open set $U$ is a holomorphic $k$-form $\omega = g(z)\, dz_1 \wedge \cdots \wedge dz_k$.

The canonical bundle encodes the "top-dimensional holomorphic measure" on $Z$.

---

## The Relative Cotangent Sequence

For $f: X \to Y$ a submersion, there is an exact sequence of holomorphic vector bundles on $X$:
$$0 \to f^*\Omega^1_Y \xrightarrow{f^*} \Omega^1_X \xrightarrow{} \Omega^1_{X/Y} \to 0.$$

Here:
- $\Omega^1_X$ = the full cotangent bundle of $X$ (all directions).
- $f^*\Omega^1_Y$ = the pullback of $Y$'s cotangent bundle to $X$ (the "horizontal" / base directions, seen in $X$).
- $\Omega^1_{X/Y}$ = the **relative cotangent bundle** = the quotient = the cotangent directions *along the fibers*.

On each fiber $X_y$, the restriction $\Omega^1_{X/Y}|_{X_y} = \Omega^1_{X_y}$ — just the cotangent bundle of the fiber.

---

## Definition of $K_{X/Y}$

The **relative canonical bundle** is
$$K_{X/Y} = \det(\Omega^1_{X/Y}) = \Omega^n_{X/Y},$$
the top exterior power of the relative cotangent bundle. It is a holomorphic line bundle on $X$.

**Equivalent formula.** Taking determinants (top exterior powers) of the relative cotangent sequence gives
$$\det(\Omega^1_X) = \det(f^*\Omega^1_Y) \otimes \det(\Omega^1_{X/Y}),$$
i.e., $K_X = f^* K_Y \otimes K_{X/Y}$, so
$$K_{X/Y} = K_X \otimes f^*K_Y^{-1}.$$

---

## The Key Property: Restriction to Fibers

$$K_{X/Y}\big|_{X_y} \;=\; K_{X_y}.$$

That is, the relative canonical bundle restricted to any fiber is the canonical bundle of that fiber. This is because $\Omega^1_{X/Y}|_{X_y} = \Omega^1_{X_y}$ and taking top exterior powers commutes with restriction.

---

## Why It Appears in the Direct Image Bundle

In B2 (Berndtsson), the direct image bundle has fibers
$$E_y = H^0(X_y,\, K_{X/Y}|_{X_y} \otimes L|_{X_y}) = H^0(X_y,\, K_{X_y} \otimes L|_{X_y}).$$

The reason $K_{X/Y}$ (not $K_X$) appears is the $L^2$ pairing. On each fiber, the natural $L^2$ norm on sections $u \in H^0(X_y, K_{X_y} \otimes L)$ is
$$\|u\|^2_y = \int_{X_y} |u|^2 e^{-\phi},$$
where $|u|^2$ makes sense pointwise because $u$ is a section of $K_{X_y} \otimes L$ and $K_{X_y}$ provides the volume form needed to integrate. Using $K_X$ instead of $K_{X_y} = K_{X/Y}|_{X_y}$ would mix in the $Y$-directions and the norm would depend on a choice of volume form on $Y$, making it non-intrinsic.

---

## Example: Trivial Family

Let $X = Y \times Z$ and $f = \text{pr}_1: X \to Y$. Each fiber is $X_y = \{y\} \times Z \cong Z$.

- $\Omega^1_X = \text{pr}_1^* \Omega^1_Y \oplus \text{pr}_2^* \Omega^1_Z$ (direct sum, since the product is trivial).
- $\Omega^1_{X/Y} = \text{pr}_2^* \Omega^1_Z$ (just the $Z$-directions).
- $K_{X/Y} = \text{pr}_2^* K_Z$.
- Restriction to fiber $X_y \cong Z$: $K_{X/Y}|_{X_y} = K_Z$. ✓

---

## What to Understand

- [ ] The cotangent bundle $\Omega^1_Z$ and canonical bundle $K_Z = \det \Omega^1_Z$. Know what a section looks like locally.
- [ ] The relative cotangent sequence $0 \to f^*\Omega^1_Y \to \Omega^1_X \to \Omega^1_{X/Y} \to 0$ and why it is exact for a submersion.
- [ ] Why $\det$ of an exact sequence $0 \to A \to B \to C \to 0$ gives $\det B = \det A \otimes \det C$. (This is the multiplicativity of determinant in short exact sequences.)
- [ ] The restriction $K_{X/Y}|_{X_y} = K_{X_y}$.
- [ ] Why sections of $K_{X_y} \otimes L$ can be integrated over $X_y$ without extra choices.
