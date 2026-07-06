# Homework 07

*MATH 464, Rice University, Spring 2020 · Due: FRIDAY, March 27th, by 5pm. Each exercise is worth 10 points*

---

Due date: FRIDAY, March 27th, by 5pm. Each exercise is worth 10 points.
Math 464 students should turn in complete problems worth a total of at least 30 points (e.g.,
problems (1), (3), and (4)) but should carefully read and understand the statements of all eight
problems.
Math 564 students should do ALL the exercises.
Unless otherwise indicated, A is a commutative ring, with unit.
---
## 1. Affine Algebraic Geometry: Part III
In this installment of our developing story, we will finally introduce the sheaf of regular functions
on Spec A. First, let me just say what a sheaf is on a topological space X. A presheaf of rings on
X is an assignment U \mapstoF(U) of a ring F(U) to each open subset U of X, together with maps
ρV U : F(U) \toF(V ) for each inclusion V \subseteqU of open sets, such that
(i) F($\emptyset$) = 0.
(ii) ρUU = id
$$
(iii) If W \subseteqV \subseteqU then ρWU = ρV U ◦ρWV .
$$
The maps ρV U are known as restriction maps. A presheaf is called a sheaf if in addition we have
the following:
(iv) For any open cover (Ui)i\inI of X and any collection of elements si \inF(Ui) (i \inI) such
that the restrictions of si and sj to F(Ui ∩Uj) are equal (for all i, j), there exists a unique
element s \inF(X) whose restriction to F(Ui) is si.
**Example 1.1**. The sheaf of continuous, real-valued functions on a space.
For each open set
$$
U \subseteqX, we let F(U) be the set of continuous functions U \toR; we give F(U) the structure of a
$$
ring by pointwise addition and multiplication. The restriction maps are just the usual restrictions of
functions. Axiom (iv) just says that specifying a continuous function on an open cover, compatibly
on overlaps, is the same as specifying a continuous function on the whole space.
**Definition 1.2**. The stalk of a sheaf F at a point x \inX is
$$
Fx := lim
-\to
$$
x\inU
F(U),
where the direct limit is taken over open subsets U \subseteqX that contain X.
We know what a direct limit is now, so we can describe this very explicitly. An element of Fx is
represented by a pair (U, s), where s \inF(U) for some U containing x, and two elements (U, s) and
(V, t) represent the same element in the direct limit if there is an open set W \subseteqU ∩V , containing

x, and an element (W, r) such that s and t restrict to r on W. In our example above, the stalk at
x is usually known as the germ of continuous functions at x.
Suppose that instead of specifying a ring for every open set U, we only specify rings on a basis
of open sets. Assume, however, that these rings and their restriction maps satisfy Axioms (i)–(iv)
above (taking only open covers by basis open sets in (iv)). This collection of information is usually
known as a β-sheaf. What’s amazing is that one can construct an honest sheaf on X out of a
β-sheaf; see Eisenbud’s and Harris’ book The Geometry of Schemes, Chapter 1. (This Chapter
may also help with the rest of the problem set in general.)
Our task here is to construct a β-sheaf of rings on X = $\operatorname{Spec}(A)$, using the open sets Xf =
D(f) as our basis of open sets. The associated sheaf is called the structure sheaf of X, and it
is usually denoted OX. Hence, out of a commutative ring with unit A, we can construct a pair
($\operatorname{Spec}(A)$, OSpec(A)). If we know that a pair (X, OX) consists of an aﬃne scheme together with its
structure sheaf, then we can actually recover A(!!).
**(1)** (a) Let φ: A \toS-1A be the canonical homomorphism. Show that the map
$$
φ∗: \operatorname{Spec}(S-1A) \toSpec(A)
$$
is a homeomorphism of $\operatorname{Spec}(S-1A)$ onto its image in X = $\operatorname{Spec}(A)$. (We denote this
image by S-1X.) In particular, if f \inA, the image of $\operatorname{Spec}(Af)$ in X is the basic open
set Xf = D(f).
(b) Let f : A \toB be a ring homomorphism. Write X = $\operatorname{Spec}(A)$, Y = $\operatorname{Spec}(B)$, and let
f∗: Y \toX be the associated map on ring spectra. We may identify $\operatorname{Spec}(S-1A)$ with
its image S-1X in X and $\operatorname{Spec}(S-1B)$ = $\operatorname{Spec}(f(S)$-1B) with its image S-1Y in Y .
Show that S-1f∗: $\operatorname{Spec}(S-1B)$ \to$\operatorname{Spec}(S-1A)$ is the restriction of f∗to S-1Y , and
that S-1Y = f∗-1(S-1X). [Hint: consider the commutative diagram
A
f
/
φA 
B
φB

S-1A
$$
S-1f / S-1B
$$
and apply the Spec functor to it. To show that S-1Y = f∗-1(S-1X) you need to
understand the relationship between prime ideals of B and prime ideals of S-1B =
f(S)-1B; look at your notes on ideal theory in localizations.]
$$
(c) Let a be an ideal of A and let b = ae be its extension in B. Let ¯f : A/a \toB/b be
$$
the homomorphism induced by f. Identify $\operatorname{Spec}(A/a)$ with its image V (a) in X and
$\operatorname{Spec}(B/b)$ with its image V (b) in $\operatorname{Spec}(B)$. Show that ¯f∗is the restriction of f∗to
V (b). [Hint: consider the commutative diagram
A
f
/

B

A/a
¯f
$$
/ B/b
$$
and apply the Spec functor to it; then use Problem 6(d) from Problem Set #1.]

**(2)** Let p be a prime ideal of A. Show that the canonical image of Xp = $\operatorname{Spec}(Ap)$ in X =
$\operatorname{Spec}(A)$ is equal to the intersection of all open neighborhoods of p in X. [Hint: What do
the prime ideals of Spec Ap look like?]
**(3)** Let U be a basic open subset of X = Spec A, i.e., U = Xf = D(f) for some f \inA.
(a) Show that the ring O(U) := Af depends only on U and not on f, i.e., if Xf = Xg then
Af \simeq Ag. Note that this isomorphism can be chosen canonically (because it comes
from a universal property).
(b) Let V = Xg be another basic open subset such that V \subseteqU. Show that gn = uf for
$$
some n > 0 and u \inA and use this to define a homomorphism ρ: O(U) \toO(V ) (i.e.,
$$
Af \toAg) by mapping a/fm to aum/gmn. Show that ρ depends only on U and V (in
the sense that changing the elements used to the define this map amounts to pre- and
post-composing with the canonical isomorphisms from part (a)). This map is called
the restriction homomorphism.
Not that if V = U then ρ is the identity map.
(c) Show that if W \subseteqV \subseteqU then the diagram of restriction arrows
O(U)
/
#
O(W)
O(V )
:
commutes.
(d) Let x = p be a point of X. Show that
lim
$$
-\to
$$
x\inU
O(U) \simeq Ap
(Here we are taking the direct limit over the basic open subsets of X that contain x).
**(4)** Show that the presheaf of the previous problem has the following property: Let (Ui)i\inI be
a cover of X by basic open subsets. For each i \inI, let si \inO(Ui). Suppose that for every
i and j the restrictions of si and sj coincide in O(Ui ∩Uj). Then there exists a unique
$$
s \inO(X) = A whose restriction to O(Ui) is si for all i \inI.
$$
Thus, the assignment U \mapstoO(U) is a β-sheaf.
