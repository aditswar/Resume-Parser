import pdfplumber
import spacy
import re
nlp = spacy.load("en_core_web_sm")

def extract_text(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_name(text):
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return None


def extract_email(text):
    return re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        text
    )

def extract_phone(text):
    return re.findall(
        r'\+?\d[\d\s\-]{8,15}',
        text
    )

def extract_skills(text):
    skills_db = [
        "python",
        "java",
        "sql",
        "machine learning",
        "flask",
        "react",
        "nodejs",
        "deep learning",
        "mongodb"
    ]

    found_skills = []

    for skill in skills_db:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


# now parsing,
if __name__ == "__main__":
    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(BASE_DIR, "resume.pdf")

    text = extract_text(pdf_path)

    name = extract_name(text)
    emails = extract_email(text)
    phones = extract_phone(text)
    skills = extract_skills(text)

    print(f"Name: {name}")
    print(f"Emails: {emails}")
    print(f"Phones: {phones}")
    print(f"Skills: {skills}")
