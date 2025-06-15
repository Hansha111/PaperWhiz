🧠 PaperWhiz – AI-Powered Research Summarizer

PaperWhiz is a smart, Streamlit-based web app that summarizes research papers in a click — whether you're reading classics like Attention is All You Need or uploading your own PDFs. Powered by Meta’s LLaMA-3 via HuggingFace, it delivers customized summaries in different styles and lengths.

###🚀 Features

📤 Upload PDFs or enter paper titles manually
🎨 Choose explanation style: Beginner-friendly, Technical, Code-oriented, or Mathematical
📏 Select explanation length: Short, Medium, or Detailed
🧠 Built on LangChain + HuggingFace + LLaMA-3
🌚 Dark-themed, clean, and modern UI with search-style input

###🔧 Tech Stack

Streamlit – UI & App Framework
LangChain – Prompt orchestration
HuggingFace Endpoint – LLaMA-3 Instruct model
PyPDF2 – PDF parsing

###📦 Installation

```
git clone https://github.com/your-username/paperwhiz.git
cd paperwhiz
pip install -r requirements.txt
```

Set up your .env file with:

```
HUGGINGFACEHUB_API_TOKEN=your_api_token_here
```

Then run the app:

```
streamlit run research_app.py
```

####💡 Future Ideas

Section-wise summarization
Citation generator
Voice-over summaries
Arxiv/Semantic Scholar integration

####🤖 Demo Screenshot

![Screenshot](AI_Research_Summarizer_ss(1).png)

![Screenshot](AI_Research_Summarizer_ss(1).png)



📚 Made by Maya (aka the Whiz herself!)

Give this repo a ⭐ if you found it helpful!
