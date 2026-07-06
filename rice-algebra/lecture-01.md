# Lecture 01 — Categories

*MATH 464, Rice University, Spring 2020 · January 13, 2020*

---

## 1. Categories

In this course we'll adopt a utilitarian point of view when it comes to category theory: while many people study it for its own sake, we'll think of category theory as a clean, organizing framework for a lot of modern mathematics, that allows us to relate seemingly different parts of the subject.

**Definition 1.1.** A *category* $\mathcal{C}$ consists of

- a collection of objects $\mathrm{Ob}(\mathcal{C})$,
- a set $\mathrm{Mor}(A, B)$ for every two objects $A, B \in \mathrm{Ob}(\mathcal{C})$,
- a *composition law*

$$\circ : \mathrm{Mor}(A, B) \times \mathrm{Mor}(B, C) \to \mathrm{Mor}(A, C)$$

for every three objects $A, B, C \in \mathrm{Ob}(\mathcal{C})$. We write $f \circ g$ instead of $\circ(g, f)$.

These objects and morphisms satisfy the following properties:

1. $\mathrm{Mor}(A, B) \cap \mathrm{Mor}(A', B') = \emptyset$ unless $A = A'$ and $B = B'$.
2. For every $A \in \mathrm{Ob}(\mathcal{C})$ there is a morphism $\mathrm{id}_A \in \mathrm{Mor}(A, A)$ which acts as the identity on the right on $\mathrm{Mor}(A, B)$ and as the identity on the left on $\mathrm{Mor}(B, A)$. For example, $f \circ \mathrm{id}_A = f$ for any $f \in \mathrm{Mor}(A, B)$.
3. Composition is associative: given $f \in \mathrm{Mor}(A,B)$, $g \in \mathrm{Mor}(B,C)$, $h \in \mathrm{Mor}(C,D)$, we have $(h \circ g) \circ f = h \circ (g \circ f)$.

**Notation.** We often write $f : A \to B$ for an element $f \in \mathrm{Mor}(A, B)$.

**Example 1.2.** $\mathcal{C} = \mathbf{Sets}$. Objects are sets; morphisms are maps between sets.

**Example 1.3.** $\mathcal{C} = \mathbf{Groups}$. Objects are groups; morphisms are group homomorphisms.

**Example 1.4.** $\mathcal{C} = \mathbf{Rings}$. Objects are commutative rings with unit; morphisms are ring homomorphisms. (If $\phi : A \to B$ is a homomorphism, we require $\phi(1_A) = 1_B$.)

**Example 1.5.** $\mathcal{C} = A\textbf{-Mod}$. Objects are modules over a ring $A$; morphisms are $A$-module homomorphisms. Special cases: if $A = k$ is a field, we recover $k\textbf{-Vect}$; if $A = \mathbb{Z}$, we recover $\mathbf{AbGps}$.

**Example 1.6.** $\mathcal{C} = \mathbf{Top}$. Objects are topological spaces; morphisms are continuous maps.

**Example 1.7.** $\mathcal{C} = G\textbf{-Sets}$. Objects are sets with an action of a group $G$; morphisms are set maps respecting the action, i.e., $f(g \cdot s) = g \cdot f(s)$ for all $g \in G$, $s \in S$.

> **MANTRA.** The morphisms of a category are just as important as the objects themselves!

**Example 1.8.** Let $\mathcal{C}$ be a category. We construct a new category $\mathcal{D}$ whose objects are all the morphisms of $\mathcal{C}$ (in particular, $\mathrm{Ob}(\mathcal{D})$ might not be a set). Say $f : A \to B$ and $g : A' \to B'$ are two objects of $\mathcal{D}$. A morphism between them is a pair of maps $(\phi, \psi) \in \mathrm{Mor}_\mathcal{C}(A, A') \times \mathrm{Mor}_\mathcal{C}(B, B')$ such that the following diagram commutes:

```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
A \arrow[r, "f"] \arrow[d, "\phi"'] & B \arrow[d, "\psi"] \\
A' \arrow[r, "g"'] & B'
\end{tikzcd}
\end{document}
```

---

## 2. Initial and Terminal Objects

Some categories are endowed with particular objects that either admit a map to or from every other object in the category. We use these to introduce an important notion: *uniqueness up to unique isomorphism*.

**Definition 2.1.** An *initial object* in a category $\mathcal{C}$ is an object $P \in \mathrm{Ob}(\mathcal{C})$ such that for every object $A \in \mathrm{Ob}(\mathcal{C})$ there exists a unique morphism $P \to A$ (i.e., $\mathrm{Mor}(P, A)$ is a singleton for every $A$). A *terminal object* is an object $P$ such that for every $A$ there is a unique morphism $A \to P$.

**Example 2.2.** $\mathbf{Sets}$ has an initial object: the empty set $\emptyset$. Terminal objects: any singleton set. Any two singleton sets are in bijection by a unique map.

**Example 2.3.** In $\mathbf{Groups}$, any one-element group is both initial and terminal.

**Example 2.4.** In $\mathbf{Rings}$, $\mathbb{Z}$ is an initial object: any ring homomorphism $\phi : \mathbb{Z} \to A$ is uniquely determined by $\phi(1) = 1_A$. The zero ring $\{0\}$ is the terminal object.

**Example 2.5.** Initial and/or terminal objects need not exist. In the category of all fields, there are neither.
