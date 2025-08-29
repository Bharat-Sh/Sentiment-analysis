import os
import requests
import streamlit as st

# Backend URL (set by Docker Compose or defaults to local)
BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")

st.set_page_config(page_title="VADER Sentiment Analysis", page_icon="🧠")
st.title(" VADER Sentiment Analysis (FastAPI + Streamlit)")


# --- Input form ---
with st.form("sentiment-form", clear_on_submit=False):
    sentence = st.text_area(
        "Enter a sentence:",
        height=140,
        placeholder="e.g., I absolutely love this product!",
        key="sentence_input"  # bind to session state
    )
    submitted = st.form_submit_button("Analyze")

if submitted:
    if sentence.strip():
        try:
            resp = requests.post(f"{BACKEND_URL}/analyze", json={"sentence": sentence}, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            st.success(f"Sentiment: **{data['sentiment']}**")
            st.subheader("Scores")
            st.json(data["scores"])
        except requests.RequestException as e:
            st.error(f"Request failed: {e}")
    else:
        st.warning("Please enter a sentence to analyze.")

# --- Example sentences ---
st.divider()
st.write("**Try examples:**")

examples = [
    "I absolutely love this product. It exceeded my expectations!",
    "This is the worst experience I've ever had.",
    "It’s okay, not good, not bad.",
]

cols = st.columns(len(examples))
for i, ex in enumerate(examples):
    if cols[i].button(f"Example {i+1}"):
        st.session_state.update({"sentence_input": ex})  # updates text area
        st.rerun()
