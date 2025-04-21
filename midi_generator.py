import pretty_midi
import random
import os
import subprocess

def generate_midi(params):
    midi = pretty_midi.PrettyMIDI()

    # Mapping instrument name to MIDI program number
    instrument_map = {
        "piano": 0, "guitare": 25, "violon": 40,
        "basse": 33, "saxophone": 65, "batterie": 118
    }

    for instr in params["instruments"]:
        program = instrument_map.get(instr, 0)
        inst = pretty_midi.Instrument(program=program)

        for i in range(8):
            note = pretty_midi.Note(
                velocity=100,
                pitch=random.randint(60, 72),
                start=i * 0.5,
                end=i * 0.5 + 0.4
            )
            inst.notes.append(note)
        midi.instruments.append(inst)

    output_path = "output.mid"
    midi.write(output_path)
    return output_path

def midi_to_wav(midi_path):
    wav_path = midi_path.replace(".mid", ".wav")
    sf2 = "FluidR3_GM.sf2"  # Assure-toi que ce fichier est présent dans le répertoire
    command = ["fluidsynth", "-ni", sf2, midi_path, "-F", wav_path, "-r", "44100"]
    subprocess.run(command, check=True)
    return wav_path

