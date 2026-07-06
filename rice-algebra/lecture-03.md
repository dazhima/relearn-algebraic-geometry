# Lecture 03 — Nilradical and Jacobson Radical (continued)

*MATH 464/564, Rice University, Spring 2020 · January 17, 2020*

---

We continue our development of further ideal theory, following the treatment in Chapter 1 of Atiyah–Macdonald.

## 1. Nilradical and Jacobson Radical (continued)

The nilradical of a ring $A$ has a characterization in terms of prime ideals.

**Theorem 1.1** *(Krull).* We have

$$
N = \bigcap_{\mathfrak{p} \subseteq A \text{ prime}} \mathfrak{p}.
$$

*Proof.* We start with the inclusion $\subseteq$. If $f \in N$, then for some $n > 0$ we have $f^n = 0$, and so for every prime ideal $\mathfrak{p}$, we have $f^n \in \mathfrak{p}$. Since $\mathfrak{p}$ is prime, this means that $f \in \mathfrak{p}$.

Now we do the other inclusion $\supseteq$. We prove the contrapositive:

$$
f \notin N \Longrightarrow f \notin \bigcap_{\mathfrak{p} \subseteq A \text{ prime}} \mathfrak{p}.
$$

So let $f \notin N$. Consider the set

$$
\Sigma := \{\mathfrak{a} \subseteq A \text{ ideal} : n > 0 \Longrightarrow f^n \notin \mathfrak{a}\}.
$$

Note that $\Sigma \neq \emptyset$ because $(0) \in \Sigma$, as $f$ is not nilpotent. Order $\Sigma$ by inclusion, and note that every chain has an upper bound. By Zorn's Lemma, $\Sigma$ has a maximal element $\mathfrak{p}$. We claim that $\mathfrak{p}$ is a prime ideal. Since $f \notin \mathfrak{p}$, taking $n = 1$, it will follow that $f \notin \bigcap_{\mathfrak{p} \subseteq A \text{ prime}} \mathfrak{p}$, as desired.

Suppose that $x, y$ are not in $\mathfrak{p}$. Then the inclusions $\mathfrak{p} \subset \mathfrak{p} + (x)$ and $\mathfrak{p} \subset \mathfrak{p} + (y)$ are proper, and by maximality of $\mathfrak{p}$, we conclude that $\mathfrak{p} + (x) \notin \Sigma$ and $\mathfrak{p} + (y) \notin \Sigma$. Therefore, there exist $n > 0$ and $m > 0$ such that

$$
f^n \in \mathfrak{p} + (x)
\qquad\text{and}\qquad
f^m \in \mathfrak{p} + (y).
$$

But then $f^{n+m} \in \mathfrak{p} + (xy)$, so $\mathfrak{p} + (xy) \notin \Sigma$, which means that $xy \notin \mathfrak{p}$, proving that $\mathfrak{p}$ is a prime ideal.

$\square$

If instead of intersecting all prime ideals of $A$, we intersect only those ideals which are maximal, we obtain a possibly bigger ideal than the nilradical. This is called the *Jacobson radical* of $A$, and is denoted $\mathfrak{R}$:

$$
\mathfrak{R} := \bigcap_{\mathfrak{m} \subseteq A \text{ maximal}} \mathfrak{m}.
$$

**Example 1.2.** Suppose that $X$ is a topological space. Let $A = C(X)$ be the ring of continuous, complex-valued functions on $X$. I claim that $\mathfrak{R}$ contains only the zero function. To see this, for every $x \in X$, consider the ideal

$$
\mathfrak{m}_x := \{f \in C(X) : f(x) = 0\}.
$$

This ideal is maximal. If $f \in \mathfrak{R}$, then $f \in \mathfrak{m}_x$ for every $x \in X$, so $f(x) = 0$ for every $x \in X$. Since $N \subseteq \mathfrak{R}$, the nilradical in this example is also trivial.

**Example 1.3.** The Jacobson radical of a ring can be larger than the nilradical. Let $(A, \mathfrak{m})$ be a local ring which is an integral domain, for instance the $p$-adic numbers. Then $N = (0)$ but $\mathfrak{R} = \mathfrak{m}$.

There is a way to characterize the elements of the Jacobson radical, analogous to the characterization of elements of the nilradical as nilpotent elements.

**Proposition 1.4.** We have $x \in \mathfrak{R}$ if and only if $1 - xy$ is a unit for every $y \in A$.

*Proof.* Suppose that $1 - xy$ is not a unit for some $y \in A$. Then $1 - xy$ is contained in some maximal ideal $\mathfrak{m}$ of $A$. If $x \in \mathfrak{m}$, then $xy \in \mathfrak{m}$, and this would imply that $(1 - xy) + xy \in \mathfrak{m}$, a contradiction. Hence $x \notin \mathfrak{m}$, and so $x \notin \mathfrak{R}$.

For the other inclusion, prove the contrapositive. Suppose that $x \notin \mathfrak{R}$. Then there is a maximal ideal $\mathfrak{m}$ such that $x \notin \mathfrak{m}$. It follows that $\mathfrak{m} + (x) = A$, which means there exists $y \in A$ such that $1 - xy \in \mathfrak{m}$, so $1 - xy$ is not a unit.

$\square$

### 1.1. The Radical of an Ideal

If $\mathfrak{a} \subseteq A$ is an ideal, define the *radical* of $\mathfrak{a}$ to be

$$
\operatorname{rad}(\mathfrak{a})
:=
\{x \in A : x^n \in \mathfrak{a} \text{ for some } n > 0\}.
$$

If $\phi : A \to A/\mathfrak{a}$ is the usual quotient map, then $\operatorname{rad}(\mathfrak{a}) = \phi^{-1}(N_{A/\mathfrak{a}})$, so $\operatorname{rad}(\mathfrak{a})$ is an ideal. Applying Krull's theorem to $A/\mathfrak{a}$ gives the following corollary.

**Corollary 1.5.** Let $\mathfrak{a} \subseteq A$ be an ideal. Then

$$
\operatorname{rad}(\mathfrak{a})
=
\bigcap_{\substack{\mathfrak{p} \text{ prime} \\ \mathfrak{a} \subseteq \mathfrak{p}}}
\mathfrak{p}.
$$

Radicals enjoy a few properties that are easy to prove and are left for you to work out:

1. $\operatorname{rad}(\operatorname{rad}(\mathfrak{a})) = \operatorname{rad}(\mathfrak{a})$.
2. $\operatorname{rad}(\mathfrak{a}\mathfrak{b}) = \operatorname{rad}(\mathfrak{a} \cap \mathfrak{b}) = \operatorname{rad}(\mathfrak{a}) \cap \operatorname{rad}(\mathfrak{b})$.
3. $\operatorname{rad}(\mathfrak{a}) = A \Longleftrightarrow \mathfrak{a} = A$.
4. $\operatorname{rad}(\mathfrak{a} + \mathfrak{b}) = \operatorname{rad}(\operatorname{rad}(\mathfrak{a}) + \operatorname{rad}(\mathfrak{b}))$.
5. If $\mathfrak{p}$ is prime, then $\operatorname{rad}(\mathfrak{p}^n) = \mathfrak{p}$.

---

## 2. The Chinese Remainder Theorem

In elementary number theory you probably came across the Chinese remainder theorem. It says that if $m_1,\dots,m_n$ are pairwise relatively prime integers, and if $a_1,\dots,a_n$ are any integers, then there exists an integer $x$ satisfying

$$
x \equiv a_i \pmod{m_i}
\qquad
(1 \leq i \leq n).
$$

Equivalently, given pairwise relatively prime integers $m_1,\dots,m_n$, the product map of quotient maps

$$
\mathbb{Z}
\to
\mathbb{Z}/m_1\mathbb{Z} \times \cdots \times \mathbb{Z}/m_n\mathbb{Z},
\qquad
x \mapsto (x \bmod m_1,\dots,x \bmod m_n)
$$

is surjective. This formulation generalizes to arbitrary commutative rings with unit.

**Definition 2.1.** Two ideals $\mathfrak{a}$ and $\mathfrak{b}$ of a ring $A$ are *relatively prime* if $\mathfrak{a} + \mathfrak{b} = (1)$.

It is easy to see that if $\mathfrak{a}$ and $\mathfrak{b}$ are any two ideals of a ring $A$, then

$$
(\mathfrak{a} + \mathfrak{b})(\mathfrak{a} \cap \mathfrak{b})
\subseteq
\mathfrak{a}\mathfrak{b}.
$$

On the other hand, $\mathfrak{a}\mathfrak{b} \subseteq \mathfrak{a} \cap \mathfrak{b}$, and so

$$
\mathfrak{a} \cap \mathfrak{b}
=
\mathfrak{a}\mathfrak{b}
\quad\text{provided}\quad
\mathfrak{a} + \mathfrak{b} = (1).
$$

Thus, for relatively prime ideals, $\mathfrak{a} \cap \mathfrak{b} = \mathfrak{a}\mathfrak{b}$. More generally:

**Lemma 2.2.** If $\mathfrak{a}_1,\dots,\mathfrak{a}_n$ are pairwise coprime ideals of a ring $A$, then

$$
\bigcap_i \mathfrak{a}_i
=
\prod_i \mathfrak{a}_i.
$$

*Proof.* Induction on $n$. The case $n = 2$ is the base case done above. See Proposition 1.10(i) of Atiyah–Macdonald for details.

$\square$
