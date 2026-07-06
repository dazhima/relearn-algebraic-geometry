# Homework 11

*MATH 464, Rice University, Spring 2020 · Due: Friday, April 24th, by 5pm. Each exercise is worth 10 points*

---

Due date: Friday, April 24th, by 5pm. Each exercise is worth 10 points.
Math 464 students should turn in complete problem 4 and two other problems.
Math 564 students should do ALL the exercises.
Unless otherwise indicated, A is a commutative ring, with unit.
---
## 1. Algebraic Closure
We have been discussing algebraically closed fields lately, and we have taken for granted
the fact that every field k has an algebraic closure. Please take a look at exercise 13 of
Chapter 1 of Atiyah-MacDonald. You don’t have to hand this exercise in, but you should
think about it for your own personal benefit.
---
## 2. Affine Algebraic Geometry IV: Grand Finale
You should have Problem Set 7 handy, so you can recall some of the objects used below.
In the last installment of our series, we saw how to associate a β-sheaf to the topological
space Spec A. Namely we showed that the assignment D(f) \mapstoAf satisfies the sheaf axioms
when we restrict our attention to covers involving only basic open sets. For this problem
set, we need the full-blown version of the structure sheaf of Spec A, i.e., we’ll need to know
what to do on general open sets.
Let U \subseteqSpec A be an open set. Let
$$
O(U) :=
$$
(
$$
functions s: U \to
$$
a
p\inU
Ap

$$
s(p) \inAp, s is locally of the form a/f
$$
)
$$
.
$$
When we say “s is locally of the form a/f” we mean that for each p \inU there is a neigh-
borhood V of p contained in U and elements a, f \inA such that for each q \inV , we have
f /\inq and s(q) = a/f in Aq. Note that O(U) is a commutative ring with unit.
From the definition, O is a sheaf (see problem set 7 for the axioms of a sheaf). What is
not clear is that this definition specializes to our previous β-sheaf, i.e., if there is any justice
in this world, we should have O(D(f)) \simeq Af, but this is not so easy to see.

**(1)** Define a homomorphism ψ: Af \toO(D(f)) by sending a/f n to the function s \in
O(D(f)) that assigns to each p \inD(f) the element a/f n \inAp. Show that ψ is
injective.
The homomorphism ψ is also surjective, but this is somewhat harder to show. In fact the
proof uses the same ideas involved Problem 3 of Problem Set 7, so I won’t ask you to do
this. In any case, we now have a full-blown sheaf on Spec A that generalizes the β-sheaf of
Problem Set 7. Note that when we take f = 1 we obtain O(Spec A) \simeq A.
**(2)** Show that the stalk Op of O at p \inSpec A is isomorphic to the local ring Ap. [Hint:
Start by defining a map Op \toAp.]
To define the category of aﬃne schemes, we need to know what a locally ringed space is.
This will take a couple of definitions.
**Definition 2.1**. Let F, G be sheaves of rings on a topological space X. A map of sheaves
φ: F \toG is a collection of ring homomorphisms φ(U): F(U) \toG (U), one for each open
subset U of X. These maps must be compatible with the restriction maps of the sheaf, i.e.,
for every inclusion V \subseteqU, we have a commutative diagram
F(U)
φ(U) /
ρF
V U 
G (U)
ρG
V U

F(V )
φ(V )
/ G (V )
**Definition 2.2**. Let f : X \toY be a map of topological spaces and let F be a sheaf of rings
on X. We define the push-forward sheaf f∗F as the sheaf on Y defined by the assignment
$$
f∗F(V ) := F(f -1(V ))
$$
for any open subset V \subseteqY .
**Definition 2.3**. A ringed space is a pair (X, OX) consisting of a topological space X and a
sheaf of rings OX on X. The sheaf OX is referred to as the structure sheaf of X. A map of
locally ringed spaces (f, f #): (X, OX) \to(Y, OY ) consists of a continuous map f : X \toY
$$
and a map f # : OY \tof∗OX of sheaves of rings on Y .
$$
For every open subset V \subseteqY , the map f # : OY \tof∗OX gives a map of rings OY (V ) \to
OX(f -1(V )). Let P \inX; note that as V ranges over all neighborhoods of f(P), f -1(V )
ranges over a subset of neighborhoods of P. Taking direct limits, we get a map
OY,f(P) = lim
$$
-\to
$$
V
OY (V ) \tolim
$$
-\to
$$
V
OX(f -1(V )),
and the codomain naturally maps to the stalk OX,P. Thus, for each P \inX, the map f #
induces a map of rings
f #
$$
P : OY,f(P) \toOX,P.
$$

**Definition 2.4**. The ringed space (X, OX) is a locally ringed space if, in addition, the
stalk OX,P is a local ring for every P \inX.
A map of locally ringed spaces is a map
(f, f #): (X, OX) \to(Y, OY ) of ringed spaces such that the induced maps on stalks f #
P are
local homomorphisms of local rings. (Note: a map φ: A \toB between local rings is said to
$$
be a local homomorphism if φ-1(mB) = mA.)
$$
Locally ringed spaces form a category. Note that topological manifolds are locally ringed
spaces, where the structure sheaf is the sheaf of continuous functions; the stalk at a point P
consists of functions which coincide in small neighborhoods of P (i.e. the germ of continuous
functions at P). This stalk is a local ring where the maximal ideal consists of equivalence
classes of functions that vanish at P. Many theorems from topology can be phrased com-
pactly (no pun intended!) using the language of sheaves and locally ringed spaces.
Note that, by problem (2), the pair (Spec A, OSpec A), where OSpec A is the sheaf O we
defined above, is a locally ringed space.
**(3)** Let φ: A \toB be a ring homomorphism. Show that φ induces a natural morphism
of locally ringed spaces
$$
(f, f #): (\operatorname{Spec} B, OSpec B) \to(\operatorname{Spec} A, OSpec A)
$$
where for any q \inSpec B, the map f #
$$
q : OSpec A,φ-1(q) \toOSpec B,q is the localization
map φq : Aφ-1(q) \toBq.
$$
**Definition 2.5**. The category of aﬃne schemes is the category whose objects are locally
ringed spaces that are isomorphic (as locally ringed spaces) to (Spec A, OSpec A), and whose
morphisms are maps of locally ringed spaces.
We will now show one of the main results of this course.
**Theorem 2.6**. The functor
$$
{Commutative rings with unit}
$$
\to
$$
{Aﬃne Schemes}
$$
A
\mapsto
(Spec A, OSpec A)
$$
φ: A \toB
$$
\mapsto
$$
(f, f #): (\operatorname{Spec} B, OSpec B) \to(\operatorname{Spec} A, OSpec A)
$$
is an equivalence of categories.
**(4)** Prove Theorem 2.6 by showing that the functor defined is fully faithful and essentially
surjective. The key to proving full faithfulness is to keep in mind that the induced
stalk maps are local homomorphisms of local rings.
Note the importance of the structure sheaf in this last problem: recall that we saw in
problem set 1 that just knowing that a topological space is isomorphic to the spectrum of a
ring is not enough to recover the ring, because Spec A and Spec A/N(A) are homeomorphic.
However, we can recover the ring from the structure sheaf by looking at the ring of global
sections OSpec A(Spec A).

**Remark 2.7**. A scheme is a locally ringed space (X, OX) that can be covered by open sets U
such that (U, OX|U) is an aﬃne scheme.
**Remark 2.8**. Recall that the category of commutative rings with unit has fibered co-products:
$$
the fibered coproduct of A \toB and A \toC is B \otimesA \mathbb{C}. By Theorem 2.6, the category of
$$
aﬃne schemes has fibered products (the functor is contravariant, so fibered co-products turn
into fibered products, as you showed in the midterm):
$$
\operatorname{Spec} B \timesSpec A \operatorname{Spec} \mathbb{C} \simeq \operatorname{Spec} B \otimesA \mathbb{C},
$$
and ditto for the structure sheaves.
