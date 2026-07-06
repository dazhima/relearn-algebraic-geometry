# Lecture 20 — More local properties

*MATH 464, Rice University, Spring 2020 · March 2, 2020*

---

## 1. More local properties
Recall the following:
A property P of an A-module M is said to be a local property if
$$
M satisfies P \LongleftrightarrowMp satisfies P for all p \inSpec(A).
$$
Likewise for maps of modules: a P is a local property of a module map f : M \toN if
$$
f : M \toN satisfies P \Longleftrightarrowfp : Mp \toNp satisfies P for all p \inSpec(A).
$$
We saw last time that being zero is a local propery.
**Proposition 1.1** *(Being injective/surjective is a local property).* Let f : M \toN be a
homomorphism of A-modules. The following are equivalent:
$$
(1) f : M \toN is injective/surjective
$$
(2) fp : Mp \toNp is injective/surjective for every prime ideal p \subseteqA.
(3) fm : Mm \toNm is injective/surjective for every maximal ideal m \subseteqA.
*Proof.* Since localization is an exact functor, we have (1) =$\Rightarrow$(2). The implication (2) =$\Rightarrow$
(3) is trivial (maximal ideals are prime). For (3)
$$
\Rightarrow
$$
(1) in the case of injectivity, let
M ′ = ker f, so that 0 \toM ′ \toM \toN is an exact sequence of modules. Localizing we see
$$
that 0 \toM ′
m \toMm \toNm is exact for every maximal ideal m \subseteqA. But M ′
$$
m = 0 for all
these ideals by hypothesis. Since being zero is a local property, it follows that M ′ = 0. For
surjectivity, reverse all arrows, replacing kernels with cokernels.
$\square$
**Proposition 1.2** *(Being flat is a local property).* Let M be an A-module. The following are
equivalent:
(1) M is a flat A-module.
(2) Mp is a flat Ap-module for every prime ideal p \subseteqA.
(3) Mm is a flat Am-module for every maximal ideal m \subseteqA.
*Proof.* We have Mp = M $\otimes$A Ap, so (1) =$\Rightarrow$(2) follows from the general claim that if M is
a flat A-module then MB = M $\otimes$A B is a flat B-module, which we have mentioned before.
The implication (2) =$\Rightarrow$(3) holds because maximal ideals are prime. For (3) =$\Rightarrow$(1), let

$$
f : N \toP be an injective map of A modules. Then
$$
Nm \toPm is injective for every maximal ideal m
$$
\RightarrowNm \otimesAm Mm \toPm \otimesAm Mm is injective by hypothesis
$$
=$\Rightarrow$(N $\otimes$A M)m \to(P $\otimes$A M)m is injective (tensor products and localization play nice)
=$\Rightarrow$N $\otimes$A M \toP $\otimes$A M is injective since being injective is a local property
And hence M is a flat A-module.
$\square$
---
## 2. Ideal theory of S−1A
$$
Let f : A \toS-1A be the natural map. If b \subseteqA is an ideal, then the extension be in S-1A
$$
is just S-1b because an element x in be has the form P ai/si with ai \inb, and the fraction
can be brought under a common denominator, so that x \inS-1b.
**Proposition 2.1**. The map of sets
$$
φ: {ideals of S-1A} \to{ideals of A}
a 7\tof -1(a) = ac
$$
is injective. It preserves inclusions and intersections, and it takes prime ideals to prime
ideals. In particular, φ induces and injective map $\operatorname{Spec}(S-1A)$ \toSpec A.
An ideal b \subseteqA is of the form ac if and only if bec = b. This is the case if and only if no
element s \inS is a zerodivisor in A/b (meaning that if a \inA and as \inb, then a \inb). In
particular, φ gives a correspondence
{prime ideals of S-1A} ↔{prime ideals of A that don’t meet S}.
*Proof.* Define the map of sets
$$
ψ: {ideals of A} \to{ideals of S-1A}
$$
b \mapstobe
We claim that ψ is a left inverse of φ, i.e., ψ ◦φ = id, which is enough to establish injectivity
of φ. We always have ace \subseteqa. To see the reverse inclusion, note that if a/s \ina then
$$
a \inf -1(a), so a/1 \inace, and we conclude that a/s \inace.
$$
The fact that φ preserves
inclusions and intersections is a fact from set theory that you hopefully learned long ago.
The statement about prime ideals you’ve shown in the homework in a more general context.
Suppose that b = ac. Then be = ace = a. Applying φ to this equality (i.e., contracting)
we obtain bec = b. Conversely, suppose that bec = b, and let a = be. Then ac = bec = b.
The claim on zerodivisors is an easy exercise, using the parenthetical comment.
As to the prime-ideal correspondence: we know that prime ideals of S-1A correspond to
prime ideals of A via φ, so we just need to ask, which prime ideals of A are in the image of φ?
Note that if p is a prime ideal of A, then A/p is a domain. Note that S-1A/S-1p = S-1(A/p),
and the latter is either the zero ring, or it is contained in the field of fractions of A/p and is

thus a domain. If the latter case occurs, we know that S-1p is a prime ideal of S-1A. The
former case can only happen if S ∩p \neq $\emptyset$. Lastly, we saw above that for a \subsetS-1A, ace = a,
and you should check that for p \subsetA a prime ideal not meeting S, pec = p.
$\square$
**Remark 2.2**. A similar result holds for submodules of an arbitrary modules. Exercise: for-
mulate the result and prove it!
---
## 3. Chain conditions
In this lecture, we closely follow Atiyah & MacDonald, Chapter 6. Most of this material
is also in Eisenbud’s book, §2.4.
So far we have dealt, for the most part, with arbitrary modules over arbitrary commutative
rings with unit. Every now and then, we’ve made hypotheses such as “suppose that M is
finitely generated” or “finitely presented” or is “free of finite rank.” These hypotheses were
usually necessary: without them the statements we made were just false. In some cases, we
provided examples to see this.
In order to develop a richer theory, it’s time to restrict our attention to modules that
satisfy some kind of finiteness conditions. Chain conditions fulfill this need.
Let Σ be a set partially ordered by a relation ≤(i.e., ≤is reflexive, transitive, and x ≤y
$$
together with y \leqx imply x = y).
$$
**Proposition 3.1**. TFAE:
(1) Every increasing sequence x1 ≤x2 ≤· · · stabilizes (i.e., there is an N such that
$$
xn = xn+1 for all n \geqN).
$$
(2) Every non-empty subset of Σ has a maximal element.
*Proof.* Exercise.
$\square$
For example, we could take Σ to be the set of submodules of a fixed A-module M, partially
ordered by inclusion (i.e. ≤means \subseteq). Condition (1) above is the called the ascending chain
condition (a.c.c.). A module M satisfying this condition on its set of submodules is called
Noetherian. If instead, we take ≤to be \supseteqthen we get the descending chain condition (d.c.c),
and a module M satisfying this condition on its set of submodules is called Artinian.
**Remark 3.2**. Notice that by the proposition, the descending chain condition is equivalent
to every non-empty subset of Σ having a minimal element, which is what it means to be
well-founded.
