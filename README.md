# Quantum Constraint Framework (QCF) at Spacetime Singularities

### *A Postulate of Isomorphic Cosmic Equilibrium*

**Author:** Andrew Rodger  
**Date:** June 2026  
**License:** MIT / Open Science  

---

## 🌌 Overview
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20615629.svg)](https://doi.org/10.5281/zenodo.20615629)

The **Quantum Constraint Framework (QCF)** introduces a novel, systems-level resolution to the long-standing incompatibility between the smooth geometric descriptions of General Relativity (GR) and the unitary demands of Quantum Mechanics (QM). 

Instead of treating the interior vacuum of a black hole as entirely disconnected from its boundary, QCF introduces the **Postulate of Isomorphic Cosmic Equilibrium (ICE)**. ICE asserts a strict one-to-one structural mapping between the maximum quantum information capacity of a localized gravitational boundary (the event horizon) and the maximum allowable curvature of the interior bulk geometry it encloses.

By enforcing the Bekenstein entropy bound as a dynamic, thermodynamic boundary condition, the framework eliminates the classical $r \rightarrow 0$ infinite singularity, replacing it with a universal, finite curvature ceiling and a non-singular interior spatial cutoff.

---

## 🛠️ Core Mathematical Framework

QCF modifies the standard Einstein field equations strictly at the horizon boundary interface ($r = r_s$):

$$\Sigma_{\mu\nu}^{\text{GR}}|_{r=r_s} = \Sigma_{\mu\nu}^{\text{QM}}$$

Where the effective boundary quantum stress tensor $\Sigma_{\mu\nu}^{\text{QM}}$ is sourced by the coarse-grained von Neumann entropy $S_{\text{vN}}$ of the horizon-localized states:

$$\Sigma_{\mu\nu}^{\text{QM}} \equiv \frac{S_{\text{vN}}}{A_H}g_{\mu\nu}$$

### 1. The Curvature Ceiling
When horizon modes saturate the Bekenstein bound ($S_{\text{vN}} \le A_H/4$), the boundary stress tensor reaches its maximum saturation threshold of $\frac{1}{4}g_{\mu\nu}$. This dynamically constrains the interior Kretschmann scalar ($K = R_{\alpha\beta\gamma\delta}R^{\alpha\beta\gamma\delta}$), inducing a universal physical cap:

$$K_{\text{max}} = \frac{1}{16}$$

### 2. The Dynamic Spatial Cutoff
Because physical curvature cannot exceed $K_{\text{max}}$, the spatial coordinate $r$ cannot continuously contract to zero. Setting the classical Schwarzschild curvature profile equal to this ceiling yields a minimum physically realizable radius, $r_{\text{cut}}$:

$$r_{\text{cut}} = 192^{1/6}r_s^{1/3}l_p^{2/3}$$

This sub-linear scaling behavior ($r_{\text{cut}} \propto r_s^{1/3}$) reveals that while the cutoff is buried deep inside macroscopic astrophysical black holes, it expands significantly in relative size for low-mass regimes.

---

## 📊 Scale Profiles Across Mass Regimes

| Mass Profile | Horizon Radius $r_s$ (m) | Cutoff Radius $r_{\text{cut}}$ (m) | Relative Ratio $r_{\text{cut}}/r_s$ |
| :--- | :--- | :--- | :--- |
| **Primordial** ($10^{12} \text{ kg}$) | $1.49 \times 10^{-15}$ | $1.75 \times 10^{-28}$ | $1.2 \times 10^{-13}$ |
| **Stellar** ($1\ M_{\odot}$) | $2.95 \times 10^{3}$ | $2.20 \times 10^{-22}$ | $7.5 \times 10^{-26}$ |
| **Intermediate** ($10\ M_{\odot}$) | $2.95 \times 10^{4}$ | $4.75 \times 10^{-22}$ | $1.6 \times 10^{-26}$ |

---

## 🚀 Repository Structure

This repository is organized to maintain total academic transparency and provide full reproducibility for the scientific community.
