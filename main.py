import streamlit as st
import os
from langchain_groq import ChatGroq

# Set the Groq API Key explicitly
GROQ_API_KEY = "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"
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Streamlit App Header
st.title("Code Analyzer with Groq-Powered LLM")
st.write(
    "Analyze your code with *Llama 3.3 (70B)* model using Groq. "
    "This tool identifies bottlenecks, suggests improvements, and explains potential issues."
)

# Initialize the Groq Chat LLM
@st.cache_resource
def load_llm():
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

llm = load_llm()

# Input Code
code_input = st.text_area(
    "Paste your code below:",
    "",
    placeholder="Enter your Python code here...",
    height=300,
)
analyze_button = st.button("Analyze Code")

# Process the Code Input and Display Results
if analyze_button:
    if not code_input.strip():
        st.warning("Please enter a valid code snippet.")
    else:
        with st.spinner("Analyzing the code..."):
            try:
                # Formulate the query for the LLM
                query = (
                    f"Analyze the following Python code:\n\n{code_input}\n\n"
                    "1. Identify potential bottlenecks in this code.\n"
                    "2. Explain the issues clearly.\n"
                    "3. Suggest improvements to optimize the code.\n"
                    "Provide the response in a structured format with sections for 'Bottlenecks', "
                    "'Explanations', and 'Suggested Improvements'."
                )
                # Invoke the model
                response = llm.invoke(query)
                
                # Display results
                st.subheader("Analysis Result")
                st.markdown(response.content)
            except Exception as e:
                st.error(f"An error occurred while analyzing the code: {e}")