# 🛡️ Data Privacy & The Bauta Protocol

This directory is empty by design.

In accordance with the **Bauta Valve Protocol**, Nyx Sieve enforces a **Zero-Persistence** policy for all raw telemetry and user data.

## 🔒 Privacy Standards:
- **No Raw Intake:** Raw visual, audio, or haptic telemetry is never committed to this repository.
- **Local Processing:** All "Chamberized Sifting" occurs locally on the user's System on a Chip (SoC).
- **Ephemeral Memory:** Data processed within the Valve is wiped immediately upon task completion.

## 🛠️ For Developers:
If you are testing new haptic signatures or UI reconstructions, please use the local Mock Telemetry Generator located in `/tests/mocks/`.

This ensures your development environment remains Bauta-compliant without risking the exposure of real-world data.
