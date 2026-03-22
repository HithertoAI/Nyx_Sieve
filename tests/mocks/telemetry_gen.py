import random
import time

class NyxMockGenerator:
    """
    Generates synthetic 'Dirty' data for testing the Nyx Sieve protocol.
    Ensures all generated data is Bauta-compliant (zero real PII).
    """

    def generate_dirty_web_intake(self):
        """
        Simulates the 'Intake' of a non-compliant website[cite: 5].
        Includes bad HTML structures and missing accessibility markers.
        """
        elements = [
            {"type": "div", "content": "Ad_Flash_01", "role": "none", "is_chaotic_js": True},
            {"type": "img", "src": "header_02.png", "alt": None}, # No alt-text [cite: 5]
            {"type": "button", "label": "Click Me", "id": "btn_402", "pos": [450, 20]},
            {"type": "form", "fields": 12, "labels": False} # Chaotic form 
        ]
        return {"source": "dirty_html_stream", "payload": elements}

    def generate_haptic_spatial_data(self):
        """
        Simulates spatial geometry for the 'Night-Seeing' sleeve[cite: 346, 559].
        Maps object proximity to frequency signatures.
        """
        # Distant object thrum (10-20 Hz) [cite: 562]
        # Proximal object staccato (250+ Hz) [cite: 563]
        return {
            "object_id": "door_frame",
            "distance_m": round(random.uniform(0.5, 12.0), 2),
            "target_frequency": random.choice([15, 120, 255]), # Mapped to depth [cite: 561, 564]
            "texture": "crisp_dense" # Relative meaning [cite: 186]
        }

    def generate_acoustic_presence(self):
        """
        Simulates 'Night-Hearing' haptic pulses for environmental awareness[cite: 347, 566].
        """
        sounds = ["human_speech", "emergency_siren", "ambient_wind"]
        choice = random.choice(sounds)
        
        signatures = {
            "human_speech": {"freq": 165, "texture": "bubbling"}, # Prosody mimic [cite: 567]
            "emergency_siren": {"freq": 300, "texture": "jagged_jolt"}, # Sharp alert [cite: 568]
            "ambient_wind": {"freq": 30, "texture": "traveling_ripple"} # Presence [cite: 569]
        }
        return {"source": choice, "signature": signatures[choice]}

    def generate_intent_map(self):
        """
        Simulates the Keating Model's 'Intent-to-Action' mapping[cite: 17, 434].
        """
        actions = ["pay_electric_bill", "check_balance", "navigate_to_exit"] # Routine habits 
        return {
            "user_intent": random.choice(actions),
            "confidence_score": 0.94,
            "path_coordinates": [[10, 10], [450, 20]] # The 'Gold' path [cite: 20]
        }

if __name__ == "__main__":
    generator = NyxMockGenerator()
    print("--- BAUTA-COMPLIANT MOCK TELEMETRY ---")
    print(f"Web Intake: {generator.generate_dirty_web_intake()}")
    print(f"Sleeve Spatial: {generator.generate_haptic_spatial_data()}")
    print(f"Acoustic Pulse: {generator.generate_acoustic_presence()}")
    print(f"Intent Map: {generator.generate_intent_map()}")
