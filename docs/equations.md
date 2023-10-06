## Equations

# Bra

```math
\langle \phi | = ( | \phi \rangle )^\dagger = \begin{pmatrix} a_1^* & a_2^* & \cdots & a_n^* \end{pmatrix}
```

- $`\phi`$: the conjugate of $\psi$ or another wavefunction describing a quantum state

The conjugate transpose (Hermitian conjugate) of the corresponding ket. It's essentially a row vector. ([Wikipedia](https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation))

# Inner Product

```math
\langle \phi | \psi \rangle = \sum_{i=1}^{n} a_i^* b_i
```

- $`\psi`$: a wavefunction describing a quantum state
- $`\phi`$: the conjugate of $\psi$ or another wavefunction describing a quantum state

It's akin to the dot product in classical vector spaces but is way more general and powerful. Because it can essentially take the very complicated spaces of wavefunctions and linearize them - making any solution to the Schrödinger equation a vector in the Hilbert space (i.e a linear combination of some orthonormalized basis vectors) ([Wikipedia](https://en.wikipedia.org/wiki/Inner_product_space))

# Ket

```math
| \psi \rangle = \begin{pmatrix}a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix}
```

- $`\psi`$: a wavefunction describing a quantum state

A column vector (state vector) in a Hilbert space. It describes the state of a quantum system. ([Wikipedia](https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation))

# Outer Product

```math
| \psi \rangle \langle \phi | = \begin{pmatrix} a_1 b_1^* & a_1 b_2^* & \cdots \\ a_2 b_1^* & a_2 b_2^* & \cdots \\ \vdots & \vdots & \ddots \end{pmatrix}
```

- $`\psi, \phi`$: wavefunctions describing quantum states

The outer product is a generalization of the cross product to any dimensionality. It expands the number of dimensions to define the total space of two or more vectors and creates a new Hilbert space. It translates operator language into matrix language (i.e. an abstract transformation into a representation of that transformation in a basis). ([Wikipedia](https://en.wikipedia.org/wiki/Outer_product))
