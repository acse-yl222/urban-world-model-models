# TorchRotor-RANS v0.3 — rotating actuator-line trial

23 turbines, 10 m/s inlet, 8 m grid, k–epsilon, 30-second model-transition trial initialized from the prior ADM flow at 600 s. Three actuator lines per turbine use scaled NREL reference chord, twist and polar data, not identified site-turbine specifications. Speed is prescribed at TSR=7; initial phase is zero for every rotor, with blades spaced 120 degrees apart. This synchronised phase choice is a trial assumption, not measured farm operation.

Thrust, aerodynamic shaft torque and mechanical power are computed from lift/drag and coupled to the flow. Ct=0.95 is not imposed. No blade-surface CFD, rotor-speed dynamics, electrical generation, controller, water/waves, floating motion or moorings are included. No steady-state, grid-independent or experimentally validated performance claim is made.

The animation displays actuator lines at recorded solver phases, with 1:1 default physical-time playback. Old decorative blades are removed in this mode. See model_card.md, numerical_audit.json and alm_trial_summary.json. The earlier ADM runs remain available and unchanged. The full input data, licence, source snapshots, parent-state provenance and restart are retained locally in the protocol run; the selected public files are presentation derivatives.
