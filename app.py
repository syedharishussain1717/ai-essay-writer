import streamlit as st
from groq import Groq

# Read the API key from Streamlit Secrets (never hard-coded)
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

MODEL = "openai/gpt-oss-20b"

st.title("📝 AI Essay Writer")
st.write("Give me a topic and I'll write a short essay on it.")

topic = st.text_input("Essay topic")
length = st.selectbox("Length", ["Short (~150 words)", "Medium (~300 words)", "Long (~500 words)"])

if st.button("Generate Essay"):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        prompt = (
            f"Write a well-structured essay of {length} on the topic: {topic}. "
            f"Include an introduction, body paragraphs, and a conclusion."
        )
        try:
            with st.spinner("Writing..."):
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=[{"role": "user", "content": prompt}],
                )
            st.subheader("Your essay")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Something went wrong: {e}")