
# Quantum Coherence Framework (QCF) — v2.0.0

**Core claim:** Σ^GR = Σ^QM ⇒ K_max = 1/(16 l_p^4), r_cut = 192^{1/6} r_s^{1/3} l_p^{2/3}

This release reproduces the four validation figures:

1. **Fig1_Emax.png** – E_max 10^19–10^21 eV, 10 orders above Fermi-LAT
2. **Fig2_lifetime.png** – τ ∝ M^3, QCF = standard to <10^-12
3. **Fig3_spectrum.png** – no observable Hawking truncation for PBHs
4. **Fig4_KKmax.png** – solar-mass BH: K/K_max =1.7e-151 at horizon, capped at r_cut=2.2e-22 m

## Run
```
pip install -r requirements.txt
python QCF_v2_sim.py
```
All figures appear and save to `results/`.

## License
MIT
