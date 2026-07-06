# Codex Task: Convert Commutative Algebra Lecture Notes to Obsidian Markdown

## Context

This folder contains Rice University MATH 464 (Commutative Algebra, Spring 2020) lecture notes. Each `lecture-XX.md` and `homework-XX.md` file was generated as a "link page" by a previous pipeline — it embeds PNG images of the original PDF pages and stores extracted text in collapsed `<details>` blocks. **These files need to be completely rewritten** as proper, self-contained Obsidian markdown files that a reader can study directly, without clicking on any images.

Two files have already been converted as reference examples:
- `lecture-01.md` — covers categories, initial/terminal objects
- `lecture-02.md` — covers functors, Zorn's lemma, nilradical

Read those files first to understand the target format.

---

## Your Task

Convert the following files, **in order**, from "link pages" to clean Obsidian markdown:

**Lectures:** `lecture-03.md` through `lecture-37.md`  
**Homeworks:** `homework-01.md` through `homework-11.md`

For each file:
1. Read the existing `.md` file to see the page count and title.
2. Read each page image at `assets/lecture-XX/page-00N.png` (or `assets/homework-XX/page-00N.png`) using the Read tool — these are the authoritative source. Do NOT rely on the extracted text in the `<details>` blocks (it mangles formulas and arrows).
3. Rewrite the `.md` file completely as clean Obsidian markdown (see format rules below).

---

## Format Rules

### General structure

```markdown
# Lecture NN — [Title from the PDF]

*MATH 464, Rice University, Spring 2020 · [Date from bottom of first page]*

---

## 1. Section Title

[content]

### 1.1. Subsection Title (if present)

[content]
```

For homeworks:
```markdown
# Homework NN

*MATH 464, Rice University, Spring 2020 · Due: [date]*

---

## 1. Ideals / [section title from PDF]

**(1)** [problem text]

**(2)** [problem text]
```

### Math

- Use `$...$` for inline math and `$$...$$` for display math.
- Always use proper LaTeX commands:
  - `\mathcal{C}` for script letters (categories)
  - `\mathrm{Mor}`, `\mathrm{Ob}`, `\mathrm{id}` for roman operators
  - `\mathfrak{p}`, `\mathfrak{m}`, `\mathfrak{a}` for Fraktur (ideals)
  - `\otimes`, `\oplus`, `\bigoplus`, `\bigotimes` for tensor/direct sum
  - `\xrightarrow{f}` for labeled arrows in sequences
  - `\hookrightarrow` for injections, `\twoheadrightarrow` for surjections
  - `\operatorname{Hom}`, `\operatorname{Tor}`, `\operatorname{Ext}`, `\operatorname{Ann}`, `\operatorname{Spec}`, `\operatorname{rad}`, `\operatorname{im}`, `\ker`

### Theorems, definitions, etc.

Use **bold** labels inline (no special callout syntax needed for Obsidian):

```markdown
**Definition 3.1.** A *module* $M$ over a ring $A$ is ...

**Theorem 3.2** *(Nakayama's Lemma).* Let ...

*Proof.* ...  $\square$

**Corollary 3.3.** ...

**Remark 3.4.** ...

**Example 3.5.** ...
```

### Short exact sequences

Write as display math using arrows:

```markdown
$$0 \to M' \xrightarrow{f} M \xrightarrow{g} M'' \to 0$$
```

For chain complexes:
```markdown
$$\cdots \to M_{i-1} \xrightarrow{d_{i-1}} M_i \xrightarrow{d_i} M_{i+1} \to \cdots$$
```

### Commutative diagrams

Use a fenced `tikz` code block. This renders with the **TikZJax** Obsidian plugin (`\usepackage{tikz-cd}` must be included). The general template:

````markdown
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
A \arrow[r, "f"] \arrow[d, "\phi"'] & B \arrow[d, "\psi"] \\
A' \arrow[r, "g"'] & B'
\end{tikzcd}
\end{document}
```
````

Common patterns:

**Commutative square:**
```
\begin{tikzcd}
A \arrow[r, "f"] \arrow[d, "\alpha"'] & B \arrow[d, "\beta"] \\
C \arrow[r, "g"'] & D
\end{tikzcd}
```

**Fibered product / pullback (with universal property arrow):**
```
\begin{tikzcd}
T \arrow[drr, bend left, "p_1"] \arrow[ddr, bend right, "p_2"'] \arrow[dr, dashed, "\exists!"] & & \\
& A \times_C B \arrow[r] \arrow[d] & A \arrow[d, "f"] \\
& B \arrow[r, "g"'] & C
\end{tikzcd}
```

**Short exact sequence as diagram:**
```
\begin{tikzcd}
0 \arrow[r] & M' \arrow[r, "f"] & M \arrow[r, "g"] & M'' \arrow[r] & 0
\end{tikzcd}
```

**Map of short exact sequences (snake lemma setup):**
```
\begin{tikzcd}
0 \arrow[r] & M' \arrow[r] \arrow[d, "\alpha"] & M \arrow[r] \arrow[d, "\beta"] & M'' \arrow[r] \arrow[d, "\gamma"] & 0 \\
0 \arrow[r] & N' \arrow[r] & N \arrow[r] & N'' \arrow[r] & 0
\end{tikzcd}
```

**Chain complex map:**
```
\begin{tikzcd}
M' \arrow[r] \arrow[d] & M \arrow[r] \arrow[d] & M'' \arrow[d] \\
N' \arrow[r] & N \arrow[r] & N''
\end{tikzcd}
```

**Adjoint / naturality square:**
```
\begin{tikzcd}
\mathrm{Hom}(M \otimes N, P) \arrow[r, "\sim"] \arrow[d] & \mathrm{Hom}(M, \mathrm{Hom}(N, P)) \arrow[d] \\
\mathrm{Hom}(M \otimes N, Q) \arrow[r, "\sim"'] & \mathrm{Hom}(M, \mathrm{Hom}(N, Q))
\end{tikzcd}
```

**Spec diagram (for Noether normalization etc.):**
```
\begin{tikzcd}
\operatorname{Spec}(B) \arrow[dr] \arrow[r] & \operatorname{Spec}(A) \arrow[d] \\
& \operatorname{Spec}(k)
\end{tikzcd}
```

For any diagram you encounter that doesn't fit neatly into tikzcd (e.g., 3D diagrams or very unusual shapes), embed the original page image instead:

```markdown
![[assets/lecture-XX/page-00N.png]]
```

### Proofs

End every proof with `$\square$` on its own line (after the last sentence).

### Section breaks

Use `---` between major sections.

---

## Specific Notes by Topic

These appear frequently in this course — handle them as follows:

**Localization** (lectures ~18–20): The localized ring is $S^{-1}A$ or $A_\mathfrak{p}$. Elements are fractions $a/s$ with $a \in A$, $s \in S$. The universal property is: any ring map $A \to B$ sending elements of $S$ to units factors uniquely through $S^{-1}A$.

**Nakayama's Lemma** (appears repeatedly): State it as: Let $A$ be a local ring with maximal ideal $\mathfrak{m}$, $M$ a finitely generated $A$-module. If $\mathfrak{m} M = M$ then $M = 0$.

**Tensor products** (lectures ~9–11): $M \otimes_A N$. Recall $\otimes$ is right-exact but not left-exact; flatness is defined by $- \otimes_A M$ being exact.

**Tor and Ext** (lectures ~34–37): $\operatorname{Tor}_i^A(M, N)$ and $\operatorname{Ext}^i_A(M, N)$. Computed from projective/injective resolutions. Note $\operatorname{Tor}_0^A(M,N) = M \otimes_A N$ and $\operatorname{Ext}^0_A(M,N) = \operatorname{Hom}_A(M,N)$.

**Spec and Nullstellensatz** (lectures ~28–31): $\operatorname{Spec}(A)$ is the set of prime ideals. The Zariski topology has closed sets $V(\mathfrak{a}) = \{\mathfrak{p} \in \operatorname{Spec}(A) : \mathfrak{a} \subseteq \mathfrak{p}\}$.

---

## Quality Checklist

Before writing each file, ask yourself:
- [ ] Have I read **all** the page images (not just the extracted text)?
- [ ] Are all formulas in proper LaTeX (no garbled ASCII arrows like `//` or `2` standing in for `\in`)?
- [ ] Are commutative diagrams in `tikz` blocks (not as ASCII art)?
- [ ] Are definitions/theorems/lemmas clearly labelled in **bold**?
- [ ] Is there a proper title line and date?
- [ ] Does the file read naturally from top to bottom, like a typed set of lecture notes?

---

## File List

Process in this order:

### Lectures
- `lecture-03.md` — Nilradical and Jacobson radical (continued)
- `lecture-04.md` — Two odd ends from ideal theory
- `lecture-05.md` — Direct product and sum of modules
- `lecture-06.md` — Interlude: Products and Coproducts in a category
- `lecture-07.md` — Exact sequences (continued)
- `lecture-08.md` — Finitely generated modules (continued)
- `lecture-09.md` — Tensor products of modules
- `lecture-10.md` — More on tensor products
- `lecture-11.md` — Tensor products on maps
- `lecture-12.md` — Adjoint functors: category theory interlude
- `lecture-13.md` — Fibered products and co-products
- `lecture-14.md` — Tensor Algebra of a module
- `lecture-15.md` — Symmetric algebra, continued
- `lecture-16.md` — More on the Alternating algebra
- `lecture-17.md` — Clean-up from last class
- `lecture-18.md` — Localization
- `lecture-19.md` — Localization continued
- `lecture-20.md` — More local properties
- `lecture-21.md` — Chain conditions (continued)
- `lecture-22.md` — Composition series (continued)
- `lecture-23.md` — Wrapping up composition series
- `lecture-24.md` — Primary Decomposition in Noetherian rings
- `lecture-25.md` — The geometry of Primary Decomposition (continued)
- `lecture-26.md` — Integral extensions
- `lecture-27.md` — Going up
- `lecture-28.md` — Noether Normalization and Weak Nullstellensatz
- `lecture-29.md` — Noether Normalization (continued)
- `lecture-30.md` — Strong Nullstellensatz
- `lecture-31.md` — An equivalence of categories (continued)
- `lecture-32.md` — Artinian Rings (continued)
- `lecture-33.md` — Local Dedekind Domains
- `lecture-34.md` — Projective, Injective and Flat modules
- `lecture-35.md` — Enough Injectives
- `lecture-36.md` — Complexes and projective resolutions
- `lecture-37.md` — Tor (continued)

### Homeworks
- `homework-01.md` through `homework-11.md`

---

## Example Output

Here is how `lecture-01.md` looks after conversion (use this as style reference):

```markdown
# Lecture 01 — Categories

*MATH 464, Rice University, Spring 2020 · January 13, 2020*

---

## 1. Categories

**Definition 1.1.** A *category* $\mathcal{C}$ consists of

- a collection of objects $\mathrm{Ob}(\mathcal{C})$,
- a set $\mathrm{Mor}(A, B)$ for every two objects $A, B \in \mathrm{Ob}(\mathcal{C})$,
- a *composition law* $\circ : \mathrm{Mor}(A, B) \times \mathrm{Mor}(B, C) \to \mathrm{Mor}(A, C)$.

...

**Example 1.8.** ... such that the following diagram commutes:

​```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
A \arrow[r, "f"] \arrow[d, "\phi"'] & B \arrow[d, "\psi"] \\
A' \arrow[r, "g"'] & B'
\end{tikzcd}
\end{document}
​```

---

## 2. Initial and Terminal Objects

**Definition 2.1.** An *initial object* ...
```

---

## Important Notes

1. **Do not keep the old format.** The old files have `## Page 1`, `## Page 2`, etc. with `<details>` blocks. Delete all of that. The new file should read like a set of lecture notes, not like a page viewer.

2. **The extracted text is unreliable for math.** Especially in earlier lectures (01–10), the PDF text extraction garbled formulas — arrows become `//`, `∈` becomes `2`, etc. Always read the image and transcribe from there.

3. **Homeworks**: transcribe problem statements faithfully (including any multi-part structure). If a homework page contains only images of hand-drawn diagrams or student work, embed the image. But for typeset problems, transcribe them.

4. **Do not add commentary or explanations** that are not in the original. Your job is faithful transcription into proper markdown, not annotation.

5. **TikZJax plugin**: the `tikz` fenced code blocks require the user to install the **TikZJax** plugin in Obsidian (Community Plugins → TikZJax). You do not need to mention this in each file; it is noted in the course index.
