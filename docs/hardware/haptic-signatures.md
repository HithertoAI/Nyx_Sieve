# 🦾 Hardware Spec: Haptic Signatures & Frequency Mapping

## Status and Hardware
- **Status:** 2026.Q1 Baseline 
- **Target Hardware:** High-Density Piezoelectric Sleeve (HDPS-1) 

## Digital Synesthesia and Actuators
To achieve Digital Synesthesia, the Nyx Sieve protocol maps environmental "meaning" to specific haptic signatures. We utilize Piezoelectric Actuators due to their sub-ms response time and ability to produce distinct "textures" compared to standard vibrating motors.

## 1. Frequency-to-Color Mapping (Chromesthesia)
Color is mapped to the skin as a "Tactile Signature" based on cross-modal correspondence research. This allows a user to "feel" the difference between a red apple and a green leaf. 
| Color | Frequency Range | Amplitude / Texture | User Perception |
|---------|-------------------|---------------------|----------------|
| Violet | 10 – 35 Hz | Low Amplitude | "Primal, organic, deep"  |
| Red | 10 – 35 Hz | High Amplitude| "Warm, intense, urgent" |
| Green | 60 – 200 Hz | Moderate  | "Growth, fresh, steady"  |
| Blue/Cyan | 200 – 300 Hz | Sharp / Pulsed | "Cool, technical, crisp"|

## 2. Spatial & Depth Mapping (Night-Seeing)
The Keating Model translates visual distance into frequency shifts. We utilize a negative monotonic correlation:
as an object or boundary gets closer, the frequency increases to trigger a pre-cognitive "danger" reflex.

- Distant (>10m): Low-frequency "thrum" (approx. **10–20 Hz**) at the sleeve's periphery
- Proximal (<2m): High-frequency "staccato" (**250+ Hz**) with high amplitude
- Obstacle Gradient: A linear sweep from **50 Hz** to **250 Hz** as the user approaches a boundary

##3. Intent & Social Signatures (Night-Hearing)
For the deaf or hard-of-hearing, we map acoustic "Presence" and "Intent" rather than simple text captions.

- Human Speech (Social Presence): A "bubbling" texture at **150–180 Hz**, mimicking the rhythm of natural prosody
- Emergency (Sirens/Alarms): Jagged, non-sinusoidal pulses at **300 Hz** ("Sharp Jolt")
- Ambient Environment (Wind/Nature): Traveling ripples across the sleeve at **10–50 Hz** to provide "Presence"

##4. Technical Constraints for SoC Integration
To maintain the "illusion of reality," hardware must meet these throughput targets:

- Sampling Rate:** The SoC must drive the actuator bus at a minimum of **2 kHz** to avoid aliasing in the **300 Hz+** high-fidelity range
- Latency Target:** `<10ms` motion-to-haptic delay
- Sensitivity Anchor Points:** Prioritize high-density actuator placement at the wrist and elbow for maximum data throughput

> The Inclusion Flywheel ensures that a *"Red"* sunset and a *"Red"* apple share a shared Physical Signature, allowing the user's brain to form intuitive connections that define experiential agency.
