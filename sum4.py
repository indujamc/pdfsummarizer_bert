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
    if text_input:
        # Generate summary using the model
        summary = model(text_input)
        
        # Display the summarized text
        st.write("## Summarized Text")
        st.write(f"<div style='font-family: Arial;'> {''.join(summary)} </div>", unsafe_allow_html=True)
    else:
        st.write("Please enter some text to summarize.")
