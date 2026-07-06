# Lecture 23 — Wrapping up composition series

*MATH 464, Rice University, Spring 2020 · March 23, 2020*

---

## 1. Wrapping up composition series
Recall that we’re trying to prove the following theorem:
**Theorem 1.1**. Let M be a module of finite length, and let (Mi) denote a composition series
of M. Let p be a prime ideal of A. Then the sum of the localization maps M \toMp gives
an isomorphism of A-modules
α: M
$$
∼-\to
$$
M
p
Mp
where p runs over the maximal ideals of A such that Mi-1/Mi \simeq A/p for some i. In addition,
the number of Mi-1/Mi isomorphic to A/p is equal to the length of Mp as an Ap-module,
and is thus independent of the composition series chosen.
We’ll use this lemma along the way:
**Lemma 1.2**. Let M \neq 0 be a simple A-module. Let p := Ann(M) \subseteqA be the annihilator
ideal of M. Then M ≃A/p as A-modules, and p is maximal. In addition, if m is a maximal
ideal of A, then
$$
Mm \simeq(A/p)m =
$$
(
M
if m = p
otherwise.
*Proof.* Let x \inM be a nonzero element. We must have Ax = M as A-modules; otherwise
Ax ⊊M, which contradicts the simplicity of M. Define the map of A-modules A \toM
determined by the assignment 1 \tox. This map is surjective, and simplicity of M implies
that the kernel is p. Hence M ≃A/p. Finally, if p is not maximal, then A/p has a nonzero
proper maximal ideal, which contradicts the simplicity of M.
For the last claim, if m = p, then (A/m)m = A/m because A/m is already a field (everything
you invert in the localization was already invertible!). If m \neq p then by maximality of p we
$$
have p ⊈m, so pm = Am and (A/p)m = Am/pm = 0.
$$
$\square$
Proof of Theorem 1.1. Being an isomorphism is a local property, so it’s enough to prove that
the given map is an isomorphism after localizing at any maximal ideal m of A. Let
$$
M = M0 ⊃M1 ⊃\cdot \cdot \cdot ⊃Mn = 0
$$

be a composition series of M. We localize a composition series of M at m:
$$
Mm = (M0)m ⊃(M1)m ⊃\cdot \cdot \cdot ⊃(Mn)m = 0.
$$
The modules Mi-1/Mi are simple, so Lemma 1.2 shows that (Mi-1/Mi)m = Mi-1/Mi if
$$
m = \operatorname{Ann}(Mi-1/Mi) and (Mi-1/Mi)m = 0 otherwise. Hence Mm has a composition series
$$
corresponding to the one for M by keeping only those (Mi-1)m for which Mi-1/Mi \simeq A/m.
In particular, if none of the modules Mi-1/Mi is isomorphic to A/m, then Mm = 0, and if
$$
m, m′ are distinct maximal ideals, then (Mm)m′ = 0.
Now consider the map α: M \toL Mp of the proposition, and localize at any maximal
$$
ideal m of A:
$$
αm : Mm \to
$$
M
p
(Mp)m,
By our work above, αm is either the zero endomorphism of the zero A-module (this happens
when m is not the annihilator of any of the quotients Mi-1/Mi), or αm = idMm. Hence, α is
an isomorphism. We have shown the other claims in the course of the proof.
$\square$
**Proposition 1.3**. When M = V is a vector space over a field A = k, TFAE:
(1) finite dimension
(2) finite length
(3) a.c.c.
(4) d.c.c.
*Proof.* Exercise.
$\square$
We saw in the homework that the dimension of a k-vector space is an additive function.
The function M \mapstoℓ(M) is also additive in the class of A-modules of finite length. The
proof is an easy exercise, but I thought it was worth mentioning this fact.
---
## 2. Primary Decomposition
Let A be a commutative ring. The goal of primary decomposition is to write an ideal
a \subseteqA as an intersection of finitely many ideals
a =
n\
i=1
qi,
where the qi are ideals that “behave like powers of prime ideals.” In particular, the radicals
r(qi) will all be prime ideals. These decompositions are important because
• they generalize unique factorization of integers into prime powers, and
• they give a way of decomposing algebraic varieties into irreducible components. In
fact, a primary decomposition of the defining ideal I of an aﬃne variety (think
Spec k[x1, . . . , xn]/I) encodes a lot more information than just the irreducible com-
ponents.

Unfortunately, primary decompositions don’t always exist (as you’ll see in the homework;
there are many natural rings you might consider where decompositions just aren’t there).
However, if A is Noetherian, a decomposition will always be available! These decomposi-
tions, when they exist, satisfy some weak uniqueness properties, which we will explore here.
We will follow the treatment in Chapter 4 of Atiyah-MacDonald.
We begin with the definition of a primary ideal; this is a notion that’s meant to mimic
“prime powers” in the integers.
**Definition 2.1**. An ideal q \subseteqA is primary if q \neq A and if
$$
xy \inq \Rightarroweither x \inq or yn \inq for some n > 0.
$$
Equivalently, A/q \neq 0 and every zero-divisor of A/q is nilpotent.
Note that prime ideals are primary. Also, if φ: A \toB is a ring homomorphism, then
φ∗: Spec B \toSpec A takes primary ideals to primary ideals.
**Lemma 2.2**. If q \subseteqA is primary, then r(q) is the smallest prime ideal containing q.
*Proof.* First we show that r(q) is prime. Suppose that xy \inr(q), so that (xy)m \inq for some
m > 0. Since q is primary, it follows that either xm \inq or ymn \inq for some n > 0. Thus,
either x \inr(q) or y \inr(q). For the remaining claim, note that r(q) = ∩q\subseteqpp. Since q \subseteqr(q),
the prime ideal r(q) appears in this intersection. Clearly, no smaller prime ideal containing
q can also appear; otherwise you would not get an equality of ideals.
$\square$
**Definition 2.3**. If q \subseteqA is a primary ideal, and if p := r(q), then we say q is a p-primary.
**Example 2.4**. The primary ideals of Z are (0) and (pn) for some prime number p. Indeed,
these are the only ideals whose radical is prime, and they are clearly primary.
**Example 2.5**. Not every primary ideal is a power of its radical. Let A = k[x, y] and let
q = (x, y2). Then A/q \simeq k[y]/y2 \neq 0 and the zero divisors of this ring are polynomials
divisible by y, so they are nilpotent.
Hence q is a primary ideal.
One can show that
r(q) = (x, y) =: p. Note that p2 \subsetq \subsetp, where the inclusions are strict.
**Example 2.6**. Prime powers of ideals need not be primary (so for example, if r(a) = p is
prime, it does not follow that a is primary). For example, let A = k[x, y, z]/(xy -z2) and
let p = (¯x, ¯z) be an ideal of A. Note that A/p \simeq k[y] so p is a prime ideal. We claim that p2
is not primary. To see this, note that ¯x¯y = ¯z2 \inp2. However, ¯x /\inp2 and ¯y /\inr(p2) = p.
Despite the last example, we do have the following lemma, whose proof we leave as an
exercise.
**Lemma 2.7**. Let q \subseteqA be an ideal. If r(q) is maximal, then q is primary.
Next class, we’ll define a primary decomposition, discuss when they exist, and look at
what the tell us geometrically.
