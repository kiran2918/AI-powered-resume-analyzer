from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List
import fitz  # PyMuPDF for PDF parsing
import re
import google.generativeai as genai
from sentence_transformers import SentenceTransformer, util
import uvicorn

app = FastAPI()

# Mount static files (CSS/JS if needed)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates folder
templates = Jinja2Templates(directory="templates")

# Configure Gemini API
genai.configure(api_key="AIzaSyC2gxrvWSmjPNHbkt1QjhABtulCzqAfqm4")

def get_gemini_model(mode="fast"):
    if mode == "fast":
        return genai.GenerativeModel("models/gemini-1.5-flash")  # Faster
    else:
        return genai.GenerativeModel("models/gemini-1.5-pro")    # Higher quality

model = SentenceTransformer('all-MiniLM-L6-v2')

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "results": None, "error": None})

@app.post("/analyze", response_class=HTMLResponse)
async def analyze(
    request: Request,
    resumes: List[UploadFile] = File(...),
    job_description: str = Form(...)
):
    try:
        jd_text = job_description.lower().strip()
        if not jd_text:
            return templates.TemplateResponse("index.html", {"request": request, "results": None, "error": "Job description cannot be empty!"})

        jd_keywords = list(set(re.findall(r'\b[a-zA-Z]{3,}\b', jd_text)))
        results = []

        for resume in resumes:
            content = await resume.read()
            if not content:
                continue  # Skip empty uploads

            # Extract text from PDF
            text = ""
            doc = fitz.open(stream=content, filetype="pdf")
            for page in doc:
                text += page.get_text()
            doc.close()

            if not text.strip():
                continue  # Skip empty PDFs with no text

            # Compute semantic similarity
            emb_resume = model.encode(text, convert_to_tensor=True)
            emb_jd = model.encode(jd_text, convert_to_tensor=True)
            match_score = round(util.cos_sim(emb_resume, emb_jd).item() * 100, 2)

            # Keyword analysis
            resume_words = set(re.findall(r'\b[a-zA-Z]{3,}\b', text.lower()))
            matched = [kw for kw in jd_keywords if kw in resume_words]
            missing = [kw for kw in jd_keywords if kw not in resume_words]

            # Gemini AI feedback
            prompt = f"""
            Resume: {text[:1500]}...
            JD: {jd_text}

            Provide 3-4 bullet points suggesting how this resume can be improved for this job.
            """
            gemini_model = get_gemini_model("fast")  # or "pro"
            feedback = gemini_model.generate_content(prompt).text


            results.append({
                "name": resume.filename,
                "score": match_score,
                "matched": ", ".join(matched),
                "missing": ", ".join(missing),
                "feedback": feedback
            })

        if not results:
            return templates.TemplateResponse("index.html", {"request": request, "results": None, "error": "No valid resumes processed! Ensure PDFs are not empty or scanned images."})

        return templates.TemplateResponse("index.html", {"request": request, "results": results, "error": None})

    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "results": None, "error": f"Error: {str(e)}"})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
