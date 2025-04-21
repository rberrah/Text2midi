import streamlit as st
from prompt_parser import parse_prompt
from midi_generator import generate_midi, midi_to_wav
import os

st.set_page_config(page_title="Text2MIDI", layout="centered")
st.title("🎵 Text2MIDI - Crée ta musique avec un prompt !")

prompt = st.text_area("🔍 Décris ta musique (style, ambiance, instruments, tempo...):",
                      "Une balade jazz relaxante avec du saxophone et une contrebasse lente")

if st.button("🎶 Générer la musique"):
    st.info("🚀 Analyse du prompt...")
    params = parse_prompt(prompt)
    st.write("**Paramètres détectés :**", params)

    st.info("🎵 Génération du fichier MIDI...")
    midi_path = generate_midi(params)

    st.success("✅ Fichier MIDI généré !")
    st.audio(midi_path, format='audio/midi')

    with open(midi_path, 'rb') as f:
        st.download_button("💾 Télécharger le MIDI", f, file_name="composition.mid")

    st.info("🎧 Conversion en audio WAV...")
    wav_path = midi_to_wav(midi_path)
    st.audio(wav_path, format='audio/wav')

    with open(wav_path, 'rb') as f:
        st.download_button("💾 Télécharger l'audio", f, file_name="composition.wav")
