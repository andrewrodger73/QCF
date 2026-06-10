# Quantum Constraint Framework (QCF) — v2.0.0
### Mathematical Core & Consolidated Cosmological Simulators

A long-standing crisis in modern theoretical physics is the incompatibility between the smooth geometric description of general relativity (GR) and the unitary demands of quantum mechanics (QM). At the core of a classical black hole, the Schwarzschild metric drives the Kretschmann scalar ($K$) to infinity, yielding an illegal physical singularity where predictability breaks down completely.

The Quantum Constraint Framework (QCF) resolves this breakdown via the Postulate of Isomorphic Cosmic Equilibrium (ICE). ICE asserts a one-to-one structural mapping between the maximum quantum information capacity of a localized gravitational boundary and the maximum allowable curvature of the interior bulk geometry it encloses. 

By identifying the Einstein tensor at the horizon boundary interface ($r = r_s$) with an effective quantum surface stress tensor ($\Sigma_{\mu\nu}^{\text{QM}}$) that enforces the Bekenstein entropy bound, the interior curvature encounters a universal, finite saturation ceiling:

$$K_{\text{max}} = \frac{1}{16 l_p^4}, \quad r_{\text{cut}} = 192^{1/6} r_s^{1/3} l_p^{2/3}$$

---

## Repository Architecture

The core code engine runs a unified diagnostic simulation suite encompassing two synchronized modules:
1. Module 1: Global Validation Suite — Evaluates macroscopic thermodynamic properties, integrated graybody power fractions, emission spectra, and phenomenological bounds.
2. Module 2: Interior Collapse Simulator — Tracks dynamic metric truncation, mapping both abrupt and smooth algebraic core regularizations directly against classical trajectories.

---

## Simulation Profiles & Outputs

All generated visual assets are compiled, rendered, and saved directly into a single consolidated directory:

### Module 1: Global Validation Suite
* results/Fig1_Emax.png (Energy Bounds): Evaluates maximum informational energy thresholds ($E_{\text{max}}$) as a function of mass, illustrating the exact sub-linear $M^{-1/3}$ power law crossing the orange Fermi-LAT observational constraint band.
* results/Fig2_lifetime.png (Evaporation Lifetimes): Compares QCF evaporation models against semiclassical Hawking lifetimes. Demonstrates precise correspondence principle alignment where QCF variations lie perfectly flush on top of standard GR lines for astronomical bodies.
* results/Fig3_spectrum.png (Spectral Signatures): Visualizes the continuous graybody emission profile for a primordial black hole ($M = 5 \times 10^{11}\text{ kg}$), showcasing the sharp high-frequency truncation cliff induced by the information cutoff boundary.
* results/Fig4_KKmax.png (Horizon Curvature Profiles): Tracks the invariant dimensionless curvature ratio $K/K_{\text{max}}$ across a solar-mass horizon, showing the classical GR transition safely flattening into the invariant saturation plateau.

### Module 2: Interior Collapse Simulator
* results/QCF_Kretschmann_Truncation.png (Singularity Elimination): Maps the spatial collapse profile of internal matter moving through the horizon toward $r \rightarrow 0$, visually plotting the exact crossover where classical infinity is eliminated by the Planckian curvature ceiling.

           K(r) ^
                |      /  [Classical Singularity Extrapolates to Infinity]
                |     / :
        K_max --|----+  :  <-- QCF Circuit Breaker Triggers at r_cut
     (1/16)     |    |  : 
                |____|__:_________________> r
                0   r_cut

---

## Quantitative Scaling Profiles

Because $r_{\text{cut}}$ scales sub-linearly relative to the horizon radius ($r_{\text{cut}} \propto r_s^{1/3}$), the framework naturally explains why classical GR remains an exceptional effective field theory for massive astronomical bodies, while resolving structural infinities at micro-scales:

* Primordial ($10^{12}\text{ kg}$) | Horizon Radius: $\sim 1.48 \times 10^{-15}\text{ m}$ | Cutoff Radius: $\sim 1.75 \times 10^{-28}\text{ m}$
* Stellar ($1\text{ M}_{\odot}$)     | Horizon Radius: $\sim 2.95 \times 10^3\text{ m}$  | Cutoff Radius: $\sim 2.20 \times 10^{-22}\text{ m}$
* Intermediate ($10\text{ M}_{\odot}$)| Horizon Radius: $\sim 2.95 \times 10^4\text{ m}$  | Cutoff Radius: $\sim 4.75 \times 10^{-22}\text{ m}$

---

## Run

### Setup Dependencies
Install the required scientific stack via the project package manager:

    $ pip install -r requirements.txt

### Execution
To fire the consolidated simulation suite and calculate all thermodynamic properties, spectral profiles, and interior metrics:

    $ python QCF_v2_sim.py

* All 5 figures will automatically compile, format, and save directly to the results/ directory.

---

## Scholarly Context

Unlike standard phenomenological models that manually inject an ad-hoc fluid de Sitter core inside the horizon metric, QCF requires no exotic internal stress-energy fluid assumptions. The interior spatial truncation arises purely as a dynamic consequence of informational saturation at the event horizon interface. 

Furthermore, by completely eliminating the $r \rightarrow 0$ singularity, this exact scaling mechanism applies globally to the universe at $t = 0$ — mathematically replacing the Big Bang singularity with a smooth, non-singular cosmic bounce.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

*Developed independently at maximum operational speed. Run the metrics, review the scripts, and audit the workings for yourself.*
