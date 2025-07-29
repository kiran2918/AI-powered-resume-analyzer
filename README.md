# 👑 GenAI Resume Master: Royal Gold Edition

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Gemini API](https://img.shields.io/badge/Google-Gemini-yellow)
![UI Theme](https://img.shields.io/badge/UI-Royal%20Gold-FFD700)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## ✨ Overview  
The **GenAI Resume Master** is an **AI-powered resume analyzer** that:  
✅ Parses resumes (PDF format)  
✅ Matches resumes against job descriptions  
✅ Extracts matched & missing keywords  
✅ Provides AI-generated improvement feedback (Google Gemini API)  
✅ Displays results in a **Royal Gold-themed UI dashboard**  

---

## 🎨 UI Preview  
<img width="1828" height="1093" alt="image" src="https://github.com/user-attachments/assets/b2807954-bb2b-42db-a54b-e1ec583c5435" />


---

## 🚀 Live Deployment  
🔗 [**Live Demo on Render**](https://your-deployment-link.com) *(Replace after deployment)*

---

## 🛠 Tech Stack  
- **Backend:** FastAPI (Python 3.10+)  
- **Frontend:** Jinja2 Templates + Bootstrap 5  
- **AI:** Google Gemini API (Generative AI Feedback)  
- **Libraries:**  
  - PyMuPDF (PDF Parsing)  
  - Sentence-Transformers (Semantic JD Matching)  
  - Pandas (Data Processing)  
- **Deployment:** Render / Railway / AWS EC2  

---

## ⚙️ Installation & Setup (Local)  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/kiran2918/AI-powered-resume-analyzer.git
cd AI-powered-resume-analyzer
2️⃣ Create Virtual Environment
bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate        # Windows  
source .venv/bin/activate     # Mac/Linux  
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Add Environment Variables
Create a .env file:

ini
Copy
Edit
GEMINI_API_KEY=your-gemini-api-key
5️⃣ Run the Server
bash
Copy
Edit
cd python_backend
uvicorn app:app --host=0.0.0.0 --port=8000 --reload
Now open: http://127.0.0.1:8000

🌐 Deployment on Render
Push your repo to GitHub

Go to Render → New Web Service

Connect your GitHub repo

Environment: Python 3.10+

Start Command:

bash
Copy
Edit
uvicorn python_backend.app:app --host=0.0.0.0 --port=8000
Add GEMINI_API_KEY in Render Environment Variables

Click Deploy

🧪 Features
✔ AI-based Resume Scoring
✔ Keyword Matching (Matched & Missing)
✔ Generative Feedback (Gemini API)
✔ Elegant Royal Gold UI
✔ Ready for FAANG+ portfolio showcase

👨‍💻 Author
Kiran Rangi
