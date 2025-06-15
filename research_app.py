from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate
import os
try:
    import PyPDF2
except ImportError:
    st.error("📄 PDF reading failed! Please install PyPDF2 using `pip install PyPDF2`")


# Load environment variables
load_dotenv()

# Initialize the model
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    max_new_tokens=500,
    temperature=0.6,
    timeout=30
)
model = ChatHuggingFace(llm=llm)

# Set dark-themed Streamlit styling
st.set_page_config(page_title="Research Summarizer", layout="centered")
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stTextInput > div > div > input, .stSelectbox > div > div {
        background-color: #1c1f26;
        color: #ffffff;
    }
    .stButton button {
        background-color: #6c63ff;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }
    .stButton button:hover {
        background-color: #5246e2;
    }
    </style>
""", unsafe_allow_html=True)

# App title and description
st.markdown("<h1 style='text-align: center; color: #6c63ff;'>🧠 AI Research Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9e9e9e;'>Summarize any research paper — your own PDF or a famous one!</p>", unsafe_allow_html=True)

# Upload PDF option
uploaded_pdf = st.file_uploader("📤 Upload Your Research Paper (PDF)", type=["pdf"])

# Manual entry for research paper name
paper_input = st.text_input("🔍 Enter Research Paper Title", placeholder="e.g., Attention is All You Need")

# Dropdowns for style and length
style_input = st.selectbox("🎨 Choose Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])
length_input = st.selectbox("📏 Choose Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

# Convert uploaded PDF to text (basic approach)
def extract_text_from_pdf(file):
    import PyPDF2
    reader = PyPDF2.PdfReader(file)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text()
    return full_text[:5000]  # limit for processing

# Prompt template
template = PromptTemplate(
    template="""
    Please summarize the following research paper content:
    {paper_input}

    With the following preferences:
    Explanation Style: {style_input}
    Explanation Length: {length_input}
    1. Mathematical Details:
        - Include relevant mathematical equations if present.
        - Explain them using simple, intuitive code if possible.
    2. Analogies:
        - Use analogies to simplify complex ideas.
    Don't use the phrase "Insufficient information available" in the summary.
    Ensure clarity, accuracy, and alignment with the selected style and length.
    """,
    input_variables=['paper_input', 'style_input', 'length_input']
)

# Final summary generation
if st.button("🚀 Summarize"):
    final_text = ""

    if uploaded_pdf:
        final_text = extract_text_from_pdf(uploaded_pdf)
    elif paper_input.strip():
        final_text = paper_input
    else:
        st.warning("⚠️ Please enter a paper title or upload a PDF to summarize.")
    
    if final_text:
        prompt = template.invoke({
            'paper_input': final_text,
            'style_input': style_input,
            'length_input': length_input
        })
        with st.spinner("Analyzing your research magic... 🧪"):
            result = model.invoke(prompt)
            clean_output = result.content.replace("Insufficient information available.", "")
        st.subheader("📄 Summary")
        st.markdown(f"<div style='color: #d6d6d6;'>{clean_output}</div>", unsafe_allow_html=True)
