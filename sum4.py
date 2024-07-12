import streamlit as st
from summarizer import Summarizer

# Initialize the Summarizer model
model = Summarizer()

# Streamlit app header
st.write("""
# Summarize Your Text
""")

# Text input area for user input
text_input = st.text_area("Text to summarize")

# Check if there's input to summarize
if st.button("Summarize"):
    # Generate the summary using the Summarizer model
    if text_input.strip():  # Check if there's non-empty input
        summary = model(text_input)
        # Display the summarized text
        st.write("## Summarized Text")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
