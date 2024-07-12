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
    # Ensure text_input is not empty
    if text_input.strip():
        try:
            # Generate the summary using the Summarizer model
            summary = model.predict(text_input)
            
            # Display the summarized text
            st.write("## Summarized Text")
            st.write(summary)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to summarize.")
