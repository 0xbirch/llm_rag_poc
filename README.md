# RAG Trading Signal POC

This project is a proof-of-concept (POC) for building a **Retrieval-Augmented Generation (RAG)** application focused on **trading signals**.

The goal is to demonstrate how Large Language Models (LLMs) can be combined with structured or unstructured data sources (e.g. CSVs, financial reports, technical indicators) to produce insightful responses to trading-related queries.

---

## 🔍 Project Purpose

- Integrate LLMs (GPT-4 / Gemini Flash 2.0) with a retrieval layer
- Load trading signal data (e.g. CSV, SQLite) as external context
- Build a lightweight local interface for querying trading-related data
- Evaluate how RAG enhances LLM accuracy and relevance in a financial context

---

## 🧱 Tech Stack

- **Python 3.10+**
- **OpenAI SDK (v1+)**
- **LangChain** (or custom retrieval layer)
- **SQLite / Pandas** for tabular data
---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/your-username/rag-trading-poc.git
cd rag-trading-poc

# Create a new conda environment
conda env create -f environment.yml
conda activate rag-trading-poc

# Add your OpenAI key (you can also put this in a .env file)
export OPENAI_API_KEY=sk-...
```

> 💡 Tip: If you're using a `.env` file to manage secrets, make sure to use `python-dotenv` to load it automatically or call `load_dotenv()` in your code.


## 📁 Project Structure

```
rag-trading-poc/
├── main.py                # Entry point for the app
├── retriever.py           # Handles retrieval of relevant context
├── data/
│   └── trading_signals.csv  # Example trading signal dataset
├── .env                   # (Optional) Environment variables
├── README.md
└── requirements.txt
```

---

## ✅ Features

- 🔍 Load and index trading signal data
- 💬 Ask natural language questions like:
  - “What were the buy signals for AAPL last week?”
  - “Show all trades where RSI < 30 and MACD turned positive.”
  - "Where am I most vulnerable based on the trades I made yesterday"
- 🧠 LLM uses both prompt + retrieved context to generate answers

- 🧠 Choose between:
  - OpenAI GPT-based model
  - Gemini 2.0 Flash for high-power, large-context reasoning

---

## 📌 Notes

- This project is a **minimal working prototype** — not yet production-ready

---

## 🧠 Future Work

- 📊 Add evaluation metrics (e.g. precision/recall of signal response accuracy)
- 🔌 Integrate real-time market data (Alpaca, Polygon.io, etc.)
- 🛠️ Explore OpenAI Function Calling for structured output

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for more details.