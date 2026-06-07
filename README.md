# Quantum Constraint Framework (QCF)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20576794.svg)](https://doi.org/10.5281/zenodo.20576794)

This repository contains the core codebase, mathematical verifications, and numerical scaling data for the **Quantum Constraint Framework (QCF)** at spacetime singularities, introducing the postulate of **Isomorphic Cosmic Equilibrium (ICE)**.

## Abstract
General Relativity predicts curvature divergence as $r \to 0$ in spherically symmetric spacetimes, while quantum unitarity forbids non-unitary loss of information. We propose the Quantum Constraint Framework (QCF), wherein the Schwarzschild radius $r_s$ acts as a thermodynamic interface. Spacetime curvature at the horizon is sourced by the coarse-grained von Neumann entropy of horizon-localized modes. The Einstein tensor at the boundary is identified with an effective quantum surface stress $\Sigma_{\mu\nu}^{QM}$ enforcing the Bekenstein entropy bound. Saturation of this informational bound yields a universal, finite curvature ceiling $K_{max} = 1/16$ in Planck units, dynamically inducing an interior spatial cutoff $r_{cut} \propto r_s^{1/3}$. 

This framework resolves the central singularity without altering standard external General Relativity for macroscopic black holes, offering concrete testable scaling signatures for primordial black holes (PBHs).

## Repository Contents
* `/src` - Core scripts for computing the curvature ceiling and thermodynamic boundary conditions.
* `/plots` - Generated scaling plots (Curvature Truncation and Cutoff Radius vs. Mass).
* `V2.pdf` - The compiled comprehensive thesis.

## Citation

If you use this framework, equations, or data scaling models in your research, please cite the work as follows:

### BibTeX
```bibtex
@misc{rodger2026qcf,
  author       = {Rodger, Andrew},
  title        = {Quantum Constraint Framework at Spacetime Singularities: A Postulate of Isomorphic Cosmic Equilibrium},
  month        = jun,
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20576794},
  url          = {[https://doi.org/10.5281/zenodo.20576794](https://doi.org/10.5281/zenodo.20576794)}
}
