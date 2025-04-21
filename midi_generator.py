import pretty_midi

def generate_midi(params):
    midi = pretty_midi.PrettyMIDI()
    piano = pretty_midi.Instrument(program=0)  # 0 = piano

    # Exemple simple : créer une mélodie aléatoire
    for i in range(8):
        note = pretty_midi.Note(
            velocity=100,
            pitch=60 + i,
            start=i * 0.5,
            end=(i + 1) * 0.5
        )
        piano.notes.append(note)

    midi.instruments.append(piano)
    midi_file_path = "output.mid"
    midi.write(midi_file_path)
    return midi_file_path
