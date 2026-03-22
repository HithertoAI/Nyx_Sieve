# 🧩 User Calibration: The "User-Twin" Onboarding

**Nyx Sieve** does not use a standard "Settings" menu. Instead, it conducts a **Stateful Calibration** to build a private, local profile known as the **User-Twin**. This profile lives exclusively on the device’s **System on a Chip (SoC)**, ensuring total privacy via the **Bauta Valve**.

## 1. The Calibration Flow: Designing from Intent
The goal is to move from **Information Accessibility** (telling a person what is there) to **Experiential Agency** (allowing a person to feel why it matters).

### Step 1: Spatial Perception (The Haptic Map) 
The system does not assume how a user perceives space. [cite_start]It asks: *"What haptic frequency feels like a 'primary action' to you?"*
* **Action**: The **HDPS-1 Sleeve** emits a frequency sweep (10Hz – 300Hz).
* **Selection**: The user identifies their "high-fidelity" comfort zone for different interaction types.
* **Result**: This defines the personalized **Haptic Signature** for buttons, forms, and navigation anchors.

### Step 2: Intent-to-Action Mapping (The Keating Model) 
We establish the user's unique "Architecture of Experience".
* **Scenario**: The user is asked to perform or describe a specific intent, such as: *"I want a button that feels 'urgent' in the top-right tactile quadrant"*.
* **Capture**: The **Keating Model** records this "Intent-to-Action" map.
* **Outcome**: The browser can now generate source code that satisfies that intent in reverse, allowing a user to "sculpt" with intent rather than just coding by line.

---

## 2. Adaptive Calibration States 
The **Nyx Sieve** architecture is modular. ]The interface layer swaps based on the specific "Exclusion Gap" identified during onboarding:

| User Need | Calibration Focus | Adaptive Experience Result |
| :--- | :--- | :--- |
| **Blind/Low-Vision** | Spatial Geometry | ]**Night-Seeing**: Translating visual density into spatial haptic pressures. |
| **Hearing-Impaired** | Temporal Presence  | **Night-Hearing**: Translating tone and rhythm into visceral frequencies. |
| **Neurodivergent** | Cognitive Load | **Cognitive Filtering**: Dampening "Dark Patterns" and sensory overload. |
| **Limited Mobility** | Predictive Intent | **Intent Engine**: Enlarging targets or executing actions based on recognized "exit" intent. |

---

## 3. The "Inclusion Flywheel" Data Loop 
This calibration doesn't just benefit the user; it fuels the project's economic sustainability:
1. **Stateful Calibration**: The user builds their unique mental model/workflow.
2. **Keating Capture**: The model captures high-efficiency, PII-free workflow data.
3. **Bauta Sifting**: The Valve ensures all data is "Ethical Data," pre-cleared for global compliance (GDPR/CCPA).
4. **Licensing**: These anonymized corpora are licensed to AI and robotics developers to fund the free tool.

---

## 🛡️ Security Note for Contributors
* **Zero-Persistence**: All calibration logic must follow the zero-persistence model.
* **Chamber Isolation**: No "User-Twin" profile should ever exist outside of its dedicated, local **Bauta Chamber**.
