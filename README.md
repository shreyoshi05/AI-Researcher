# 📄 AI Research Agent

An autonomous AI research assistant that discovers recent papers from arXiv, reads them, proposes new research directions, and generates a complete research paper rendered as a LaTeX PDF.

Built using **LangGraph + LLM tool-calling + Streamlit + Tectonic**.

---

## 🚀 Features

- 🔎 Search and retrieve latest research papers from **arXiv**
- 📚 Extract and analyze full paper content from PDF
- 🧠 Identify promising future research directions
- ✍️ Automatically generate a structured research paper
- 🧮 Supports mathematical equations via LaTeX
- 📄 Compile and export the paper as a **PDF**
- 💬 Interactive **Streamlit chat interface**
- 🔁 Stateful multi-turn conversation using LangGraph memory

---

## 🏗️ Architecture
User → Streamlit UI → LangGraph Agent
↓
LLM (tool-calling)
↓
Tools:
• arxiv_search
• read_pdf
• render_latex_pdf
↓
Generated Research Paper → PDF (Tectonic)

---

## 🧠 Tech Stack

- **LangGraph** – agent workflow & state management
- **OpenAI / Gemini (tool-calling LLM)**
- **Streamlit** – frontend UI
- **arXiv API** – research paper retrieval
- **PyPDF2** – PDF text extraction
- **Tectonic** – LaTeX → PDF compilation
- **Python**

---

## 📂 Project Structure

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/AI-Researcher.git
cd AI-Researcher
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Set environment variables

Create a .env file:

OPENAI_API_KEY=your_key_here
# or
GOOGLE_API_KEY=your_key_here
5️⃣ Install Tectonic (LaTeX engine)

Verify installation:

tectonic --version
▶️ Run the Application
streamlit run frontend.py
