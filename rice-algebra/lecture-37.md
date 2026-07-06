# Lecture 37 — Tor (continued)

*MATH 464, Rice University, Spring 2020 · April 24, 2020*

---

## 1. Tor (continued)
Last class we introduced the functors TorA
n(M, •) on the category A-Mod. The following
proposition makes concrete the sense in which Tor measures the failure of flatness and/or
projectiveness.
**Proposition 1.1**. If M is a flat A-module, or if N is projective, then TorA
n(M, N) = 0 for
all n ≥1.
*Proof.* Recall how we compute Tor. Let
· · · \toPn
dn
$$
-\toPn-1 \to\cdot \cdot \cdot \toP1
$$
d1
$$
-\toP0
π-\toN \to0
$$
be a projective resolution of N. Apply the functor M $\otimes$A • to this exact sequence, omitting
$$
the term M \otimesA N from the resulting complex:
$$
(1)
$$
\cdot \cdot \cdot \toM \otimesA Pn
$$
idM $\otimes$dn
$$
-----\toM \otimesA Pn-1 \to\cdot \cdot \cdot \toM \otimesA P1
$$
idM $\otimes$d1
$$
----\toM \otimesA P0 \to0
$$
If M is flat then the sequence (1) is exact, except that the last map need not be surjective.
This means there are no nontrivial homology groups, so the modules TorA
n(M, N) are all zero
for n ≥1. If N is projective, then
· · · 0 \toN
id
$$
-\toN \to0
$$
is a projective resolution of N. Applying M $\otimes$A • and omitting the last term we get the
complex
$$
\cdot \cdot \cdot 0 \to0 \toM \otimesA N \to0
$$
which has no homology past the zero-th homology group.
$\square$
---
## 2. Ext
We can use the functor HomA(•, N), which is left exact, to define a series of functors
Extn
$$
A(•, N): A-Mod \toA-Mod
$$
such that HomA(•, N) \simeq Ext0
A(•, N) as functors on A-modules. The functor Ext1
A(•, N) will
measure the failure of exactness of HomA(•, N).

We begin by defining the functors on objects, so let M be an A-module and let ⟨Pn, dn⟩
be a projective resolution for it:
· · · \toPn
dn
$$
-\toPn-1 \to\cdot \cdot \cdot \toP1
$$
d1
$$
-\toP0
π-\toM \to0
$$
Apply the functor HomA(•, N) to this exact sequence, omitting the term HomA(M, N) from
the resulting complex:
0 \toHomA(P0, N)
d∗
$$
-\toHomA(P1, N) \to\cdot \cdot \cdot \toHomA(Pn-1, N)
$$
d∗
n-1
$$
---\toHomA(Pn, N) \to\cdot \cdot \cdot
$$
Define
Extn
$$
A(M, N) := \ker(d∗
$$
n)/ im(d∗
n-1).
As with the Tor functors, one shows that this definition does not depend on the chosen
projective resolution. Note, as promised, that Ext0
A(M, N) \simeq HomA(M, N).
**Example 2.1**. We compute Extn
Z(Z/pZ, N).
For a projective resolution of Z/pZ by Z-
modules we can take
(2)
$$
\cdot \cdot \cdot 0 \to0 \toZ
$$
×p
$$
-\toZ \toZ/pZ \to0.
$$
Applying HomZ(•, N) and omitting the first term, we obtain the complex
0 \toHomZ(Z, N)
(×p)∗
$$
---\toHomZ(\mathbb{Z}, N) \to0 \to\cdot \cdot \cdot
$$
Identifying HomZ(Z, N) with N, and thus (×p)∗with ×p, we obtain the complex
0 \toN
×p
$$
-\toN \to0 \to\cdot \cdot \cdot
$$
Conclusion:
Ext0
$$
\mathbb{Z}(\mathbb{Z}/pZ, N) = {n \inN : pn = 0}
$$
Ext1
$$
\mathbb{Z}(\mathbb{Z}/pZ, N) = N/pN
$$
Extn
$$
\mathbb{Z}(\mathbb{Z}/pZ, N) = 0 for all n \geq2
$$
**Example 2.2**. While we’re at it, the above work also lets us compute TorZ
n(M, Z/pZ).
Simply apply M $\otimes$Z • to (2), omitting the last term to get
$$
\cdot \cdot \cdot \to0 \toM
$$
×p
$$
-\toM \to0
$$
and conclude that
TorZ
$$
0(M, \mathbb{Z}/pZ) = M/pM \simeq M \otimesZ \mathbb{Z}/pZ
$$
TorZ
$$
1(M, \mathbb{Z}/pZ) = {m \inM : pm = 0}
$$
TorZ
$$
n(M, \mathbb{Z}/pZ) = 0 for all n \geq2
$$
---
## 3. Long exact sequences
Let K(A) be the category of chain complexes of A-modules, i.e., a category whose objects
are chain complexes
· · · \toCi
di
$$
-\toCi-1 \to\cdot \cdot \cdot
$$
of A-modules (which we denote ⟨Ci, di⟩for short) and whose morphisms are chain maps of
complexes:
· · ·
/ Ci
di /
φi

Ci-1
/
φi-1

· · ·
· · ·
$$
/ \mathbb{C}′
$$
i
d′
$$
i / \mathbb{C}′
$$
i-1
/ · · ·
$$
We can think of homology as a collection of functors Hn : K(A) \toA-Mod.
$$
**Remark 3.1**. If the indexing goes the other way, i.e., if our complexes naturally look like this:
· · ·
/ Ci
di /
φi

Ci+1
/
φi+1

· · ·
· · ·
$$
/ \mathbb{C}′
$$
i
d′
$$
i / \mathbb{C}′
$$
i+1
/ · · ·
then we call the above a chain map of co-chain complexes, and the homology at each spot is
more naturally called cohomology, and it is a series of functors Hn : co-K(A) \toA-Mod.
Think of Extn(M, N) here: when we applied the functor HomA(•, N) to a projective resolu-
tion of M, the arrows were turned around because the functor HomA(•, N) is contravariant.
We end up with a co-chain complex and thus our homology modules are really cohomology
modules.
Homology takes short exact sequences of complexes to long exact sequences. A short exact
sequence of complexes is what you think it is!
**Theorem 3.2**. Let
$$
0 \toC′
φ-\toC
ψ-\toC′′ \to0
$$
be a short exact sequence in K(A). Then, for every n \inZ there exists a map
$$
δn : Hn(\mathbb{C}′′) \toHn-1(\mathbb{C}′)
$$
such that the sequence of A-modules
$$
\cdot \cdot \cdot \toHn+1(\mathbb{C}′′)
$$
δn+1
$$
--\toHn(\mathbb{C}′)
$$
φ∗
$$
-\toHn(\mathbb{C})
$$
ψ∗
$$
-\toHn(\mathbb{C}′′)
$$
δn
$$
-\toHn-1(\mathbb{C}′) \to\cdot \cdot \cdot
$$
is exact. Further more, if
$$
/ \mathbb{C}′
$$
/

C
/

$$
\mathbb{C}′′
$$
/

$$
/ ˆC′
$$
/ ˆC
$$
/ ˆC′′
$$
/ 0

is a commuting diagram in K(A), then the diagrams
$$
Hn(\mathbb{C}′′)
$$
δn /

$$
Hn-1(\mathbb{C}′)
$$

$$
Hn( ˆC′′)
ˆδn / Hn-1( ˆC′)
$$
commutes for all n \inZ.
Sketch of proof. I will define the map δn and let you check the rest. The idea is to use the
snake lemma to define δn. Writing the exact sequence of complexes vertically, we have the
diagram



$$
/ \mathbb{C}′
$$
n
φn
/
d′
n

Cn
ψn
/
dn

$$
\mathbb{C}′′
$$
n
/
$$
d′′
$$
n

$$
/ \mathbb{C}′
$$
n-1
$$
φn-1 /
$$

Cn-1
$$
ψn-1 /
$$

$$
\mathbb{C}′′
$$
n-1
/

The snake lemma gave an exact sequence
ker(d′
$$
n) \toker(dn) \toker(d′′
n) \tocoker(d′
n) \tocoker(dn) \tocoker(d′′
$$
n)
$$
and the map \ker(d′′
n) \tocoker(d′
n) took x \inker(d′′
$$
n), lifted it to a y \inCn, pushed down to
$$
dn(y) \inC′
n and pulled this back to some z \inC′
$$
n-1. Define
$$
δn : Hn(\mathbb{C}′′) \toHn-1(\mathbb{C}′)
by taking, in the above notation, x+\operatorname{im}(d′′
n+1) 7\toz +\operatorname{im}(d′
$$
n). We have to check a few things:
$$
• z \inker(d′
$$
n-1)
• independence of the choice of y
$$
• if x \inim(d′′
n+1) then z \inim(d′
$$
n).
If you look at the maps in the long exact sequence given by the snake lemma, you’ll see that
this long exact sequence induces the long exact sequence in homology we’re looking for! So
most of the work is already done.
$\square$
**Corollary 3.3**.
(1) Let
$$
0 \toM ′′ \toM \toM ′′ \to0
$$

be a short exact sequence of A-modules. For every A-module N there is a long exact
sequence
· · · \toTorA
$$
1 (M ′, N) \toTorA
$$
1 (M, N) \toTorA
$$
1 (M ′′, N)
$$
δ1
$$
-\toM ′\otimesAN \toM\otimesAN \toM ′′\otimesAN \to0
$$
(2) Let
$$
0 \toN ′ \toN \toN ′′ \to0
$$
be a short exact sequence of A-modules. For every A-module M there is a long exact
sequence
$$
0 \toHomA(M, N ′) \toHomA(M, N) \toHomA(M, N ′′)
δ-\toExt1
A(M, N ′) \to\cdot \cdot \cdot
$$
**Remark 3.4**. This is the sense in which Tor1 and Ext1 can measure the failure of exactness
of the tensor and (contravariant) Hom functors.
*Proof.* For (1), let ⟨Pn, dn⟩be a projective resolution of N. Consider the diagram
$$
...
$$

$$
...
$$

$$
...
$$

$$
/ M ′ \otimesA P1
$$

$$
/ M \otimesA P1
$$

$$
/ M ′′ \otimesA P1
$$

/ 0
$$
/ M ′ \otimesA P0
$$

$$
/ M \otimesA P0
$$

$$
/ M ′′ \otimesA P0
$$

/ 0
This is an exact sequence in K(A): the rows are exact because the modules Pi are projective
(hence flat!), and the columns are complexes. The long exact sequence in homology now
follows from Theorem 2.2 from last lecture.
For (2), let ⟨Pn, dn⟩be a projective resolution of M. Consider the diagram
$$
...
...
...
/ HomA(P1, N ′)
$$
/
O
HomA(P1, N)
/
O
$$
HomA(P1, N ′′)
$$
/
O
$$
/ HomA(P0, N ′)
$$
/
O
HomA(P0, N)
/
O
$$
HomA(P0, N ′′)
$$
/
O
O
O
O

This is an exact sequence in co-K(A): the rows are exact because the modules Pi are pro-
jective, and the columns are cochain complexes. The long exact sequence in (co-)homology
now follows from Theorem 2.2 from last lecture.
$\square$
**Corollary 3.5**. The following are equivalent:
(1) M is a projective A-module;
(2) Extn
$$
A(M, N) = 0 for every A-module N and all n \geq1;
$$
(3) Ext1
A(M, N) = 0 for every A-module N.
*Proof.* Note that (1) =$\Rightarrow$(2) we have done before (take a silly projective resolution of M),
$$
and (2) \Rightarrow(3) is trivial. To see that (3) \Rightarrow(1), let
0 \toN ′ \toN \toN ′′ \to0
$$
be an exact sequence of A-modules.
Since Ext1
A(M, •) \simeq 0, the long exact sequence in
cohomology is actually short:
$$
0 \toHomA(M, N ′) \toHomA(M, N) \toHomA(M, N ′′) \to0
$$
and this is the definition of M being projective.
$\square$
---
## 4. Other resolutions: Tor
There are two other long exacts sequences in cohomology that I would like to discuss. For
this, I need to address questions that have hopefully been bothering you for a lecture or two:
• Can we use resolutions of M to compute TorA
n(M, N)?
• Can we use resolutions of N to compute Extn
A(M, N)?
Spoiler: Yes! In fact, we can use flat resolutions of M to compute TorA
n(M, N) and injective
resolutions of N to compute Extn
A(M, N). Note that projective resolutions of M are flat
resolutions, so we can use projective resolutions in either M or N to compute Tor. The
idea is as follows: suppose we want to compute TorA
n(M, N). Let ⟨Pn, dn⟩be a projective
resolution of N and suppose we are given a flat resolution ⟨Fn, d′
n⟩of M.
Tensor these

resolutions together, deleting the term M $\otimes$A N, as follows:
$$
...
$$

$$
...
$$

$$
...
$$

· · ·
$$
/ F1 \otimesA P1
$$

$$
/ F1 \otimesA P0
$$

$$
/ F1 \otimesA N
$$

/ 0
· · ·
$$
/ F0 \otimesA P1
$$

$$
/ F0 \otimesA P0
$$

$$
/ F0 \otimesA N
$$

/ 0
· · ·
$$
/ M \otimesA P1
$$

$$
/ M \otimesA P0
$$

/ 0

/ 0
Note that all the rows except the bottom one are exact, because the Fi are flat, and all the
columns except the rightmost one are exact, because the Pi are projective (hence flat). The
idea from here is to do some general diagram chasing to see that the homology of the bottom
row is isomorphic to the homology of the last column. For the full proof, see Section 3.3 of
Osborne.
**Proposition 4.1**. The A-module TorA
n(M, N) can be computed, up to isomorphism, by taking
a flat resolution of M, tensoring it with N (omitting the last nonzero term) and taking the
n-th homology of the resulting complex.
