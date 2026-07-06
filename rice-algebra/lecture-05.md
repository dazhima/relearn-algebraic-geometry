# Lecture 05 — Direct product and sum of modules

*MATH 464, Rice University, Spring 2020 · January 24, 2020*

---

## 1. Direct product and sum of modules
From Math 463, you are probably familiar with the notion of cartesian product of A-modules
M × N and the direct sum of A-modules M $\oplus$N. In fact, you may wonder what the diﬀerence is.
At first sight, it appears to just be notation. However, these two constructions are manifestations
of more general categorical notions that don’t usually coincide.
The categorical point of view is extremely powerful here, so let me give you the correct definitions
of these objects.
**Definition 1.1**. Let M and N be two A-modules. The direct product M × N is an A-module,
together with two projections
$$
i: M \times N \toM,
j : M \times N \toN
$$
satisfying the following universal property: given any A-module T, together with maps p1 : T \toM
and p2 : T \toN, there exists a unique map T \toM × N making the following diagram commute.
T
p1

p2

∃!

M × N
i
z
j
#
M
N
In other words, the map
$$
HomA(T, M \times N) \toHomA(T, M) \times HomA(T, N)
$$
f \mapsto(i ◦f, j ◦f)
is a bijection of sets.
It is not clear from the definition that direct products exist! However, if you take the definition
you know, you can check that this set satisfies the universal property. Concretely, let
$$
S := {(m, n) : m \inM, n \inN}
and let i: S \toM be the map (m, n) 7\tom and j : S \toN be the map (m, n) 7\ton. Now suppose
$$
that T is an A-module with projections p1 : T \toM and p2 : T \toN. Then there is exactly one
map φ: T \toS such that p1 = i ◦φ and p2 = j ◦φ, namely φ(t) := (p1(t), p2(t)). Thus S is a direct
product.
**Proposition 1.2**. The direct product of two A-modules is unique up to unique isomorphism.

*Proof.* Suppose that T and T ′ both satisfy the universal property to be the direct product of two
$$
A-modules M and N. In particular, we have maps p1 : T \toM, p2 : T \toN, p′
1 : T \toM, and
$$
p′
2 : T \toN. Since T is a direct product, we know there is a unique map of A-modules φ: T ′ \toT
making the following diagram commute:
T ′
p′

p′

∃!

T
p1
~
p2

M
N
Since T ′ is a direct product we also have a map ψ: T \toT ′ making the analogous diagram commute.
The map φ ◦ψ: T \toT is a map of A modules that commutes with p1 : T \toM. But since T is a
direct product, there is a unique map T \toT that makes the following diagram commute
T
p1

p2

∃!

T
p1
~
p2

M
N
namely, the identity map! So φ ◦ψ = idT . Similarly, we can show that ψ ◦φ = idT ′. Thus T and
T ′ are uniquely isomorphic, as desired.
$\square$
Let me illustrate the power of the definition in a simple example (which is overkill, but instruc-
tive). Suppose you suspect that Z/6Z \simeq Z/2Z × Z/3Z as Z-modules, i.e., as abelian groups. Here
we’re implicitly thinking of the maps
$$
i: \mathbb{Z}/6Z \toZ/2Z
j : \mathbb{Z}/6Z \toZ/3Z
$$
m mod 6Z \mapstom mod 2Z
m mod 6Z \mapstom mod 3Z
Now suppose there exists an abelian group T together with homomorphisms p1 : T \toZ/2Z and
$$
p2 : T \toZ/3Z. Define φ: T \toZ/6Z by the rule
$$
φ(t) =



















$$
if p1(t) = 0 and p2(t) = 0,
if p1(t) = 1 and p2(t) = 1,
if p1(t) = 0 and p2(t) = 2,
if p1(t) = 1 and p2(t) = 0,
if p1(t) = 0 and p2(t) = 1,
if p1(t) = 1 and p2(t) = 2.
$$
Check that this is a homomorphism of Z-modules. Then, by definition we have p1 = i ◦φ and
p2 = j ◦φ. Also, this is the only map that’ll do the job (check this!). Voil`a! We don’t have to
check anything else! We are done! I agree there are easier ways of doing this, but the idea is very
powerful: we just had to check a bijection of sets!
**Definition 1.3**. Let M and N be two A-modules. The direct sum M $\oplus$N is an A-module, together
with two maps
$$
i: M \toM \oplusN,
j : N \toM \oplusN
$$

satisfying the following universal property: given any A-module T, together with maps f : M \toT
and g: N \toT, there exists a unique map M $\oplus$N \toT making the following diagram commute.
T
M $\oplus$N
∃!
O
M
i
:
f
D
N
g
Z
j
c
In other words, the map
$$
HomA(M \oplusN, T) \toHomA(M, T) \times HomA(N, T)
$$
φ \mapsto(φ ◦i, φ ◦j)
is a bijection of sets.
The set
$$
S := {(m, n) : m \inM, n \inN}
$$
that we used to show that direct products exist will also do the job here, but the additional data of
$$
the maps associated to S is diﬀerent! We take i: M \toS to be m 7\to(m, 0) and j : N \toS to be
$$
n \mapsto(0, n).
**Proposition 1.4**. The direct sum of two A-modules is unique up to unique isomorphism.
*Proof.* Exercise! Do this out to get practice with the definitions.
$\square$
Direct products and sums of finitely many A-modules are defined analogously. As in the
case of two A-modules, their underlying sets have the same cardinality, though the accompanying
maps go in opposite directions.
If we have an arbitrary collection of A-modules {Mi}i\inI, then we can define the direct product
and the direct sum analogously, but now their underlying sets will be diﬀerent. An element in
L
i\inI Mi consists of a tuple (xi)i\inI where almost all the xi \inMi are zero, whereas in Q
i\inI Mi there
is no restriction on the xi. Please check this by showing that the sets I just described satisfy the
right universal property.
