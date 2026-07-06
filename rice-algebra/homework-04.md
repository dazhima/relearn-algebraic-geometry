# Homework 04

*MATH 464, Rice University, Spring 2020 · Due: Wednesday, February 12th, by 5pm. Each exercise is worth 10 points*

---

Due date: Wednesday, February 12th, by 5pm. Each exercise is worth 10 points.
Math 464 students should turn in complete problems worth a total of at least 50 points (but
should carefully read and understand the statements of all eight problems).
Math 564 students should do ALL the exercises.
Unless otherwise indicated, A is a commutative ring, with unit.
---
## 1. Tensor products; direct limits; flatness
**(1)** Some practice with tensor products:
(a) Describe the topological space Spec F4 $\otimes$F2 F4. In other words, determine the set of
primes of the ring F4 $\otimes$F2 F4 and describe its Zariski topology. [Hint: F4 ≃F2[x]/(x2 +
x + 1).]
(b) Let k be a field. Use the universal property of tensor products to show that
$$
(k[x1, . . . , xn]/a) \otimesk (k[y1, . . . , ym]/b) \simeqk[x1, . . . , xn, y1, . . . , ym]/(ae + be),
$$
where ae and be are the respective extensions of a and b in k[x1, . . . , xn, y1, . . . , ym].
**(2)** Let (Mi, µij) be a directed system over a directed set I with direct limit M, and let N be
an A-module. Then (Mi $\otimes$A N, µij $\otimes$idN) is also a directed system. Let P := lim
$$
-\to(Mi \otimesA N)
$$
be its direct limit. For each i \inI we have a homomorphism µi $\otimes$idN : Mi $\otimes$A N \toM $\otimes$A N.
By the universal mapping property of direct limits, we get an A-module homomorphism
ψ: lim
$$
-\to(Mi \otimesA N) \to
$$
lim
$$
-\toMi
$$

$\otimes$A N.
Show that ψ is an isomorphism.
[Hint: use the universal mapping property of tensor
products to construct a map of A-modules that goes the other way; show that ψ and the
map you just constructed are inverses to each other.]
**(3)** (a) Let Mi (i \inI) be any family of A-modules, and let M be their direct sum. Prove that
M is flat if and only if each Mi is flat.
(b) Prove that A[x] is a flat A-algebra. (Hint: Let Mi be a A-submodule of A[x] generated
by xi; apply the result of part (a)).
(c) Prove that if M and N are flat A-modules, then so is M $\otimes$A N.

**(4)** Let M, N and P be A-modules. Suppose that M is finitely presented and that P is flat
over A. Show that the natural homomorphism
$$
HomA(M, N) \otimesA P \toHomA(M, N \otimesA P)
$$
is an isomorphism. Hint: First do the case when M is finitely generated and free. Then
use the finite presentation hypothesis to reduce to this case, following the template from an
exercise last week.
---
## 2. Affine algebraic geometry: Part II
We continue our study of Spec of a ring. A lot of the following exercises are propositions in
general topology. By the end of this set of exercises you’ll deduce a neat property of Noetherian
rings with (essentially) topological arguments.
**Definition 2.1**. A topological space X is said to be irreducible if X \neq $\emptyset$and if every pair of
nonempty open subsets of X intersect (equivalently, if every nonempty open subset of X is dense).
**(5)** Show that X = $\operatorname{Spec}(A)$ is irreducible if and only if the nilradical of A is a prime ideal.
**(6)** Let X be a topological space.
(a) Show that, if Y is an irreducible subspace of X, then the closure Y of Y in X is
irreducible.
(b) Show that every irreducible subspace of X is contained in a maximal irreducible sub-
space.
(c) Show that the maximal irreducible subspaces of X are closed and they cover X. They
are called the irreducible components of X. What are the irreducible components of a
Hausdorﬀspace?
(d) Show that the irreducible components of X = $\operatorname{Spec}(A)$ are of the form V (p), where p
is a minimal prime ideal of A. In particular, if A is an integral domain, then $\operatorname{Spec}(A)$
is irreducible.
Note that part (d) of this last exercise says that spaces line Spec Z, Spec C[x] (the aﬃne line),
Spec C[x, y] (the aﬃne plane) and Spec C[x, y]/(y2 -x3 -1) (the aﬃne part of the elliptic curve
y2 = x3 + 1) are irreducible. Part (c) shows that all these spaces are seriously not Hausdorﬀ.
**Definition 2.2**. A topological space is said to be Noetherian if the open subsets of X satisfy the
ascending chain condition on open sets, meaning that that for any sequence
$$
X1 \subseteqX2 \subseteq\cdot \cdot \cdot
$$
of open subsets of X, there exists an N such that Xn = Xn+1 for all n ≥N. Equivalently, X
satisfies the descending chain condition for closed sets: for any sequence
Y1 \supseteqY2 \supseteq· · ·
of closed subsets of X, there exists an N such that Yn = Yn+1 for all n ≥N.

**(7)** Show that a Noetherian space X is a finite union of irreducible closed subspaces. Deduce
that the set of irreducible components of X is finite. [Hint: for the first part consider the
set Σ of closed subsets of X that are not finite unions of irreducible closed spaces.]
**(8)** Show that if A is a Noetherian ring, then $\operatorname{Spec}(A)$ is a Noetherian topological space. [Hint:
observe that V (a) \subseteqV (b) =$\Rightarrow$r(b) \subseteqr(a).] Is the converse true? Deduce that the set of
minimal primes in a Noetherian ring is finite.
Now breathe. We just showed that a Noetherian ring has finitely many minimal primes using
the topology of $\operatorname{Spec}(A)$! By the way, that means that for a Noetherian ring A, the nilradical is the
intersection of only finitely many prime ideals! (the minimal primes). So if we could compute the
minimal primes of a Noetherian ring, then we could compute its nilradical! We would then have a
way to determine if a ring has nilpotent elements, or a way to tell if an ideal a is equal to its radical
r(a) (by looking at the nilradical of A/a). In fact, all of this can be done using Gr¨obner bases.
