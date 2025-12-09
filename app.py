import streamlit as st
from openai import OpenAI

# -----------------------
# Page Configuration
# -----------------------
st.set_page_config(page_title="🎭 Performing Arts Creative Chatbot", layout="wide")
st.title("🎭 Performing Arts Creative Chatbot")
st.write("Select a role from the performing-arts industry and ask your question or pitch your idea!")

# -----------------------
# Sidebar: API Key + Role Selection
# -----------------------
st.sidebar.header("🔑 API & Role Settings")

# API key input
api_key = st.sidebar.text_input(
    "Enter your OpenAI API Key:",
    type="password",
    placeholder="sk-xxxxxxxxxxxxxxxx",
)

# Performing-arts roles
roles = {
    "🎼 Musical Director": (
        "You are a musical director. Give advice about vocal interpretation, harmony, "
        "tempo, ensemble balance, and how music drives emotional beats on stage."
    ),
    "📝 Dramaturg": (
        "You are a dramaturg. Provide deep analysis on narrative structure, character arcs, "
        "themes, pacing, and how the script can be strengthened artistically."
    ),
    "🎭 Acting Coach": (
        "You are an acting coach. Give guidance on emotional delivery, blocking, "
        "presence, timing, and character embodiment for the stage."
    ),
    "🎨 Stage / Set Designer": (
        "You are a stage and set designer. Describe set concepts, lighting, stage mechanics, "
        "color palettes, props, and how to visually support storytelling."
    ),
    "🔊 Sound Designer": (
        "You are a sound designer. Provide insights on sound cues, ambience, SFX, "
        "microphone strategy, and creating immersive auditory spaces for live performance."
