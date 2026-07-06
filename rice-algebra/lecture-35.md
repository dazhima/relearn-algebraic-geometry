# Lecture 35 — Enough Injectives

*MATH 464, Rice University, Spring 2020 · April 8, 2020*

---

## 1. Enough Injectives
As usual, A is a commutative ring with unit. Our goals in this lecture is to prove the
following theorem.
**Theorem 1.1**. The category of A-modules has enough injectives, i.e., for every A-module
M there exists an injective A-module I and an injective map M ,\toI.
One of the first steps towards this goals was the lemma we proved at the end of the last
lecture:
**Proposition 1.2** *(Injectivity test lemma).* An A-module I is injective if and only if there
is a filler g for every diagram of the form
/ a
φ
/
f

A
g

I
where a is an ideal of A.
$\square$
**Corollary 1.3**. Let M be an A-module. Suppose that A is a PID, and that aM = M for
every nonzero a. Then M is injective.
*Proof.* Since A is a PID, any ideal a \subseteqA is of the form (a). Suppose we have a diagram of
the form
/ (a)
i
/
f

A
M
We need a filler g: A \toM for this diagram. If a = 0, then we can take g to be the zero
map. Otherwise, since aM = M, we have f(a) = am for some m \inM. Define g: A \toM
by setting g(x) = mx. (Check this is a filler!)
$\square$
For example, the above Corollary says that Q is injective when considered as a Z-module,
and so is Q/Z. In fact, the property that aM = M for every nonzero a has a special name,
even in the setting when A is not a PID.

**Definition 1.4**. An A-module M is divisible if aM = M for every non zerodivisor a \inA.
**Corollary 1**. 3 says that over a PID, a divisible module is injective. The converse statement,
that an injective module is divisible, is true over an arbitrary A. So over a PID the notions
of injective and divisible coincide. Note, on the other hand, that Z is not divisible as a
Z-module, it follows that Z is not injective as a Z-module!
Any A-module M is isomorphic to a quotient F/K, where F is a free module. If A is a
domain, then we have
$$
F/K \simeq (\oplusA)/K ,\to(\oplusFrac(A))/K.
$$
Suppose that A is a PID. Then $\oplus$Frac(A) is divisible, and then so is ($\oplus$Frac A)/K. These
modules are thus injective! Again, think of Q/Z as a Z module to fix ideas.
As a key step towards proving Theorem 1.1, we’ll now show that the category of Z-modules
(a.k.a abelian groups) has enough injectives.
**Lemma 1.5**. Let H be an abelian group. Then there exists a divisible abelian group G and
an injection H ,\toG.
*Proof.* Let ˆH = HomZ(H, Q/Z). This group is called the dual group of H. We can define a
map H \toˆˆH via the assignment
$$
h 7\to[[φ: H \toQ/\mathbb{Z}] 7\toφ(h)]
$$
We claim that this map is injective. Otherwise, there is an h \inH such that φ(h) = 0 for
every φ \inˆH = HomZ(H, Q/Z). Since Q/Z is injective, for any diagram of the form
/ ⟨h⟩
i
/
φ0

H
Q/Z
$$
there exists a filler φ: H \toQ/\mathbb{Z}.
$$
So to get a contradiction, it suﬃces to find a map
φ0 : ⟨h⟩\toQ/Z such that φ0(h) \neq 0. Now H being an abelian group, we know that ⟨h⟩\simeq Z
or Z/nZ for some n > 1. In the former case, take φ0(h) = 1/2; in the latter case take
$$
φ0(h) = 1/n. Hence the map H \toˆˆH is injective.
$$
Now ˆH is a Z-module; every module being the homomorphic image of a free module, we
know there is a set I an exact sequence
M
i\inI
$$
\mathbb{Z} \toˆH \to0.
$$
Taking duals we obtain
$$
0 \toˆˆH \toHomZ
$$
M
i\inI
Z, Q/Z
!
=
Y
i\inI
$$
HomZ(\mathbb{Z}, \mathbb{Q}/\mathbb{Z}) \simeq
$$
Y
i\inI
Q/Z

So we have a chain of injections
$$
H ,\toˆˆH ,\to
$$
Y
i\inI
Q/Z
The latter module is the product of injective Z-modules, so it is an injective Z-module.
$\square$
**Lemma 1.6**. Let M be a flat A-module, and let G be a divisible abelian group (i.e., and
injective Z-module). Then HomZ(M, G) is an injective A-module.
Note that HomZ(M, G) is an A-module by the rule a · φ(m) := φ(am).
*Proof.* Let
$$
0 \toN ′ \toN \toN ′′ \to0
$$
be a short exact sequence of A-modules. Since M is flat over A, the tensored sequence
$$
0 \toM \otimesA N ′ \toM \otimesA N \toM \otimesA N ′′ \to0
$$
is also exact. Since G is an injective Z-module, the functor HomZ(•, G) is also exact, so the
sequence
$$
0 \toHomZ(M \otimesA N ′′, G) \toHomZ(M \otimesA N, G) \toHomZ(M \otimesA N ′, G) \to0
$$
is also exact. Adjointness of Hom and $\otimes$implies the sequence
0 \toHomA(N ′′, HomZ(M, G)) \toHomA(N, HomZ(M, G)) \toHomA(N ′, HomZ(M, G)) \to0
Hence the functor HomA(•, HomZ(M, G)) is exact, and HomZ(M, G) is an injective A-
module.
$\square$
We come to today’s Main Theorem.
Proof of Theorem 1.1. Consider M as an abelian group (i.e., forget scalar multiplication by
elements of A). Since the category of abelian groups has enough injectives, there is a divisible
$$
ableian group G and an injection φ: M \toG. Now
M \simeq HomA(A, M) \subsetHomZ(A, M) \simeq HomZ(A, φ(M)) \subsetHomZ(A, G),
$$
and this last module is injective as an A-module, applying Lemma 1.6 with M = A.
$\square$
