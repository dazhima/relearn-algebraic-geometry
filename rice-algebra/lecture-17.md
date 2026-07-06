# Lecture 17 — Clean-up from last class

*MATH 464, Rice University, Spring 2020 · February 24, 2020*

---

## 1. Clean-up from last class:
Last time we saw that if M is a free A-module of rank n < ∞, then
r^
(M) = 0
for r > n.
The hypothesis that M is free over A is absolutely crucial, as the following example shows.
**Example 1.1**. Let A = Z[x, y], M = I = (x, y) as an ideal of A. Then M has rank 1 over
A, but it is not free! I claim that ∧2(I) \neq 0. More precisely, I claim that x ∧y \neq 0. To see
$$
this, define φ: I \times I \toA/I = \mathbb{Z} by
φ(ax + by, cx + dy) = (ad -bc) mod (x, y).
$$
Then φ is alternating and A-bilinear. Thus, it corresponds to the A-linear map
2^
$$
(I) \toA/I = \mathbb{Z}.
$$
that sends
$$
(ax + by) \wedge(cx + dy) 7\to(ad -bc) mod (x, y).
Since φ(x, y) = 1, it follows that x \wedgey \neq 0.
$$
---
## 2. A note on multiplication in the alternating algebra
I want to clarify a point about multiplication in the alternating algebra. We saw that if
we transpose two coordinates xi, xj in the product x1 ∧· · · ∧xr we pick up a negative sign,
i.e.,
$$
x1 \wedge\cdot \cdot \cdot \wedgexi \wedge\cdot \cdot \cdot \wedgexj \wedge\cdot \cdot \cdot \wedgexr = -x1 \wedge\cdot \cdot \cdot \wedgexj \wedge\cdot \cdot \cdot \wedgexi \wedge\cdot \cdot \cdot \wedgexr
$$
It is not true in general, however, that if x \inVr(M) and y \inVs(M) then x∧y = -y∧x. The
points is that to get all the components of y “across” x we need to make many transposition
moves. If we make an even number of transpositions, then we won’t pick up a negative sign!
**Exercise 2.1**. Show that if x \inVr(M) and y \inVs(M) then
$$
x \wedgey = (-1)rsy \wedgex.
$$
---
## 3. Differential forms in R3
The alternating algebra is extremely important in the study of calculus on Rn, and more
generally, on manifolds. We don’t have the time to make a deep digression, but I do want
to show you how the alternating algebra makes grad, div and curl seem very natural.
Let C∞(R3) be the ring of smooth functions on R3, so that an element of this ring is a
function f : R3 \toR with continuous partial derivatives of all orders. For a point p \inR3,
tangent space TpR3 is a three dimensional R-vector space with basis
(1)
 ∂
∂x

p
, ∂
∂y

p
, ∂
∂z

p

$$
If v = (v1, v2, v3) \inR3 then the element
$$
v1
∂
∂x

p
+ v2
∂
∂y

p
+ v3
∂
∂z

p
of Tp(R3) is what we know as the directional derivative along the direction v. A vector field
on R3 is a function that assigns a tangent vector to each point p \inR3, i.e., it is something
of the form
Xp = ax(p) ∂
∂x

p
+ ay(p) ∂
∂y

p
+ az(p) ∂
∂z

p
We say the vector field is smooth if ax, ay, az \inC∞(R3). The set of smooth vector fields
X(R3) is a module over C∞(R3). The dual module X(R3)∗is called the module of diﬀerential
1-forms of R3. It is a free C∞(R3) module of rank 3. We write

dx|p, dy|p, dz|p

for the dual basis to (1), and

dx, dy, dz

for the standard basis of X(R3)∗over C∞(R3).
For a smooth function f \inC∞(R3), we define the diﬀerential 1-form df \inX(R3)∗as follows:
(df)p(Xp) = Xpf
You can check, by unwinding the definitions, that
df = ∂f
∂xdx + ∂f
∂y dy + ∂f
∂z z
Now look at the alternating algebra V(X(R3)∗). We have
^
(X(R3)∗) =
0^
(X(R3)∗) $\oplus$
1^
(X(R3)∗) $\oplus$
2^
(X(R3)∗) $\oplus$
3^
(X(R3)∗)

where
0^
(X(R3)∗) = C∞(R3)
1^
$$
(X(R3)∗) = {fdx + gdy + hdz : f, g, h \inC∞(R3)}
$$
2^
$$
(X(R3)∗) = {fdy \wedgedz + gdz \wedgedx + hdx \wedgedy : f, g, h \inC∞(R3)}
$$
3^
$$
(X(R3)∗) = {fdx \wedgedy \wedgedz : f \inC∞(R3)}
$$
We now define an operator called exterior diﬀerentiation
d:
i^
(X(R3)∗) \to
i+1
^
(X(R3)∗)
by acting on the coeﬃcient functions as above. For example:
d:
0^
(X(R3)∗) \to
1^
(X(R3)∗)
is given by
$$
f 7\todf = fxdx + fydy + fzdz
$$
This derivative is known as “grad.” The operator
d:
1^
(X(R3)∗) \to
2^
(X(R3)∗)
is aﬀectionately known as “curl”:
$$
d(fdx + gdy + hdz) = df \wedgedx + dg \wedgedy + dh \wedgedz
= (fxdx + fydy + fzdz) \wedgedx
$$
+ (gxdx + gydy + gzdz) ∧dy + (hxdx + hydy + hzdz) ∧dz
$$
= (gx -fy)dx \wedgedy + (hy -gz)dy \wedgedz + (fz -hx)dz \wedgedx
$$
Finally, the operator
d:
2^
(X(R3)∗) \to
3^
(X(R3)∗)
is aﬀectionately known as “div”:
$$
d(fdy \wedgedz + gdz \wedgedx + hdx \wedgedy) = df \wedgedy \wedgedz + dg \wedgedx \wedgedz + dh \wedgedx \wedgedy
= (fxdx + fydy + fzdz) \wedgedy \wedgedz
+ (gxdx + gydy + gzdz) \wedgedz \wedgedx
+ (hxdx + hydy + hzdz) \wedgedx \wedgedy
= (fx + gy + hz)dx \wedgedy \wedgedz
$$

Vector Calculus is then summarized by saying that the following diagram “commutes”:
V0(X(R3)∗)
R

d
“grad”
/ V1(X(R3)∗)
R

d
“curl”
/ V2(X(R3)∗)
R

d
“div”
/ V3(X(R3)∗)
R

$$
{oriented points}
{oriented curves}
$$
∂
o
$$
{oriented surfaces}
$$
∂
o
$$
{oriented solids}
$$
∂
o
Here the vertical arrows are integration maps: for example, the integral of a function f \in
V0(X(R3)∗) along a pair of oriented points {a, b} is f(b) -f(a). Thus the commutativity of
the left-most square is just the fundamental theorem of line integrals for curves in R3; the
commutativity of the middle square is just the Stokes’ theorem, and the commutativity of
the right-most square is just the divergence theorem.
If we repeat this exercise for R1 instead of R3 we end up with a single commutative square
encoding the fundamental theorem of Calculus. If we do it for R2 we get two squares: the
left one encodes the fundamental theorem of line integrals for the plane; the right one is
known as Green’s theorem.
For a more leisurely walk through this material, done in greater generality, I recommend:
L. Tu An Introduction to Manifolds, Springer (New York), 2008.
You can download it for free (and legally!) on the Rice network through www.springerlink.com
