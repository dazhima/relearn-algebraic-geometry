# Lecture 18 — Localization

*MATH 464, Rice University, Spring 2020 · February 26, 2020*

---

## 1. Localization
We turn now to localization1. We’ve spent a lot of time trying to build new modules
from old modules. Now we’re going to shift focus and fix a particular module and try to
understand its internal behavior in a local way. The impetus for localization (at least that I
know of) is algebro-geometric: the idea is to study the behavior of an aﬃne variety (so Spec
of a finitely generated, nilpotent free k-algebra) around a particular point (a prime ideal in
the spectrum) by looking at the ring of functions around that point. More on this later.
Let’s plunge into the construction of localization.
Hopefully you are familiar with the construction of Q as the field of fractions of Z: Q is
obtained by putting an equivalence relation on Z × Z \ {0}, as follows:
$$
(a, b) ∼(c, d) \Longleftrightarrowad -bc = 0,
$$
and setting Q =
$$
\mathbb{Z} \times \mathbb{Z} \ {0}
$$

∼. We write a/b for the equivalence class of (a, b). We then
define addition and multiplication by:
a
b + c
$$
d := ad + bc
$$
cd
a
b · c
$$
d := ac
$$
bd,
and check that these operations are well-defined (i.e., they don’t depend on the choice of
representatives). These operations give Q the structure of a ring and there is a canonical
$$
map \mathbb{Z} \toQ sending a 7\toa/1.
$$
The same procedure can be used to construct the field of fractions of an integral do-
main: the “no (non-zero) zero-divisors” hypothesis is crucial for proving transitivity of the
equivalence relation. There is a way out of this excessively restrictive hypothesis, as follows.
Let A be a ring (commutative, with unit, as usual). A multiplicatively closed subset S \subseteqA
is a subset such that 1 \inS and S is closed under multiplication. Define a relation on A × S
by
$$
(a, s) ∼(b, t) \Longleftrightarrow(at -bs)u = 0 for some u \inS.
$$
1You should read Chapter 3 of Atiyah-MacDonald. Also, Chapter 2 of Eisenbud is very helpful. His notation
will diﬀer from our slightly, but we’ll touch on all the same points, if only in a slightly diﬀerent order.

The relation is clearly reflexive and symmetric. Suppose that (a, s) ∼(b, t) and (b, t) ∼(c, u).
Then there are v, w \inS such that
$$
(at -bs)v = 0
and
(bu -ct)w = 0.
$$
Eliminating b we obtain
$$
0 = atvuw -ctwsv = (au -cs)tvw.
$$
Since S is multiplicatively closed, it follows that tvw \inS and so (a, u) ∼(c, s). We write
S-1A for the set of equivalence classes under this relation, and we write a/s for the image
$$
of (a, s) in S-1A. We define addition and multiplication on S-1A as above:
$$
a
s + b
$$
t := at + bs
$$
st
a
s · b
$$
t := as
$$
bt .
You should check that these operations are well-defined. They give S-1A the structure of a
commutative ring with unit. Note that there is a ring homomorphism
$$
f : A \toS-1A
$$
a \mapstoa
1.
**Example 1.1**. If A is an integral domain and S = A\{0}, then S-1A is the field of fractions
of A (e.g., A = Z above).
**Example 1.2**. Let p be a prime ideal of A. Then S := A -p is a multiplicatively closed
subset (by definition of prime ideal!). We write Ap instead of S-1A in this case. For a
concrete example, take A = Z and p = (p). Then Ap consists of rational numbers m/n such
that p does not divide n.
The elements of Ap of the form a/s with a \inp form a prime ideal of Ap; call this ideal m.
If b/t /\inm then b /\inp which means that b \inS, so b/t is a unit in Ap. Hence, if a ⊈m is an
ideal of Ap, then a contains a unit and is therefore equal to all of Ap. This means that m is
the only maximal ideal of Ap, i.e., Ap is a local ring.
When A = Z and p = (p), the ideal m consists of rational numbers m/n such that p | m
but p ∤n. When A = k[t1, . . . , tn], where k is an infinite field, the ring Ap consists of rational
$$
functions f/g such that g \notinp.
$$
**Example 1.3**. Let f \inA and set S = {f n}n≥0. We write Af for S-1A in this case. If A = Z
and 0 \neq f \inZ, then Af consists of all rational numbers whose denominator is a power of f.
Elements of S in S-1A are units: this observation can be turned into a universal property.
**Proposition 1.4**. Let g: A \toB be a ring homomorphism such that g(s) is a unit in B for
all s \inS. Then g factors uniquely through f, i.e., there exists a unique ring homomorphism
$$
h: S-1A \toB such that g = h ◦f.
$$
*Proof.* For existence, set h(a/s) = g(a)g(s)-1. This is a homomorphism provided it is well-
defined. Suppose that a/s = a′/s′. Then there exists t \inS such that (as′ -a′s)t = 0.

Applying g we see that
$$
(g(a)g(s′) -g(a′)g(s))g(t) = 0.
$$
Since g(t) is a unit in B, we have g(a)g(s′) -g(a′)g(s) = 0, and this is all we need.
$$
For uniqueness, note that g(a) = h ◦f(a) = h(a/1), and if s \inS then h(1/s) =
h((s/1)-1) = h(s/1)-1 = g(s)-1, so that h(a/s) = h(a/1) \cdot h(1/s) = g(a)g(s)-1, so h is
$$
determined by g.
$\square$
---
## 2. Localization of Modules
Let M be an A-module and let S \subseteqA be a multiplicatively closed subset. We can define
the localization of M at S just like we did for rings: define a relation on M × S by
$$
(m, s) ∼(m′, s′) \Longleftrightarrowt(ms′ -m′s) = 0 for some t \inS
$$
As before, this is an equivalence relation; write S-1M for the set of equivalence classes, and
$$
let m/s stand for (m, s). The set S-1M has the structure of an S-1A-module with the
$$
obvious definitions of addition and scalar multiplication.
$$
Notation: We write Mp when S = A -p and Mf when S = {f n}n\geq0
$$
