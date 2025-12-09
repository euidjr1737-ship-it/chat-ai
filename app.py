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
    )
}

role_name = st.sidebar.selectbox("Choose a performing-arts role:", list(roles.keys()))
role_description = roles[role_name]
st.sidebar.info(role_description)

# -----------------------
# User Input Area
# -----------------------
user_input = st.text_area(
    "💬 Ask your question or describe your live-performance idea:",
    height=120,
    placeholder="e.g., How can I make a transition scene feel more magical on stage?"
)

# -----------------------
# Generate Response
# -----------------------
if st.button("Generate Response"):
    if not api_key:
        st.warning("⚠️ Please enter your OpenAI API key in the sidebar.")
    elif not user_input:
        st.warning("Please enter a question or idea first!")
    else:
        try:
            client = OpenAI(api_key=api_key)

            with st.spinner("🎭 Generating creative advice..."):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": role_description},
                        {"role": "user", "content": user_input}
                    ],
                    max_tokens=500
                )

                answer = response.choices[0].message.content
                st.success(f"🎭 {role_name} says:")
                st.write(answer)

        except Exception as e:
            st.error(f"Error: {e}")

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.caption("Created for live-performance creatives • Streamlit + OpenAI")
