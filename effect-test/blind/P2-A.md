An eight-channel upper-arm electromyography (EMG) device records electrical muscle signals from the human demonstrator. The signals are processed to represent muscle activation, which a model uses with arm posture to estimate human arm endpoint stiffness. The estimated stiffness profile is mapped to the gains of the robot’s joint impedance controller, which applies those gains during motion.

**Terminology ledger**

| Term | Role |
|---|---|
| EMG signals | Recorded electrical muscle signals |
| Muscle activation | Representation derived from the signals |
| Endpoint stiffness | Model estimate |
| Controller gains | Parameters mapped from the estimated stiffness profile |

**Revision notes:**

- Corrected the sequence from recorded signals to activation, estimated stiffness, and controller gains.
- Distinguished estimated stiffness from a direct EMG measurement.
- Removed the unsupported claims of direct force control and physical application of human stiffness.