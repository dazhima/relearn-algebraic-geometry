# Lecture 04 — Two Odd Ends from Ideal Theory

*MATH 464, Rice University, Spring 2020 · January 22, 2020*

---

## 1. Two Odd Ends from Ideal Theory

We start with two odd ends from ideal theory. Please read Atiyah–Macdonald, Chapter 1, and in particular Proposition 1.11 and the notion of quotient ideals.

### 1.1. The Chinese Remainder Theorem

**Theorem 1.1** *(Chinese Remainder Theorem).* Let $\mathfrak{a}_1, \dots, \mathfrak{a}_n$ be pairwise coprime ideals of a ring $A$. The map

$$\phi : A \to A/\mathfrak{a}_1 \times \cdots \times A/\mathfrak{a}_n$$

is surjective, with kernel $\mathfrak{a}_1 \cdots \mathfrak{a}_n = \mathfrak{a}_1 \cap \cdots \cap \mathfrak{a}_n$.

*Proof.* We'll show elements of the form $(1, 0, \dots, 0)$ (with $1$ in position $i$, $0$ elsewhere) are in the image of $\phi$; surjectivity follows. Since $\mathfrak{a}_1$ is coprime to each $\mathfrak{a}_j$ ($j \neq 1$), for each $j > 1$ there exist $a_j \in \mathfrak{a}_j$ and $b_j \in \mathfrak{a}_1$ with $a_j + b_j = 1$. Set $x = \prod_{j > 1} a_j$. Then:

- $x \equiv 1 \pmod{\mathfrak{a}_1}$ (since each $a_j \equiv 1 \pmod{\mathfrak{a}_1}$),
- $x \equiv 0 \pmod{\mathfrak{a}_i}$ for $i > 1$ (since $a_i \in \mathfrak{a}_i$ divides the product).

Similarly construct $x_i$ for each $i$; any element of the product is achieved by $\sum_i c_i x_i$. The kernel is $\bigcap_i \mathfrak{a}_i = \prod_i \mathfrak{a}_i$ (using pairwise coprimality from Lemma 2.2 of Lecture 03). $\square$

### 1.2. Extension and Contraction of Ideals

Let $f : A \to B$ be a ring homomorphism. The image $f(\mathfrak{a})$ of an ideal $\mathfrak{a} \subseteq A$ is generally not an ideal, but it generates one: the *extension* of $\mathfrak{a}$ is

$$\mathfrak{a}^e := \left\{\,\sum_{\text{finite}} f(a_i) b_i : a_i \in \mathfrak{a},\; b_i \in B\right\}.$$

The *contraction* of an ideal $\mathfrak{b} \subseteq B$ is $\mathfrak{b}^c := f^{-1}(\mathfrak{b})$, which is always an ideal of $A$.

Good news: if $\mathfrak{b}$ is a prime ideal of $B$, then $\mathfrak{b}^c$ is a prime ideal of $A$ (since $A/\mathfrak{b}^c$ injects into $B/\mathfrak{b}$, an integral domain). Bad news: a prime ideal need not have a prime extension.

---

## 2. Modules

We move on to Chapter 2 of Atiyah–Macdonald.

Let $A$ be a ring. An $A$-*module* $M$ is an abelian group together with a scalar multiplication

$$A \times M \to M, \quad (a, m) \mapsto am$$

satisfying: $a(m + n) = am + an$, $(a+b)m = am + bm$, $(ab)m = a(bm)$, $1 \cdot m = m$.

**Example 2.1.** If $A = k$ is a field, then $A$-modules are $k$-vector spaces.

**Example 2.2.** If $A = k[t]$, an $A$-module is a $k$-vector space $M$ together with a chosen linear map $t : M \to M$ (the action of $t$).

**Example 2.3.** If $A = k[t]/(t^n)$, an $A$-module is a $k$-vector space on which $t^n$ acts as zero.

**Example 2.4.** If $f : A \to B$ is a ring homomorphism, then $B$ becomes an $A$-module by $a \cdot b := f(a)b$.

**Example 2.5.** $\operatorname{End}(M)$, the ring of $A$-module endomorphisms of $M$ (with composition), receives a ring map $A \to \operatorname{End}(M)$, $a \mapsto (m \mapsto am)$, making $\operatorname{End}(M)$ an $A$-algebra. For example, if $A = \mathbb{R}$ and $M = \mathbb{R}^n$ then $\operatorname{End}(M) = \operatorname{Mat}_n(\mathbb{R})$, and the map sends $a \in \mathbb{R}$ to the diagonal matrix $aI_n$.

**Example 2.6.** The set of $A$-module homomorphisms $\operatorname{Hom}_A(M, N)$ is itself an $A$-module, with pointwise addition and scalar multiplication $(a \cdot \phi)(m) := a\phi(m) = \phi(am)$.

I will assume that you are familiar with the notions of submodules and quotient modules.
