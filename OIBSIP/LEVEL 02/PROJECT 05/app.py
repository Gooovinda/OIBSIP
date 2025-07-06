# app.py

import streamlit as st

st.title("Autocomplete & Autocorrect Demo")

# Sentences used in the project
sentences = [
    "I love to eat pizza on weekends",
    "Please send me the latest report",
    "Artificial intelligence is changing the world",
    "The weather today is quite pleasant",
    "He is going to the gym regularly"
]

# Build a list of unique words from all sentences
import re
word_set = set()
for sentence in sentences:
    words = re.findall(r'\b\w+\b', sentence.lower())  # extract words ignoring punctuation
    word_set.update(words)

suggestions = sorted(list(word_set))  # Alphabetically sorted list of unique words

# Streamlit input
user_input = st.text_input("Start typing a word:")

if user_input:
    st.subheader("Autocomplete Suggestions:")
    matched = [word for word in suggestions if word.startswith(user_input.lower())]
    if matched:
        for word in matched:
            st.write(f"🔹 {word}")
    else:
        st.write("❌ No suggestions found.")
