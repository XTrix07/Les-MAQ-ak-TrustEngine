# 🛡️ TrustEngine — SD Worx Knowledge Base
> *Unlock the Knowledge Within : Find it. Understand it. Trust it.*

Developed by **Les MAQ-ak** for the **Tectonic Hackathon 2026** (SD Worx Challenge).

---

## 📌 The Problem (SD Worx Challenge)

In a large organization like SD Worx, internal knowledge is fragmented across official manuals, shared documents, and informal Teams chats. 

Finding a document is easy, but **knowing if it can be trusted is a real challenge**:
* Payroll consultants face contradictory or outdated information.
* Standard AI summaries provide answers without explainability or local legal guarantees.
* Doubt slows down decision-making and wastes valuable team time.

---

## 💡 Our Solution: TrustEngine

**TrustEngine** transforms internal document search into a system driven by **trust** and **explainability**:

1. **Transparent Trust Score**: Every synthesized answer is weighted based on data freshness, applicable jurisdiction, and internal approval level.
2. **Active Contradiction Detection**: Highlights conflicts between official documents and unverified discussions (e.g., an outdated amount from a Teams channel).
3. **Human-in-the-loop Routing**: If uncertainty is too high, the system immediately directs the employee to the right business expert within the company.
4. **Express Audio Briefing**: Instant voice synthesis of key legal alerts for consultants on the go.

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit (Python)
* **AI Logic & Processing**: Python / GCP
* **Voice Synthesis**: ElevenLabs API
* **Security & Code Audit**: Aikido Security

---

## 🚀 Local Installation

### Prerequisites
* Python 3.9+
* Git

### Step-by-step

1. Clone the repository:
git clone https://github.com/XTrix07/Les-MAQ-ak.git
cd Les-MAQ-ak

2. Install dependencies:
pip install streamlit

3. Run the application:
streamlit run app.py

The application will open automatically in your browser at http://localhost:8501.

---

## 🔒 Aikido Security Audit

As per hackathon requirements, the entire codebase has been subjected to the **Aikido** security audit tool:
* Strict segregation of data.
* No hardcoded API keys or secrets in the public source code.
* *(Aikido audit screenshots are attached to the Builderbase submission).*
