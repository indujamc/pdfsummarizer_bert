import streamlit as st 

from summarizer import Summarizer
model = Summarizer()

st.write("""
# Summarize Your Text
""")
text_input = st.text_area("Text to summarize")

#st.write("""
# Number of sentence required""")

#num_sentences=st.number_input("Enter the number of sentences to include in the summary:")*/


summary = model(text_input, num_sentences=4) 

st.write("## Summarized Text")
st.write(f"<div style='font-family: Arial;'> {''.join(summary)} </div>", unsafe_allow_html=True)
