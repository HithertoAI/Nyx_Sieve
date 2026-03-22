# 🧬 Human Impact Statement (HIS) Template

**Note:** PRs submitted without a completed HIS will be automatically labeled as "Incomplete Intent" and will not proceed to technical review.

## 1. The Exclusion Gap
- **Identify the "Bug":**
  - Which specific exclusion gap in the digital or physical world is this PR patching? (e.g., visual density, acoustic isolation, or cognitive overload)
- **The "Win":**
  - Describe the specific "Win" for the stakeholder (The User, The Creator, or The Regulator).

## 2. Cognitive Load Reduction
- **The Sieve Effect:**
  - How does this contribution simplify the user’s mental model?
- **Intent Alignment:**
  - Does this code help the Keating Model better translate a user's "Intent" into "Action"?
- **Friction Check:**
  - Does this move the user closer to a "Zero-Friction" creation environment?

## 3. Bauta Integrity & Privacy
- **Local Chamber Confirmation:**
  - Confirm that all telemetry and PII processing remains 100% local to the device's System on a Chip (SoC).
- **Zero-Persistence:**
  - Verify that no raw data is stored beyond its immediate execution window.
- **Chamber Isolation:**
  - If you modified a chamber (A-E), explain how you maintained the "mathematical isolation" between gates.

## 4. Ambient Agency vs. Extractive Attention
- **The "Screentime" Test:**
  - Does this feature require active visual attention (Extractive), or does it provide a passive "Sense of Presence" (Ambient)?
- **Transparency:**
  - Does this logic allow the user to keep their eyes on the physical world (e.g., the sunset or a child's face) while receiving the data?

## 5. Thermal & Hardware Sensitivity
- **NPU Optimization:**
  - Is this logic offloaded to the Neural Processing Unit to maintain the sub-10ms latency target?
- **Skin-Safe Thermal Profile:**
  - For wearable-related code (Sleeves/Collars), confirm that these changes do not push the SoC beyond the 1.5W thermal safety limit.
