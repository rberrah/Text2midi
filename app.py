import streamlit as st
from prompt_parser import parse_prompt
from midi_generator import generate_midi

st.title("🎧 Générateur de MIDI à partir d'un prompt")

prompt = st.text_input("Décris la musique que tu veux créer :", "Une balade jazz avec du saxophone et un tempo lent")

if st.button("Générer"):
    params = parse_prompt(prompt)
    midi_file = generate_midi(params)
    st.success("Fichier MIDI généré !")

    with open(midi_file, 'rb') as f:
        st.download_button("Télécharger le fichier MIDI", f, file_name="composition.mid")
