An eight-channel upper-arm electromyography (EMG) device records electrical muscle signals from the human demonstrator, which are processed to represent muscle activation. A model uses this activation and arm posture to estimate human arm endpoint stiffness. The estimated stiffness profile is then mapped to gains of the robot joint impedance controller, which applies those gains during motion.

**Revision notes:**

- Corrected the sequence from EMG recording through stiffness estimation to controller gains.
- Distinguished estimated stiffness from a direct EMG measurement.
- Removed the unsupported claims that the robot directly applies human stiffness or an “impedance force.”

| Term | Use in this passage |
|---|---|
| EMG | Electromyography, defined at first use |
| Human arm endpoint stiffness | Estimated by the model |
| Robot joint impedance controller gains | Set by mapping the estimated stiffness profile |