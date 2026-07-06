# Lecture 36 — Complexes and projective resolutions

*MATH 464, Rice University, Spring 2020 · April 22, 2020*

---

## 1. Complexes and projective resolutions
Recall a sequence of maps of A-modules
M ′
$$
f-\toM
g-\toM ′′
is a complex if \operatorname{im} f \subseteqker g. The homology of the complex at M is the group H := \ker g/ \operatorname{im} f.
$$
This group, by definition, provides a measure of the failure of exactness of a complex. The
notions of projective, injective and flat are all defined in terms of exactness, so homology
groups of complexes can help measure the extent to which a general module can fail of satisfy
one of these three properties.
An arrow between two complexes is a diagram of the form
M ′
f
/
φ

M
g
/
ψ

$$
M ′′
$$
η

N ′
f′
/ N
g′
$$
/ N ′′
where the squares commute. Let H = \ker g/ \operatorname{im} f and H′ = \ker g′/ \operatorname{im} f ′. The above map of
$$
chain complexes induces a map in homology
$$
ψ∗: H \toH′
m + \operatorname{im} f 7\toψ(m) + \operatorname{im} f ′
$$
Note that this map is well-defined, because
$$
• if m \inker g then g′(ψ(m)) = 0, so ψ(m) \inker g′, and
• if m1 + \operatorname{im} f = m2 + \operatorname{im} f then m1 -m2 = f(m′) for some m′ \inM ′, and applying ψ
$$
we get
$$
ψ(m1) -ψ(m2) = ψ(f(m′)) = f ′(φ(m′)),
so ψ(m1) + \operatorname{im} f ′ = ψ(m2) + \operatorname{im} f ′.
$$
---
## 2. Homotopies
Note that we did not discuss this section in class, but it is necessary if you want to complete
any of the proofs that we also skipped in class.
It is possible that two maps between complexes give rise to the same map in homology.
One way in which this can happen is if we have a homotopy: Suppose that we have two

maps between complexes:
M ′
f
/
φ
φ′

M
g
/
ψ
ψ′

$$
M ′′
$$
η
η′

N ′
f′
/ N
g′
$$
/ N ′′
$$
A homotopy is a pair of maps ∆1 : M \toN ′ and ∆2 : M ′′ \toN such that
$$
ψ -ψ′ = f ′ ◦∆1 + ∆2 ◦g
$$
Here’s the diagram we are looking at:
M ′
f
/
φ
φ′

M
∆1
w
g
/
ψ
ψ′

$$
M ′′
$$
∆2
w
η
η′

N ′
f′
/ N
g′
$$
/ N ′′
$$
THIS DIAGRAM DOES NOT COMMUTE!
If there is a homotopy, then the induced maps in homology ψ∗, ψ′
$$
∗: H \toH′ coincide since
ψ∗(m + \operatorname{im} f) = ψ(m) + \operatorname{im} f ′
= ψ′(m) + f ′ ◦∆1(m) + ∆2 ◦g(m) + \operatorname{im} f ′
= ψ′(m) + f ′ ◦∆1(m) + 0 + \operatorname{im} f ′
= ψ′(m) + \operatorname{im} f ′
= ψ′
$$
∗(m + im f)
One reason homotopies are great is that an additive functor (i.e., a functor F such that
F(f + g) = F(f) + F(g)) takes homotopies to homotopies, so the corresponding maps in
homology F(ψ∗) and F(ψ′
∗) also coincide.
---
## 3. Resolutions
We are going to use projective modules to construct certain complexes that will allow us
to measure the extent to which a module fails to be flat. So let N be an A-module (as usual,
A is a commutative ring with unit). A projective resolution of N is an exact sequence of the
form
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
such that the modules Pi are all projective.
Such resolutions exist: Since the category
A-Mod of A-modules has enough projectives, we know there is a projective module P0
such that
P0
$$
π-\toN \to0
$$
is exact. Now use again the fact that A-Mod has enough projectives, to conjure up a
projective module P1 such that
P1
d1
$$
-\toker(π) \to0
$$

is exact. Keep going: there is a projective module P2 such that
P2
d2
$$
-\toker(d1) \to0
$$
is exact, etc. We write ⟨Pn, dn⟩for the projective resolution of N above.
**Proposition 3.1**. Let N and N ′ be A-modules, and let ⟨Pn, dn⟩and ⟨P ′
n, d′
n⟩be projective
resolutions of these modules, respectively. Then, for any φ \inHomA(N, N ′) there exist fillers
$$
{φn : Pn \toP ′
$$
n}n≥0 such that the following diagram commutes:
· · ·
/ Pn
dn /
φn

Pn-1
$$
dn-1 /
$$
φn-1

· · ·
/ P1
d1
/
φ1

P0
π
/
φ0

N
/
φ

· · ·
$$
/ P ′
$$
n
d′
$$
n / P ′
$$
n-1
d′
$$
n-1 / \cdot \cdot \cdot
/ P ′
$$
d′
$$
/ P ′
$$
π′
$$
/ N ′
$$
/ 0
$$
Moreover, if {φ′
n : Pn \toP ′
$$
n}n≥0 is another collection of fillers that makes the diagram com-
mute, then φn and φ′
$$
n are homotopic, i.e., there exist maps ∆n : Pn \toP ′
$$
n+1 (with the under-
standing that ∆-1 ≡0), such that
$$
φn -φn′ = dn+1∆n + ∆n-1dn
$$
*Proof.* To define φ0 we use the fact that P0 is projective, so we get a filler
P0
φ0
~
φ ◦π

P ′
π′
$$
/ N ′
$$
/ 0
Suppose we have defined φ0, . . . , φn. I claim that φn(im dn+1) \subseteqker d′
$$
n = \operatorname{im} d′
$$
n+1. To see
$$
this, suppose that x \inim dn+1. Then dn(x) = 0, so
0 = φn-1(dn(x)) = d′
$$
n(φn(x))
$$
and φn(x) \inker(d′
$$
n). Now use the fact that Pn+1 is projective to get a filler for the diagram
Pn+1
φn+1
z
φn ◦dn+1

P ′
n+1
d′
$$
n+1/ \operatorname{im}(d′
$$
n+1)
/ 0
This shows the existence of the map between the two projective resolutions.
$$
Now suppose that {φn} and {φ′
n} give two sets of fillers. Define ∆-1 : N \toP ′
$$
0 to be the
zero map. We have the diagram
P1
d1
/
φ1
φ′
1 
P0
π
/
φ0
φ′
0 
N
∆-1
x
φ

P ′
d′
$$
/ P ′
$$
π′
$$
/ N ′
$$

$$
Now π′(φ0 -φ′
0) = 0, so \operatorname{im}(φ0 -φ′
0) \subseteqker π′ = \operatorname{im} d′
$$
---
## 1. Since P0 is projective, there is a filler
for the diagram
P0
∆0
|
$$
φ0-φ′
$$

P ′
d1 / im(d1)
/ 0
Now note that
$$
φ0 -φ′
0 = d1∆0 + ∆-1π.
$$
Now suppose we have constructed ∆0, . . . , ∆n. I’ll leave it as an exercise to you to complete
the proof...
$\square$
---
## 4. Tor
As usual, A denotes a commutative ring with unit. Let M an A-module. We will define
a series of functors
TorA
$$
n(M, •): A-Mod \toA-Mod
Such that M \otimesA • \simeq TorA
$$
0 (M, •) as functors on A-modules. The functor TorA
1 (M, •) will
measure the failure of exactness of M $\otimes$A •.
First, we define the functor on objects. So let N be an A-module. Let
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
(Note this is a complex since M $\otimes$A • is a functor: it takes compositions to compositions,
so if two maps compose to the zero map in the original category, they will also compose to
zero after you apply the functor). Define
TorA
$$
n(M, N) := \ker(idM \otimesdn)/ \operatorname{im}(idM \otimesdn+1).
$$
Of course, this definition only makes sense if the quotient does not depend on the projective
resolution of N chosen.
**Proposition 4.1**. The A-module TorA
n(M, N) is independent, up to isomorphism, of the
chosen projective resolution of N.
We skipped this proof in lecture, but here it is in case you’re interested.

*Proof.* Let ⟨Pn, dn⟩and ⟨P ′
n, d′
$$
n⟩be projective resolutions of N. The map id: N \toN gives
$$
rise to a collection of fillers
· · ·
/ Pn
dn /
φn

Pn-1
$$
dn-1 /
$$
φn-1

· · ·
/ P1
d1
/
φ1

P0
π
/
φ0

N
/
id

· · ·
$$
/ P ′
$$
n
d′
$$
n / P ′
$$
n-1
d′
$$
n-1 / \cdot \cdot \cdot
/ P ′
$$
d′
$$
/ P ′
$$
π′
/ N
/ 0
and we also get fillers in the opposite direction:
· · ·
$$
/ P ′
$$
n
d′
n /
ψn

P ′
n-1
d′
$$
n-1 /
$$
ψn-1

· · ·
$$
/ P ′
$$
d′
/
ψ1

P ′
π′
/
ψ0

N
/
id

· · ·
/ Pn
$$
dn / Pn-1
dn-1 / \cdot \cdot \cdot
$$
/ P1
d1
/ P0
π
/ N
/ 0
Now stack these two diagrams on top of each other:
· · ·
/ Pn
dn /
φn

Pn-1
$$
dn-1 /
$$
φn-1

· · ·
/ P1
d1
/
φ1

P0
π
/
φ0

N
/
id

· · ·
$$
/ P ′
$$
n
d′
n /
ψn

P ′
n-1
d′
$$
n-1 /
$$
ψn-1

· · ·
$$
/ P ′
$$
d′
/
ψ1

P ′
π′
/
ψ0

N
/
id

· · ·
/ Pn
$$
dn / Pn-1
dn-1 / \cdot \cdot \cdot
$$
/ P1
d1
/ P0
π
/ N
/ 0
$$
We see that {ψn◦φn}n\geq0 is a collection of fillers for the map id: N \toN. But so is {idPn}n\geq0,
$$
so we conclude that the maps ψn ◦φn and idPn are chain homotopic. This means there are
$$
maps ∆n : Pn \toPn+1 such that
ψn ◦φn -idPn = ∆n-1 ◦dn + dn+1 ◦∆n
$$
Tensor being additive and respecting compositions, we obtain
$$
idM \otimesψn ◦idM \otimesφn -idM \otimesidPn = idM \otimes∆n-1 ◦idM \otimesdn + idM \otimesdn+1 ◦idM \otimes∆n
$$
ans so idM $\otimes$ψn ◦idM $\otimes$φn and idM $\otimes$idPn are homotopic! That means they induce the same
map in homology, i.e.,
$$
(idM \otimesψn)∗◦(idM \otimesφn)∗= (idM \otimesidPn)∗= idTorA
$$
n (M,N)
Reversing the roles of ⟨Pn, dn⟩and ⟨P ′
n, d′
n⟩we get
$$
(idM \otimesφn)∗◦(idM \otimesψn)∗= (idM \otimesidPn)∗= idTorA
$$
n (M,N)
We conclude the maps (idM $\otimes$φn)∗and (idM $\otimes$ψn)∗are inverses of each other.
$\square$

**Example 4.2**. We compute TorZ/4Z
n
$$
(\mathbb{Z}/2Z, \mathbb{Z}/2Z). We need to take a projective resolution
$$
of Z/2Z as a Z/4Z-module. I claim that the following exact sequence does the job:
$$
\cdot \cdot \cdot \toZ/4Z
$$
×2
$$
-\toZ/4Z \to\cdot \cdot \cdot \toZ/4Z
$$
×2
$$
-\toZ/4Z
π-\toZ/2Z \to0
$$
That the sequence is exact is obvious, and Z/4Z is a free (hence projective) Z/4Z-module.
$$
Now we have to tensor the map \times2: \mathbb{Z}/4Z \toZ/4Z with \mathbb{Z}/2Z \timesZ/4Z •. We get
idZ/2Z \otimes(\times2): \mathbb{Z}/2Z \timesZ/4Z \mathbb{Z}/4Z \toZ/2Z \timesZ/4Z \mathbb{Z}/4Z.
$$
I claim that if we identify Z/2Z×Z/4ZZ/4Z with Z/2Z, then the above map becomes the zero
$$
map! That’s because the identification converts a\otimesb to ab \inZ/2Z so the map a\otimesb 7\toa\otimes2b
$$
takes ab to 2ab = 0. So after tensoring we have the complex
$$
\cdot \cdot \cdot \toZ/2Z
0-\toZ/2Z \to\cdot \cdot \cdot \toZ/2Z
0-\toZ/2Z \to0
Conclusion: TorZ/4Z
$$
n
$$
(\mathbb{Z}/2Z, \mathbb{Z}/2Z) \simeq \mathbb{Z}/2Z for all n \geq0.
$$
**Example 4.3**. Note, as promised, that TorA
$$
0 (M, N) \simeq M \otimesA N. This is the reason we omit
$$
the term M $\otimes$A N from the tensored projective resolution.
We have yet to say what the functor TorA
n(M, •) does to morphisms in A-Mod. Suppose
$$
that φ: N \toN ′ is a morphism of A-modules.
$$
Let ⟨Pn, dn⟩and ⟨P ′
n, d′
n⟩be projective
resolutions of N and N ′, respectively. We get a collection of fillers {φn}n≥0 making the
following diagram commute:
· · ·
/ Pn
dn /
φn

Pn-1
$$
dn-1 /
$$
φn-1

· · ·
/ P1
d1
/
φ1

P0
π
/
φ0

N
/
φ

· · ·
$$
/ P ′
$$
n
d′
$$
n / P ′
$$
n-1
d′
$$
n-1 / \cdot \cdot \cdot
/ P ′
$$
d′
$$
/ P ′
$$
π′
$$
/ N ′
$$
/ 0
Applying M $\otimes$A • and omitting the last terms, we obtain a map of complexes
· · ·
$$
/ M \otimesA Pn
idM \otimesdn/
$$
idM $\otimes$φn

$$
M \otimesA Pn-1
idM \otimesdn-1 /
idM \otimesφn-1
$$

· · ·
$$
/ M \otimesA P1
idM \otimesd1/
$$
idM $\otimes$φ1

M $\otimes$A P0
/
idM $\otimes$φ0

· · ·
$$
/ M \otimesA P ′
$$
n
$$
idM \otimesd′
n/ M \otimesA P ′
$$
n-1
$$
idM \otimesd′
n-1 / \cdot \cdot \cdot
/ M \otimesA P ′
idM \otimesd′
1/ M \otimesA P ′
$$
/ 0
And this is all we need to define a map in homology:
$$
(idM \otimesφn)∗: TorA
$$
n(M, N) \toTorA
n(M, N ′)
Exercise: show that this map is independent of the projective resolutions chosen!
