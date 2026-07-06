# Lecture 06 — Interlude: Products and Coproducts in a category

*MATH 464, Rice University, Spring 2020 · January 27, 2020*

---

## 1. Interlude: Products and Coproducts in a category
The direct product and direct sum of A-modules are manifestations of very general categorical
constructions.
**Definition 1.1**. Let C be a category, and let {Xi}i\inI be a collection of objects.
The product
Q
i\inI Xi, if it exists, is an object of C, together with maps
pj :
Y
i\inI
Xi \toXj
j \inI
satisfying the following universal property: for any Y \inOb(C) endowed with maps fj : Y \toXj,
$$
there exists a unique map π: Y \toQ
i\inI Xi making the following diagram commute for all j \inI:
$$
Q
i\inI Xi
pj
/ Xj
Y
∃!
O
fj
;
A coproduct is defined analogously by reversing all the arrows.
**Definition 1.2**. Let C be a category, and let {Xi}i\inI be a collection of objects. The coproduct
`
i\inI Xi, if it exists, is an object of C, together with maps
$$
uj : Xj \to
$$
a
i\inI
Xi
j \inI
satisfying the following universal property: for any Y \inOb(C) endowed with maps fj : Xj \toY ,
there exists a unique map `
$$
i\inI Xi \toY making the following diagram commute for all j \inI:
$$
`
i\inI Xi
∃!

Xj
uj
o
fj
{
Y
You should check at home, but it should come to you as no surprise at this point, that products
and coproducts, if they exist, are unique up to unique isomorphism.
**Example 1.3**. In the category C = Sets, products are the usual cartesian products of sets, and
coproducts are disjoint unions.
**Example 1.4**. In the category C = Groups, products are the usual cartesian products of groups
(with component-wise multiplication), and coproducts are free products of groups.

**Example 1.5**. The above examples give us a silly way to construct categories without products and
coproducts. For example, the category of all finite groups cannot have coproducts, since coproducts
are always infinite, as long as two of the groups involved are not the trivial group.
**Example 1.6**. In the category C = A-Mod, products are the usual cartesian products of modules
that we have seen, and coproducts are direct sums.
**Example 1.7**. In the category C = Top, products are the usual cartesian products of topological
spaces (endowed with the product topology), and coproducts are disjoint unions (with the disjoint
union topology).
**Example 1.8**. In the category C = pt-Top, the product of two spaces (X, x0) and (Y, y0) is the
pointed space (X × Y, (x0, y0)). The coproduct is the wedge sum of the two spaces.
Many propositions you know can be phrased more categorically. For example, if (X, x0) and
(Y, y0) are pointed topological spaces, then we know from our first course in algebraic topology
that
$$
π1 (X \times Y, (x0, y0)) \simeq π1(X, x0) \times π1(Y, y0)
and π1 (X \veeY, x0 = y0) \simeq π1(X, x0) ∗π1(Y, y0)
$$
These two statements can be written succinctly as:
The functor π1 : pt-Top \toGroups preserves products and coproducts.
---
## 2. Exact sequences
Recall the philosophical point that the morphisms (or arrows) of a category should be as impor-
tant as its objects, because they tell us how objects are related or interact. Maps themselves can
interact. The fundamental concept here is that of exactness. Homology and cohomology theories
give us functorial invariants of objects; at heart, these invariants measure the failure of exactness.
**Definition 2.1**. A sequence of A-module homomorphisms
$$
\cdot \cdot \cdot \toMi-1
$$
fi-1
$$
---\toMi
$$
fi
$$
-\toMi+1 \to\cdot \cdot \cdot
$$
is exact at Mi if im fi-1 = ker fi. The sequence is exact if it is exact at every Mi.
Thus, to say that 0 \toM′ f-\toM is exact is to say that f is injective. To say that M
$$
g-\toM′′ \to0
$$
is exact is to say that g is surjective. To say that
(1)
$$
0 \toM′ f-\toM
g-\toM′′ \to0
$$
is exact is to say that f is injective, that g is surjective and that im f = ker g. An exact sequence
of the form (1) is called a short exact sequence. The play a special role, in part due to the following
useful observation.
Observation: Any exact sequence can be cut up into short exact sequences.

To see this, let
$$
\cdot \cdot \cdot \toMi-1
$$
fi-1
$$
---\toMi
$$
fi
$$
-\toMi+1 \to\cdot \cdot \cdot
be an exact sequence. Let Ni = \ker fi = \operatorname{im} fi-1. Then
0 \toNi \toMi \toNi+1 \to0
$$
is a short exact sequence. Conversely, these particular short exact sequences can be spliced into
the original long exact sequence.
**Proposition 2.2**. The sequence of A-modules
$$
0 \toM′
i-\toM
j-\toM′′
$$
is exact if and only if the induced sequence
$$
0 \toHomA(N, M′) i∗
-\toHomA(N, M)
$$
j∗
$$
-\toHomA(N, M′′)
$$
is exact for every A-module N.
*Proof.* (=$\Rightarrow$) First we show i∗is injective. Suppose that i∗(f) = i∗(g), i.e., i ◦f = i ◦g. Then
i(f(n)) = i(g(n)) for all n \inN. Since i is injective this means that f(n) = g(n) for all n \inN, so
f = g.
Next, let’s show that im i∗= ker j∗. For the inclusion im i∗\subseteqker j∗all we have to show is that
j∗◦i∗= 0. Now (j∗◦i∗)(f) = j∗(i∗(f)) = j ◦i ◦f = 0, where the last equality follows because
j ◦i = 0, by hypothesis. To show that ker j∗\subseteqim i∗, suppose that j∗(f) = 0, i.e., j ◦f = 0, so
that im f \subseteqker j = im i. Since i is injective, there is a well-defined map i-1 : im i \toM′. Let
$$
g := i-1 ◦f. Then i ◦g = f, so i∗(g) = f, which is to say that f \inim i∗.
$$
(⇐=) First, we show that i is injective. Suppose that i(m′) = 0. Take N = A and consider the two
maps f : A \toM′, 1 \mapstom′ and g: A \toM′, a \mapsto0. Then i∗(f) = i∗(g); since i∗is injective, we have
$$
f = g, so m′ = 0.
$$
Next we show that im i \subseteqker j. We know that j∗◦i∗(f) = 0 for every f \inHomA(N, M′). Take
$$
N = M′ and f = idM′. We get j ◦i(m′) = 0 for every m′ \inM′, so \operatorname{im} i \subseteqker j. Now we show the
$$
reverse inclusion. We know that ker j∗\subseteqim i∗for every A-module map f : N \toM. Suppose that
$$
j(m) = 0 and let f : A \toM be the map determined by 1 7\tom. Then j∗(f) = 0, so f = i∗(g) for
$$
some g: A \toM′. This means that f(1) = i(g(1)), which is to say that m = i(g(1)) so m \inim i.
$\square$
