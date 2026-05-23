import streamlit as st
st.set_page_config(
    page_title="AI Music Generator",
    page_icon="🎵"
)
st.title("🎵 AI Music Generator")
st.write(
    "AI-generated MIDI music successfully created."
)
st.subheader("Generated Music File")
with open(
    "generated_music/output.mid",
    "rb"
) as file:
    st.download_button(
        label="Download Generated Music",
        data=file,
        file_name="output.mid",
        mime="audio/midi"
    )
st.success("Music generation completed successfully!")