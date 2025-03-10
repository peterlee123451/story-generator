import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = st.secrets[""]

st.title("Story Generator")


if st.button("Generate Response"):
    if prompt:
        response = openai.ChatCompletion.create(
            model="GPT-4",
            messages=[
                {"role": "user", "content": "Write me a 1000 word story about any topic."}
            ]
        )
        st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter a prompt.")