import streamlit as st
from llm_security_lab import (
    KnowledgeBasePoisoning,
    PromptInjectionTester,
    ModelExtractionDefense
)

st.title("🔒 LLM Security Lab")

kb = KnowledgeBasePoisoning()
pi = PromptInjectionTester()
me = ModelExtractionDefense()

tab1, tab2, tab3 = st.tabs([
    "KB Poisoning", "Prompt Injection", "Model Extraction"
])

with tab1:
    text = st.text_area("Enter document")
    if st.button("Analyze"):
        result = kb.detect_poisoned_content(text)
        st.write(result)

with tab2:
    user_input = st.text_area("User Input")
    if st.button("Test Injection"):
        result = pi.test_injection_defense(user_input, "")
        st.write(result)

with tab3:
    query = st.text_input("Query")
    if st.button("Track Request"):
        result = me.track_request("user1", query, "")
        st.write(result)
