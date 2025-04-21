def parse_prompt(prompt):
    prompt = prompt.lower()
    styles = ["classique", "jazz", "techno", "rock", "pop", "blues", "lofi"]
    instruments = ["piano", "basse", "batterie", "violon", "guitare", "saxophone"]
    moods = ["joyeux", "triste", "calme", "énergique", "romantique"]

    detected = {
        "style": next((s for s in styles if s in prompt), "pop"),
        "tempo": 90 if "lent" in prompt else 140 if "rapide" in prompt else 120,
        "mood": next((m for m in moods if m in prompt), "neutre"),
        "instruments": [i for i in instruments if i in prompt]
    }
    return detected
