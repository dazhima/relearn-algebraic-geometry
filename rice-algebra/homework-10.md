# Homework 10

*MATH 464, Rice University, Spring 2020 · Due: Wednesday, April 15th, by 5pm. Each exercise is worth 10 points*

---

Due date: Wednesday, April 15th, by 5pm. Each exercise is worth 10 points.
Math 464 students should turn in complete problems 1 and 4 and two other problems.
Math 564 students should turn in complete problems 1 and 4 and four other problems.
Unless otherwise indicated, A is a commutative ring, with unit.
---
## 1. Towards Dedekind Domains
Dedekind domains constitute a very important class of rings: the ring of integers of a finite
extension of Q (e.g., the Gaussian integers Z[i] \subseteqQ[i]) is a Dedekind domain, as is the stalk OX,x
of the structure sheaf OX at a smooth point x on an algebraic curve X.
**Definition 1.1**. A Dedekind domain is a Noetherian domain where every nonzero prime ideal is
maximal, and where every primary ideal is a prime power.
Warning: The above definition, while correct, is not how Dedekind domains are introduced in
most books: the condition “every primary ideal is a prime power” can be replaced by the equivalent
condition “A is integrally closed”, which we will come to very soon in the course.
**(1)** Let A be a Noetherian domain in which every nonzero prime ideal is maximal. Show that
every nonzero ideal a \subseteqA can be uniquely expressed as a product of primary ideals, whose
radicals are all distinct. Conclude that in a Dedekind Domain, every nonzero ideal has a unique
factorization as a product of prime ideals.
[Hints: Prove that the primary ideals in a minimal primary decomposition of A are pairwise co-
prime. Apply the Chinese Remainder Theorem. For the uniqueness statement, read about the
second uniqueness theorem for primary decompositions, Corollary 4.11 in Atiyah–Macdonald.]
This proposition helps fix the “bug” you (hopefully) ran into in Math 463: that unique factor-
ization into irreducible elements can fail in rings like Z[√-5]:
$$
6 = 2 \cdot 3 = (1 +
$$
√
$$
-5)(1 -
$$
√
-5).
The ring Z[√-5] is the ring of integers in Q(√-5), and is therefore a Dedekind Domain (we will
prove these assertions in due course). However, the ideal (2) \subseteqZ[√-5] is not prime:
Z[
√
$$
-5]/(2) \simeqZ[x]/(x2 + 5, 2) \simeqF2[x]/(x2 + 5) = F2[x]/(x2 + 1) = F2[x]/(x + 1)2,
$$

and this last ring is visibly not a domain. However, Problem 1 tells us that the ideal (2) factorizes
into prime ideals! In fact
**(2)** = (2, 1 +
√
-5)2,
$$
and the ideal p1 := (2, 1 + √-5) is prime in \mathbb{Z}[√-5]! Similarly,
$$
**(3)** = (3, 1 +
√
$$
-5)(3, 1 -
$$
√
-5),
$$
and the ideals p2 := (3, 1 + √-5) and p3 := (3, 1 -√-5) are prime in \mathbb{Z}[√-5]. In fact,
$$
(1 +
√
$$
-5) = p1p3
and
$$
(1 -
√
$$
-5) = p2p3.
$$
The upshot is that
**(6)** = p2
1p2p3
is a factorization of (6) into prime ideals in Z[√-5]. Dedekind introduced ideals in rings in order
to solve the failure of unique factorization into irreducible elements in rings like Z[√-5]. He called
objects like p1 “idealized elements”. Dedekind domains are named in his honor for this discovery.
The following exercises will be needed in our upcoming study of Dedekind domains.
They
begin exploring the local case. You already have all the tools you need to prove them (the “neat
application” after Corollary 1.6 in Lecture 8 should prove quite useful).
**(2)** Let A be a Noetherian ring, and let a \subseteqA be an ideal.
$$
(a) Prove that r(a)n \subseteqa for some n \geq1.
$$
(b) Let m \subseteqA be a maximal ideal. Prove that the following statements are equivalent
(i) a is m-primary;
(ii) r(a) = m;
$$
(iii) mn \subseteqa \subseteqm for some n \geq1.
$$
In the next two problems, we shall assume that A is a local Noetherian domain. We write
m for its unique maximal ideal, and k = A/m for its residue field. We assume that m \neq 0.
**(3)** Show that mn \neq mn+1 for all n.
**(4)** Suppose that every nonzero prime ideal of A is maximal (and hence equal to m). Consider the
following statements
$$
(a) dimk m/m2 = 1.
$$
(b) The ideal m is principal.
(c) Every nonzero ideal of A is of the form mn.
(d) There is an x \inA such that every nonzero ideal of A is of the form (xk) for some k ≥0.
$$
Show that (a) \Longleftrightarrow(b) \Rightarrow(c) \Rightarrow(d).
$$

Hint for (b) =$\Rightarrow$(c): By Problem 2, since m is the only nonzero prime ideal, if a \subsetA is a
proper nonzero ideal of A, then a is m-primary and mn0 \subseteqa \subseteqm for some n0 ≥1. From here,
proceed in one of two ways:
**(1)** Since a \subseteqm and m = (x) for some x \inA, write a \ina as a = y1x for some y1 \inA. If
$$
y1 \inA\m, conclude that a = m. If y1 \inm = (x), write y1 = y2x for some y2 \inA. If y2 \inA\m,
$$
conclude that a = m2. Else, repeat. Why must this process terminate?
**(2)** If a = mn0, then we are done. Otherwise, let n be maximal with respect to the property that
a \subseteqmn, so a ̸\subsetmn+1 (why does this n exist?). Show that dimk mn/mn+1 = 1, and conclude
that the composition a ,\tomn ↠mn/mn+1 must be surjective. Use this to help you prove that
a = mn.
The element x \inA at the end of Problem 4 is called a uniformizer. It can be used to give A the
structure of a discrete valuation ring. This is an integral domain A, together with a map
$$
v: A \toZ
$$
such that
$$
• v(xy) = v(x) + v(y), and
• v(x + y) \geqmin{v(x), v(y)}.
$$
This valuation is usually extended to the field of fractions K of A by setting v(x/y) := v(x) -v(y)
and v(0) = +∞. For example, if p is prime, the p-adic valuation is the discrete valuation vp on the
ring A = Z, whose extension to Q is computed by putting a rational number t in the form pna/b,
where p ∤ab, and setting vp(t) = n. In Problem 6, the ring A has the discrete valuation
$$
v: A \toZ
$$
a \mapstomin
n
$$
k : a \in
$$
xko
$$
.
$$
To connect this to the above example, if A = Z(p) (i.e., the localization of Z at (p)), then the
valuation obtained coincides with the p-adic valuation in the common field of fractions Q.
---
## 2. Norm and Trace
In this section we explore the concepts of norm and trace. We used the latter heavily to prove
that the ring of integers of a number field is a Noetherian ring (and thereafter a Dedekind domain).
Let L/K be a finite extension of K. An element x \inL defines a “multiplication by x” map
$$
mx : L \toL
$$
y \mapstoxy
The map mx is K-linear, i.e., viewing L as a K-vector space, the map mx is a K-linear operator
on L. If we fix a basis for L as a K-vector space, then mx will be given by an n × n matrix with
coeﬃcients in K, where n = [L : K]. Thus, we can talk about the trace and the determinant of
mx, which is independent of the chosen basis for L/K. Define the trace and norm, respectively, by

the maps
$$
T : L \toK
N : L \toK
$$
x \mapstoTr(mx)
x \mapstodet(mx)
The map T can be used in turn to define a (symmetric) K-bilinear form
$$
B: L \times L \toK
$$
(x, y) \mapstoT(xy)
**(5)** Prove that if L/K is separable then the form B is non-degenerate, i.e., if B(x, y) = 0 for all
$$
y \inL, then x = 0. (Equivalently, B is non-degenerate if for any basis v1, . . . , vn for L/K, the
$$
determinant of the matrix [B(vi, vj)] is nonzero.)
Hints: Since the extension is separable, by the primitive element theorem, we have L = K(θ) for
some θ \inL. Hence L has a K-basis of the form {1, θ, . . . , θn-1}, where n = [L : K]. Compute the
matrix of the form B with respect to this basis, and use Vandermonde determinants to show it is
not zero.
**(6)** Let L/K be a finite separable field extension. Let σ: L \toK vary over the K-embeddings of
L into a fixed algebraic closure of K. Prove that
(a) T(x) =
X
σ
σ(x).
(b) N(x) =
Y
σ
σ(x)
Hint: The characteristic polynomial fx(t) of the operator mx is a power fx(t) = px(t)d of the
$$
minimal polynomial px(t) of mx, and deg(px(t)) = [K(x) : K] =: m. To see this: 1, . . . , xm-1 is a
$$
basis for K(x)/K; letting v1, . . . , vd be a bassi for L/K(x), we have that
$$
v1, v1x, . . . , v1xm-1, . . . , vd, vdx, . . . , vdxm-1
$$
is a basis for L/K. Compute the matrix of mx with respect to this basis. Now partition the set
HomK(L, K) into m equivalence classes, by the equivalence relation σ ∼τ $\Longleftrightarrow$σ(x) = τ(x), of d
elements each. Let σ1, . . . , σm be a set of representatives. Show that
px(t) =
m
Y
i=1
(t -σi(x))
$$
and
$$
fx(t) =
Y
σ\inHomK(L,K)
(t -σ(x)).
If L/K is a finite Galois extension, then the embeddings σ: L \toK correspond to elements of
the Galois group Gal(L/K).
**(7)** Let A be a Dedekind domain with field of fractions K, let L/K be a finite separable field
extension, and let B be the integral closure of A in L. Prove that if x \inB, then T(x) \inA and
N(x) \inA.
Hint: You should use the fact that Dedekind domains are integrally closed, which we’ll discuss
in class on Monday. Show that T(x), N(x) \inK are integral over A (using the equalities from
Problem 6).
