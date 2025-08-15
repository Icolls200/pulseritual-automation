import json, random, os

# Load product config
config = {
  "ritual_name": "Focus Flow",
  "social_proof_min": 1000,
  "social_proof_max": 2000,
  "scarcity_min": 50,
  "scarcity_max": 150
}

# Generate dynamic scarcity & social proof
scarcity = random.randint(config['scarcity_min'], config['scarcity_max'])
social_proof = random.randint(config['social_proof_min'], config['social_proof_max'])

# Build the value-first script
script = {
  "title": f"Morning Vitality Pulse: {os.getenv('DATE', 'TODAY')}",
  "hook": "YOUR CORTISOL SPIKE IN 3...2...1 → FIX IT NOW",
  "ritual_steps": [
    "30 sec of morning sunlight → 40%↓ stress (studies suggest)",
    "5 deep breaths through left nostril → focus boost",
    "Sip room-temperature water → hydration hack"
  ],
  "bio_cta": f"FIRST {scarcity} TAP BIO FOR:\n"
            f"1) YOUR PERSONAL RITUAL BLUEPRINT\n"
            f"2) THE '{config['ritual_name']}' RITUAL (USED IN THIS VIDEO)\n"
            f"3) JOIN {social_proof} RITUAL UPGRADERS"
}

# Output for robot
print(json.dumps(script))
