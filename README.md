📄 Resume Analyzer (AI Powered)

An AI-powered Resume Analyzer that extracts, analyzes, and evaluates resumes from PDF files. It helps in understanding candidate skills, experience, and provides intelligent suggestions to improve resumes for better job opportunities.

🚀 Features
📄 Upload and analyze PDF resumes
🧠 Extract structured text from resumes
🤖 AI-based resume understanding (skills, experience, education)
📊 Resume scoring and evaluation
💡 Smart suggestions to improve resume quality
🔍 Keyword and skill detection for job readiness
🌐 Simple and interactive Streamlit UI
🛠️ Tech Stack
Python 3.10+
Streamlit (Frontend UI)
PyPDF / pdfminer.six (PDF parsing)
LangChain (optional for AI pipeline)
Google Gemini / OpenAI / Ollama (for AI analysis)
Scikit-learn (for basic scoring/NLP)
Pandas & NumPy (data handling)
📁 Project Structure

resume-analyzer/
│
├── app.py                # Streamlit UI
├── parser.py             # PDF text extraction
├── analyzer.py           # AI/NLP resume analysis logic
├── utils.py              # Helper functions
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

⚙️ Installation Guide
1️⃣ Clone the repository
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
2️⃣ Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
▶️ Run the Application
streamlit run app.py

Then open in browser:

http://localhost:8501
🧠 How It Works
User uploads a PDF resume
The system extracts raw text from the PDF
Text is processed using NLP/AI models
The system identifies:
Skills
Experience
Education
Keywords relevance
AI generates:
Resume score (out of 100)
Suggestions for improvement
Missing skills or improvements
📊 Output Example
✅ Resume Score: 78/100
💼 Skills Found: Python, SQL, Machine Learning
⚠️ Missing Skills: Cloud, Docker
💡 Suggestions:
Add project descriptions
Improve ATS keywords
Include measurable achievements
🔮 Future Enhancements
🔥 ATS (Applicant Tracking System) Score Checker
💼 Job role matching system
🤝 Resume vs Job description comparison
📄 Downloadable AI report (PDF)
🧑‍💻 Multi-resume comparison system
☁️ Cloud deployment (Streamlit Cloud / AWS)
⚠️ Important Notes
If using Gemini/OpenAI API, ensure API keys are stored securely in .env
Free API tiers may have rate limits
For offline use, Ollama (Llama models) is recommended
👨‍💻 Author

Akshara Kaushik