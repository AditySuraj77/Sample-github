import streamlit as st


st.title("Testing Website")

col1, col2 = st.columns(2)

with col1:
    st.write("Some stuff")

with col2:
    st.header("Bay")


st.header('LLM Models')
st.subheader("Gemini")
st.subheader("OpenAI")
st.subheader("Claude")