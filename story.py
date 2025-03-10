import streamlit as st
import openai

if 'api_key' not in st.session_state:
    st.session_state.api_key = ''

st.title("Story Generator")

api_key = st.text_input("Enter your OpenAI API key:", value=st.session_state.api_key, type="password")

if api_key:
    st.session_state.api_key = api_key
    openai.api_key = api_key

if st.session_state.api_key:
    genre = st.selectbox(
        "Select a genre:",
        ["Fantasy", "Science Fiction", "Mystery", "Romance", "Horror", "Adventure"]
    )
    
    characters = st.text_input("Enter main characters (separate with commas):", 
                             placeholder="e.g., John, Sarah, Dragon")

    if st.button("Generate Story"):
        try:
            prompt = f"Write me a 600 word {genre} story"
            if characters:
                prompt += f" featuring these characters: {characters}"
            prompt += "."

            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": prompt}
                ], max_tokens = 1000, temperature = 0.8
            )
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
else:
    st.warning("Please enter your OpenAI API key to generate stories.")
