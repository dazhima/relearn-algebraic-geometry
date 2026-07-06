# Lecture 30 — Strong Nullstellensatz

*MATH 464, Rice University, Spring 2020 · April 7, 2020*

---

## 1. Strong Nullstellensatz
**Theorem 1.1** *(Strong Nullstellensatz).* Let k be an algebraically closed field, and let J \subseteq
k[X1, . . . , Xn] be an ideal.
(1) If J is not the unit ideal, then V (J) \neq $\emptyset$.
(2) I(V (J)) =
√
J.
**Corollary 1.2**. Let k be an algebraically closed field. Then there is a one-to-one correspon-
dence between radical ideals of k[X1, . . . , Xn] and algebraic sets in kn.
We will also relate this to finitely generated k algebras with no nilpotent elements: Note
that k[V ] has no nilpotent elements since its nilradical is the image of the radical of I(V )
in k[V ], but this is just zero, since I(V ) is a radical ideal by the NullStellensatz. That is,
there is also a one-to-one correspondence between algebraic sets in kn and finitely generated
k algebras with no nilpotent elements given by sending V to k[V ].
Proof of the Strong Nullstellensatz. (1) If J is not the unit ideal, then it is contained in a
maximal ideal of k[X1, . . . , Xn], which is of the form (X1 -a1, . . . , Xn -an) by the weak
$$
NullStellensatz. But then P = (a1, . . . , an) \inV (J), so V (J) \neq \emptyset.
$$
(2) The inclusion
√
$$
J \subseteqI(V (J)) is easy: if f N \inJ for some N > 0, then f N(P) = 0 for every
$$
P \inV (J). Since k is a field, this implies that f(P) = 0 for every P \inV (J), so f \inI(V (J)).
It suﬃces now to show that I(V (J)) \subseteq
√
$$
J. Let f \inI(V (J)); we want to show that f N \inJ
$$
for some N > 0, or in other words, that f is a nilpotent element in k[X1, . . . , Xn]/J. We
can accomplish this by showing that the localized ring (k[X1, . . . , Xn]/J)f is the zero ring.
This localization is isomorphic to the ring
$$
k[X1, . . . , Xn, Y ]/ (J + (fY -1)) .
Let J′ = J + (fY -1). By definition of I( • ), the polynomial f \ink[X1, . . . , Xn] vanishes
at all P \inV (J). So a point (a1, . . . , an, b) \inV (J′) is a point (a1, . . . , an) \inV (J) such that
bf(a1, . . . , an) = 1, i.e., P \inV (J) and f(P) \neq 0. Since f was supposed to vanish on all
$$
P \inV (J), we conclude that V (J′) = $\emptyset$. By part (1) this means that J′ is the unit ideal in
k[X1, . . . , Xn, Y ].
$\square$
---
## 2. Maps between algebraic sets
So far we have studied algebraic sets in isolation. How are they related to each other?
Since, by definition, these sets are the zero loci of a set of polynomials, the maps between
these sets should also be defined by polynomials.
**Definition 2.1**. Let V \subseteqkn and W \subseteqkm be algebraic sets. A maps of sets φ: V \toW is a
regular map of algebraic sets if there exist polynomials φ1, . . . , φm \ink[X1, . . . , Xn] such that
φ(a1 . . . , an) = (φ1(a1, . . . , an), . . . , φm(a1, . . . , an))
Note that the polynomials φi are defined up to elements of I(V ), i.e., perturbing φi by a
$$
polynomial in I(V ) gives the same map φ: V \toW.
$$
**Example 2.2**. Let V = k and let W \subseteqk2 be the cuspidal cubic defined by y2 -x3 = 0.
The map of sets φ: V \toW given by t \mapsto(t2, t3) is a regular map of algebraic sets: take
$$
φ1(t) = t2 and φ2(t) = t3.
$$
Thus, algebraic sets form a category: the objects are algebraic sets, and the morphisms
are regular maps between algebraic sets
---
## 3. An equivalence of categories
Define a contravariant functor
Γ: { algebraic sets V } \to{ Finitely generated, reduced k-algebras }
$$
V 7\tok[V ] = k[X1, . . . , Xn]/I(V )
[φ: V \toW] 7\to[φ∗: k[W] \tok[V ], f 7\tof ◦φ]
$$
The definition of this functor already uses the strong NullStellensatz, since we are asserting
that I(V ) is a radical ideal, so that k[V ] is reduced, i.e., it has no nilpotent elements.
**Example 3.1**. If V = k and if W \subseteqk2 is the cuspidal cubic defined by y2 -x3 = 0, then
$$
the map φ: V \toW in the previous section induces a map φ∗: k[X, Y ]/(Y 2 -X3) \tok[t]
$$
that takes F(x, y) to F(t). Here x and y denote the images of X and Y in k[W].
$$
Write k[V ] = k[X1, . . . , Xn]/I(V ) and k[W] = k[Y1, . . . , Ym]/I(W), and let yi denote the
image of Yi in k[W]. If φ: V \toW is given by polynomials φ1, . . . , φm \ink[X1, . . . , Xn], then
$$
by definition, we have
$$
φ∗(yi) = φi + I(V ).
$$
**Theorem 3.2**. The functor Γ is an equivalence of categories.
*Proof.* We’ll show that Γ is essentially surjective and fully faithful. For essential surjectivity,
let A be a finitely generated, reduced k-algebra. Then A \simeq k[X1, . . . , Xn]/J, where J is a
radical ideal in the polynomial ring k[X1, . . . , Xn]. Let V := V (J) \subseteqkn. Then
$$
Γ(V ) = k[V ] = k[X1, . . . , Xn]/I(V ),
$$

$$
and by the Strong Nullstellensatz we have I(V ) = I(V (J)) =
$$
√
J = J.
Now we show that Γ is fully faithful. We need to show that the set Reg(V, W) of regular
maps between two algebraic sets V and W is in bijection with the set Homk-alg(k[W], k[V ])
via Γ. We look at injectivity: suppose that φ∗= ψ∗as maps k[W] \tok[V ]. Recall that
$$
φ∗(yi) = φi + I(V )
and
ψ∗(yi) = ψi + I(V ),
$$
so that φi and ψi coincide up to an element of I(V ). This shows that φ = ψ. Lastly, we will
show surjectivity next time.
$\square$
