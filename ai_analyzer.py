from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

def analyze_resume(resume_text):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""You are a professional resume reviewer and career coach.
Analyze the resume below and provide:

1. **Overall Score** (out of 10)
2. **Strong Points** (what's good)
3. **Missing Skills** (what's lacking)
4. **Improvements** (specific suggestions)
5. **Best Job Roles** (top 3 roles this person fits)

Be specific, honest, and helpful.

Resume:
{resume_text}"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024
    )

    return response.choices[0].message.content
# Test
if __name__ == "__main__":
    from pdf_extractor import extract_text_from_pdf
    resume_text = extract_text_from_pdf("test_resume.pdf")
    result = analyze_resume(resume_text)
    print(result)