import streamlit as st


st.title("Testing Website")

col1, col2 = st.columns(2)

with col1:
    st.write("Some stuff")

with col2:
    st.subheader("Bay")


st.header('LLM Models')
st.subheader("Gemini")
st.subheader("Claude")
st.subheader('Mistral')
st.subheader('Gemma')
st.subheader('LLamma')



st.sidebar.title('Menu')
st.sidebar.markdown("""

- Home
- About
- Career
- Login
- Register
- Contact Us
                
""")

