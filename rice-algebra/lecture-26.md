# Lecture 26 — Integral extensions

*MATH 464, Rice University, Spring 2020 · March 30, 2020*

---

## 1. Integral extensions
Recall the following definitions introduced last class:
**Definition 1.1**. An A-algebra φ: A \toB is finite if B is finitely generated as an A-module.
**Definition 1.2**. Let φ: A \toB be an A-algebra. We say that an element x \inB is integral
over A if there exists a relation (in B) of the form
$$
xn + a1xn-1 + \cdot \cdot \cdot + an = 0.
$$
ai \inA,
i = 1, . . . , n.
Observe that this relation is monic.
**Definition 1.3**. We say that B is integral over A if every element of B is integral over A.
We also proved the following relation between finiteness and integrality.
**Theorem 1.4**. Let φ: A \toB be an A-algebra; identify A with its image in B. The following
are equivalent
(1) x \inB is integral over A;
(2) A[x] is a finite A-algebra, i.e., A[x] is a finitely generated A-module;
(3) there is a subring A[x] \subseteqC \subseteqB such that C is a finite A-algebra.
There are two key corollaries to this theorem.
**Corollary 1.5**. Let B be an A-algebra. If x1, ..., xn \inB are integral over A, then A[x1, ..., xn]
is a finite A-algebra.
*Proof.* This follows easily by induction on n. The base case is the content of Theorem 1.4.
So suppose n > 1. Then we can consider the extensions
$$
A \subsetA[x1, ..., xn-1] \subsetA[x1, ..., xn-1][xn].
$$
The first inclusion is finite by the inductive hypothesis, and xn is integral over A, so the
same monic equation shows that xn is integral over A[x1, ..., xn-1]. Thus again by Theorem
1.4, A[x1, ..., xn-1][xn] is finite over A[x1, ..., xn-1]. Now by the tower law proved last class,
it follows that A[x1, ..., xn] is a finite A-algebra.
$\square$

**Corollary 1.6**. Let B be an A-algebra. Then the following are equivalent:
(1) B is a finite A-algebra.
(2) B is a finitely generated A-algebra and B is integral over A.
*Proof.* 
(1)
$$
\Rightarrow
$$
(2): Since B is a finitely generated A-module, it is clearly a finitely generated
A-algebra. To check integrality, consider x \inB. We know that A[x] \subsetB = B for B a finite
A-algebra, so using (3) =$\Rightarrow$(1) in Theorem 1.4, we conclude that x \inB is integral over A.
Since x \inB was arbitrary, B is integral over A.
(2) =$\Rightarrow$(1): Since B is a finitely generated A-algebra, B \simeq A[x1, ..., xn] for some elements
x1, ..., xn \inB. Then by Corollary 1.5, B is a finite A-algebra.
$\square$
**Theorem 1**. 4 along with Corollaries 1.5 and 1.6 yields incredible dividends.
**Proposition 1.7**. Let A \subseteqB \subseteqC be inclusions of rings.
(1) If x1, . . . , xm \inB are integral over A then any x \inA[x1 . . . , xn] is integral over A.
(2) If C is integral over B and B is integral over A then C is integral over A.
(3) The set
$$
eA := {x \inB : x is integral over A} \subseteqB.
$$
is a subring of B. Also, if x \inB is integral over eA, then x \ineA. In other words,
eeA = eA.
*Proof.* 
(1) By Corollary 1.5, A[x1, ..., xn] is finite, and so by Corollary 1.6, A[x1, ..., xn] is integral
over A, i.e. every x \inA[x1, ..., xn] is integral over A.
(2) Suppose that z \inC satisfies
$$
zn + bn-1zn-1 + \cdot \cdot \cdot + b0 = 0,
$$
bi \inB.
Each bi is integral over A by hypothesis, so by Theorem 1.4, each inclusion
$$
A \subseteqA[b0, . . . , bn-1] \subseteqA[b0, . . . , bn-1, z]
$$
is finite, so the overall inclusion is finite by the tower law. Then by Corollary 1.6, A[b0, . . . , bn-1, z]
is integral over A, and hence z \inC is integral over A for every z \inC.
(3) That eA is a subring follows from part (1) of the proposition: if x, y \inB are integral over
A, A[x, y] is integral over A, so in particular x ± y and xy are integral over A. For the last
claim note that the inclusions
$$
A \subseteqeA \subseteqeeA
$$
are each integral, so the overall inclusion is integral by the second part of the proposition.
$$
Thus for x \ineeA, x \inB is integral over A, i.e. x \ineA.
$$
$\square$

**Definition 1.8**. The ring eA is called the integral closure of A in B. If A = eA then we say
that A is integrally closed in B.
**Definition 1.9**. A domain A is said to be normal if it is integrally closed in its field of
fractions.
**Example 1.10**. We saw last time that Z is normal.
**Example 1.11**. More generally, UFDs are normal. (This will be a homework exercise).
**Example 1.12**. The ring A = k[X, Y ]/(Y 2 -X3) is not normal: Let x, y be the images of X
and Y under the quotient map k[X, Y ] \toA. Then one can show that the field of fractions
of A is k(t), where t = y/x. Unfortunately, t /\inA, and this is why A is not normal. Note,
however, that x -t2 = 0 and y -t3 = 0, so that t is integral over A. Since integral elements
form a ring, it follows that all elements of k[t] are integral over A. By definition of integral
closure, this means that k[t] is contained in the integral closure ˜A of A in Frac A. But k[t]
is integrally closed in Frac A = Frac k[t], because it is a UFD.
Now let’s see the reverse inclusion: if f is in ˜A, i.e. f \ink(t) is integral over A, then it’s
also integral over k[t] (the same relation will do the job). But k[t] is integrally closed, so
$$
f \ink[t], which shows that ˜A \subseteqk[t], so ˜A = k[t].
$$
The geometric picture is as follows: Spec A is a “cuspidal cubic”; it has a singularity at
the origin. The non-normality of A detects this! Furthermore, normalization ‘resolves the
singularity’ as follows: there is an inclusion A \subseteqk[t],and so we get a map Spec k[t] \toSpec A.
This maps takes the point t0 in the aﬃne line to the point (t2
0, t3
0) of the cuspidal cubic. The
aﬃne line is the desingularization of the cubic, and the map Spec k[t] \toSpec A is known as
the normalization or resolution morphism.
---
## 2. Going up
Here is a basic question, one that integrality settles. Suppose that A \subseteqB is a ring ex-
tension, and let p be a prime ideal of A. Is there a prime ideal q of B that restricts to p?
I.e., A ∩q = p? Since the map from A to B is an inclusion, we are asking that the con-
traction of q to A be p. In other words, is the induced morphism Spec B \toSpec A surjective?
Here is a concrete situation to think about: consider the inclusion Z \subseteqZ[i]. The ideal (5)
is prime in Z, but it is not prime in Z[i] because we have the factorization 5 = (2 + i)(2 -i),
and both 2 + i and 2 -i are not units of Z[i]. So we are asking if there is a prime ideal in
Z[i] that gives a “replacement” for (5). In this case, the answer is easy: the ideal (2 + i) (or
also (2 -i)) does the job. First note that it is indeed a prime ideal since
$$
\mathbb{Z}[i]/(2 + i) \simeq \mathbb{Z}[x]/(x2 + 1, x + 2) \simeq \mathbb{Z}/5Z
$$

and this last ring is a domain. Second, Z ∩(2 + i) is a principal ideal, and clearly (5) \subseteq
A ∩(2 + i). Unique factorization in Z easily shows that this containment is an equality.
