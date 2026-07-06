# Lecture 10 — More on tensor products

*MATH 464, Rice University, Spring 2020 · February 5, 2020*

---

## 1. More on tensor products
Recall the construction and universal property of the tensor product M $\otimes$A N of two A-modules
M and N. As our examples at the end of last lecture showed, we now have a way to take two
k-vector spaces and construct a product vector space, and the examples showed that the dimension
is multiplicative. This happens in general: if the set {xi}i\inI generates M and {yj}j\inJ generates
N, then you can check that the set {xi $\otimes$yj}i\inI,j\inJ generates M $\otimes$A N. Moreover, if I and J are
both finite, this shows that the tensor product of two finitely generated modules is also finitely
generated.
### 1.1. Tensoring more than 2-modules at a time. Let M1, . . . , Mr be A-modules. I claim there
$$
is an A-module M1 \otimesA \cdot \cdot \cdot \otimesA Mr, together with an A-multilinear map
g: M1 \times \cdot \cdot \cdot \times Mr \toM1 \otimesA \cdot \cdot \cdot \otimesA Mr
$$
such that for any multilinear map f : M1 × · · · Mr \toP there exists a unique map of A-modules
$$
M1 \otimesA \cdot \cdot \cdot \otimesA Mr \toP making the following diagram commute:
$$
M1 × · · · Mr
f
/
g

P
$$
M1 \otimesA \cdot \cdot \cdot \otimesA Mr
$$
∃!
This property tells us there is bijection
$$
{A-multilinear maps M1 \times \cdot \cdot \cdot \timesA Mr \toP} \leftarrow\toHomA(M1 \otimesA \cdot \cdot \cdot \otimesA Mr, P)
$$
The existence can be shown by constructing an appropriate free module and quotienting out a
submodule that captures the A-multilinearity, just like the case of two modules.
### 1.2. Associativity of tensor products. Let M, N and P be A-modules. I claim there are maps
$$
(M \otimesA N) \otimesA P
f-\to
M \otimesA N \otimesA P
g-\to
M \otimesA (N \otimesA P)
(x \otimesy) \otimesz 7\to
x \otimesy \otimesz 7\to
x \otimes(y \otimesz)
$$
Let’s make sure they are really there though.
$$
First we construct f. Fix z \inP, and consider the map M \times N \toM \otimesA N \otimesA P given by
(x, y) 7\tox \otimesy \otimesz. This map is bilinear, so it induces a map fz : M \otimesA N \toM \otimesA N \otimesA P
given by x \otimesy 7\tox \otimesy \otimesz. Now consider the map (M \otimesA N) \times P \toM \otimesA N \otimesA P given
$$

by (t, z) \mapstofz(t). You should check that this is an A-bilinear map. Thus it gives rise to a map
$$
f : (M \otimesA N) \otimesA P \toM \otimesA N \otimesA P, which takes (x \otimesy) \otimesz to x \otimesy \otimesz, as claimed.
$$
Now we construct g. This is easier: I claim that the map M ×N ×P \toM $\otimes$A (N $\otimes$A P) sending
$$
(x, y, z) to x \otimes(y \otimesz) is A-trilinear, and thus we get a map M \otimesA N \otimesA P \toM \otimesA (N \otimesA P) that
sends x \otimesy \otimesz to x \otimes(y \otimesz).
$$
To show associativity, we assert the existence of maps
$$
f′ : M \otimesA N \otimesA P \to(M \otimesA N) \otimesA P
x \otimesy \otimesz 7\to(x \otimesy) \otimesz
g′ : M \otimesA (N \otimesA P) \toM \otimesA N \otimesA P
(x \otimesy) \otimesz 7\tox \otimesy \otimesz
$$
which are clearly inverses of f, g, respectively.
There are many other properties that tensor products satisfy. I invite you to write down the
proofs for them. We’ve done the hardest one (associativity).
**Proposition 1.1**. Let M, N and P be A-modules. Then
$$
(1) The map M \otimesA N \toN \otimesA M, defined by x \otimesy 7\toy \otimesx (extended by A-linearity), is an
$$
isomorphism.
$$
(2) The map (M \oplusN) \otimesA P \to(M \otimesA P) \oplus(N \otimesA P), defined by (x, y) \otimesz 7\to(x \otimesz, y \otimesz)
$$
(extended by A-linearity), is an isomorphism.
$$
(3) The map A\otimesAM \toM, defined by a\otimesx 7\toax (extended by A-linearity), is an isomorphism.
$$
There is also an associativity property for tensor products over diﬀerent rings. Suppose that
A and B are rings (commutative, with unit). Let M be an A-module and let P be a B-module.
Suppose that N is an (A, B)-bimodule, i.e., N is a left A-module and a right B-module, and these
structures are compatible in the sense that (ay)b = a(yb) for any y \inN, a \inA and b \inB. Then
$$
(M \otimesAN) is a B-module via (x\otimesy)\cdotb := x\otimesyb and (N \otimesB P) is an A-module via a\cdot(y\otimesz) := ay\otimesz,
$$
and there is an isomorphism of Z-modules
$$
(M \otimesA N) \otimesB P \simeq M \otimesA (N \otimesB P).
$$
### 1.3. Restriction and Extension of Scalars. Let f : A \toB be a ring homomorphism. Let N
be a B-module. Using the map f, we can give N an A-module structure, as follows:
$$
a \cdot n := f(a) \cdot n
a \inA, n \inN.
$$
The resulting A-module is said to be obtained by restriction of scalars, and is usually denoted AN.
In many situations, f is an injective map (e.g., the natural inclusion R \toC), hence the name of
the operation.
Tensor product allows us to give a counterpart to restriction of scalars, called extension of
scalars: suppose that M is an A-module. The map f makes B an A-module as well. The module
$$
MB := B \otimesA M is the extension of scalars. It is a B-module via b \cdot (b′ \otimesx) := bb′ \otimesx. For example,
$$
if V is an R-vector space, then VC = C $\otimes$R V is a C-vector space. Note that dimR VC = 2 dimR V .
If M is finitely generated over A then MB is finitely generated over B: if {xi}n
i=1 generated M
$$
as an A-module, then {1 \otimesxi}n
$$
i=1 generates MB as a B-module.
