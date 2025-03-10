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
    if st.button("Generate Story"):
        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Write me a 1000 word story about any topic."}
                ], max_tokens = 10000, temperature = 0.8
            )
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
else:
    st.warning("Please enter your OpenAI API key to generate stories.")
