# Lecture 25 — The geometry of Primary Decomposition (continued)

*MATH 464, Rice University, Spring 2020 · March 27, 2020*

---

## 1. The geometry of Primary Decomposition (continued)
Recall from last class that we saw that a primary decomposition a = ∩n
i=1qi for qi primary
ideals allows us to write the topological space V (a) as a finite union V (a) = ∪n
i=1V (qi), and
we could even replace V (qi) with V (r(qi)), if we like, and the r(qi)) are prime ideals.
**Example 1.1**. Let A = C[x, y], and let a = (x2, y). We showed that a is a primary ideal,
and r(a) = (x, y). The quotient map
$$
\mathbb{C}[x, y] \toC[x, y]/(x2, y)
$$
gives rise to a map of prime spectra
$$
V (a) = \operatorname{Spec} \mathbb{C}[x, y]/(x2, y) \toSpec \mathbb{C}[x, y] = A2
$$
that a homeomorphism onto its image. This time, set-theoretically, we have
$$
V (a) = V (r(a)) = V (x, y) = the origin in A2.
$$
There is a sheaf of functions O on X = Spec C[x, y]/(x2, y), and its global sections are
$$
O(X) = \mathbb{C}[x, y]/(x2, y)
$$
This means that a global function on X is a polynomial of the form ¯f = a0 + a1¯x with a0,
a1 \inC. Note that
a0 = ¯f(0, 0)
$$
and
$$
a1 = ∂¯f
∂¯x(0, 0).
So X is topologically the origin A2, but its global functions are able to record a first derivative
in the x-direction!
**Example 1.2**. Let A = C[x, y], and let a = (x, y)n+1. The aﬃne scheme
$$
X := \operatorname{Spec} \mathbb{C}[x, y]/(x, y)n+1
$$
is called the n-th infinitesimal neighborhood of the origin.
Set-theoretically, X is just the
origin, since
$$
X = V ((x, y)n) = V (x, y),
$$
but the sheaf of functions on X has global sections
$$
O(X) = \mathbb{C}[x, y]/(x, y)n+1
$$

which have the form
$$
¯f = a0 + a1,x¯x + a1,y¯y + \cdot \cdot \cdot +
$$
n
X
i=0
$$
an,xn-iyi¯xn-i¯yi
$$
And as in Example 1.1, the coeﬃcients of this function are recovered as mixed partial deriva-
tives of f of order ≤n in each of ¯x and ¯y.
**Example 1.3**. We come back to the example A = C[x, y], and let a = (x2, xy). The primary
decomposition a = (x) ∩(x, y)2 shows that we have an isomorphism of rings
$$
\simeqC[x, y]/a \simeqC[x, y]/(x) \times \mathbb{C}[x, y]/(x, y)2
$$
that comes from the projection maps
$$
\mathbb{C}[x, y] \toC[x, y]/(x)
and
\mathbb{C}[x, y] \toC[x, y]/(x, y)2.
$$
Applying the functor Spec, we obtain
$$
X := \operatorname{Spec} \mathbb{C}[x, y]/a \simeqSpec
\mathbb{C}[x, y]/(x) \times \mathbb{C}[x, y]/(x, y)2
= \operatorname{Spec} \mathbb{C}[x, y]/(x) ⊔\operatorname{Spec} \mathbb{C}[x, y]/(x, y)2,
$$
where the last equality follows because Spec is contravariant and the co-product in the
category of aﬃne schemes is disjoint union. This disjoint union consists of the y-axis (corre-
sponding to the isolated component V (x) of X) and the first-order infinitesimal neighborhood
of the origin (which is “embedded” in the y-axis).
---
## 2. Finite ring extensions and integrality
We understand finite field extensions (to say that k′/k is a finite extension of fields just
means that k′ is finite dimensional as a k vector space)—this is the content of linear algebra.
What are finite extensions of rings? And what are they good for? Taking a cue from the
theory of vector spaces, to say a ring extension A \subseteqB is finite should mean that B is finitely
generated as an A-module. We’ll study this in a little more generality, using the concept of
algebra. Recall that an A-algebra is a map of rings φ: A \toB.
**Definition 2.1**. An A-algebra φ: A \toB is finite if B is finitely generated as an A-module.
**Remark 2.2**. This definition should not be confused with the concept of finite generatedness
as an A-algebra. We say that B is a finitely generated A-algebra if there exist b1, . . . , bn \inB
such that every element of B is a polynomial combination of b1, . . . , bn with coeﬃcients in
A.
**Example 2.3**. The key example to remember is the canonical inclusion φ: k \tok[x1, . . . , xn].
Note that k[x1, . . . , xn] is finitely generated as a k-algebra, but it is not a finite k-algebra
(i.e., as a k-vector space, k[x1, . . . , xn] is infinite-dimensional).
The concept bridging finiteness of algebras to finiteness as A-modules is integrality. This
concept leads, in one fell swoop, so the following seemingly distinct phenomena:

• Rings of integers of number fields
• Singularities of plane curves and resolutions of singularities of curves.
The slogan whose content we will prove in this lecture is:
$$
finite = finitely generated + integral.
$$
**Definition 2.4**. Let φ: A \toB be an A-algebra. We say that an element x \inB is integral
over A if there exists a relation (in B) of the form
$$
xn + a1xn-1 + \cdot \cdot \cdot + an = 0.
$$
ai \inA,
i = 1, . . . , n.
Observe that this relation is monic.
**Definition 2.5**. We say that B is integral over A if every element of B is integral over A.
**Example 2.6**. Take the inclusion φ: Z \toQ. Take r/s \inQ such that (r, s) = 1 and suppose
that it is integral. Then it satisfies a relation of the form
r
s
n
+ a1
r
s
n-1
$$
+ \cdot \cdot \cdot + an = 0.
$$
and clearing denominators we get
$$
rn + a1srn-1 + \cdot \cdot \cdot + ansn = 0,
$$
which shows that s ∤rn, so that s = ±1. This shows that the integral elements of Q as a
Z-algebra are precisely the integers!
**Example 2.7**. Take the inclusion φ: Z \toZ
 1

$$
. It is not an integral extension: 1/3 is not
$$
integral over Z. To see this, argue as in the example above.
**Example 2.8**. In the same vein, let f \ink[x] be an irreducible polynomial. Then k[x] \to
k[x]
h
f
i
$$
is not an integral extension: 1/f is not integral over k[x].
$$
**Example 2.9**. The inclusion k[x2] \subseteqk[x] is integral.
The proof of the following lemma can be transferred from the theory of vector spaces.
**Lemma 2.10**. Let A \subseteqB \subseteqC be inclusions of rings. If C is a finite B-algebra and B is a
finite A-algebra then C is a finite A-algebra.
$\square$
Here is how finiteness and integrality are related.
**Theorem 2.11**. Let φ: A \toB be an A-algebra; identify A with its image in B.
The
following are equivalent
(1) x \inB is integral over A;
(2) A[x] is a finite A-algebra, i.e., A[x] is a finitely generated A-module;

(3) there is a subring A[x] \subseteqC \subseteqB such that C is a finite A-algebra.
The key is to use our souped-up version of Cayley-Hamilton to prove that (3) =$\Rightarrow$(1).
Let’s start by recalling this theorem.
**Theorem 2.12** *(Cayley-Hamilton).* Let M be a finitely generated A-module, and let a \subseteqA
be an ideal. Suppose the endomorphism φ: M \toM satisfies φ(M) \subseteqaM. Then φ satisfies
a relation of the form
$$
φn + a1φn-1 + \cdot \cdot \cdot + an = 0
$$
a1, . . . , an \ina.
This relation should be understood as equality of elements in End(M).
Proof of Theorem 2.11.
$$
(1) \Rightarrow(2): Say that x satisfies xn + a1xn-1 + \cdot \cdot \cdot + an = 0.
Then {1, x, . . . , xn-1} is a
$$
generating set for A[x] as an A-module. (Note how important it is for the relation to be
monic!)
$$
(2) \Rightarrow(3): Take \mathbb{C} = A[x].
$$
(3) $\Rightarrow$(1): Consider the endomorphism φx : C \toC given by c \mapstocx. Apply the Cayley-
Hamilton Theorem with a = A. Thus φx satisfies a relation of the form
$$
(φx)n + a1(φx)n-1 + \cdot \cdot \cdot + an = 0.
$$
Apply this relation to the element 1 \inC (note C is a subring of B!!!). We get
$$
xn + a1xn-1 + \cdot \cdot \cdot + an = 0,
$$
and so x is integral over A.
$\square$
