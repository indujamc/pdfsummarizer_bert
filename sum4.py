import streamlit as st
from summarizer import Summarizer

# Initialize the Summarizer model
model = Summarizer()

# Streamlit UI
st.write("""
# Summarize Your Text
""")
text_input = st.text_area("Text to summarize")

# Check if there is input to summarize
if st.button("Summarize"):
    # Ensure text_input is not empty
    if text_input.strip():  # Check if text_input has content
        try:
            # Generate summary using the model
            summary = model(text_input)  # Use the model directly on text_input
            
            # Display the summarized text
            st.write("## Summarized Text")
            st.write(summary)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text to summarize.")
