# Resume Parser

A web app that extracts structured data from PDF and DOCX resumes — name, email, phone, and skills — and stores the results in a PostgreSQL database.

Built with Python, Flask, spaCy, and pdfplumber.

---

## Features

- Upload a resume in PDF or DOCX format via a simple web interface
- Extracts:
  - **Name** — using spaCy's NER (`PERSON` entity)
  - **Email** — regex pattern matching
  - **Phone** — regex pattern matching
  - **Skills** — keyword matching against a curated skills list
- Saves extracted data to a PostgreSQL database
- Results displayed instantly on the page after upload

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| NLP | spaCy (`en_core_web_sm`) |
| PDF Parsing | pdfplumber |
| Database | PostgreSQL |
| Frontend | HTML (Jinja2 templates) |

---

## Project Structure

```
Resume-Parser/
├── app.py          # Flask app — routes and upload handling
├── parser.py       # Core extraction logic (NLP + regex)
├── database.py     # PostgreSQL connection and insert logic
├── templates/
│   └── index.html  # Upload form and results page
├── resume.pdf      # Sample resume for testing
└── resume.docx     # Sample resume for testing
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL installed and running

### Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/aditswar/Resume-Parser.git
   cd Resume-Parser
   ```

2. Install dependencies:
   ```bash
   pip install flask spacy pdfplumber psycopg2-binary
   python -m spacy download en_core_web_sm
   ```

3. Set up the database:

   Create a PostgreSQL database and update the connection settings in `database.py`:
   ```python
   conn = psycopg2.connect(
       host="localhost",
       database="your_db_name",
       user="your_username",
       password="your_password"
   )
   ```

   Then create the candidates table:
   ```sql
   CREATE TABLE candidates (
       id SERIAL PRIMARY KEY,
       name TEXT,
       email TEXT,
       phone TEXT,
       skills TEXT
   );
   ```

4. Run the app:
   ```bash
   python app.py
   ```

5. Open your browser at `http://localhost:5000`, upload a resume, and see the results.

---

## How It Works

1. User uploads a PDF resume through the web form
2. `pdfplumber` extracts raw text from the file
3. `spaCy` NER identifies the candidate's name
4. Regex patterns find emails and phone numbers
5. Skills are matched against a predefined keyword list
6. Extracted data is inserted into PostgreSQL via `psycopg2`
7. Results are rendered back on the page

---

## Known Limitations

- Skill extraction is keyword-based — non-standard skill names may be missed
- Name extraction depends on spaCy's NER, which can misidentify names in unusual resume formats
- Currently supports PDF only (DOCX support via `python-docx` can be added)
- PostgreSQL must be configured manually before running

---

## Future Improvements Soon

- [ ] Add DOCX parsing support
- [ ] Expand skills database
- [ ] REST API endpoint for programmatic access
