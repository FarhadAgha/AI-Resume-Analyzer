import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        return f"Error reading PDF: {str(e)}"
    if not text.strip():
        return "Could not extract text. PDF might be image-based."
    return text.strip()
# Test
if __name__ == "__main__":
    result = extract_text_from_pdf("test_resume.pdf")
    print(result[:500])