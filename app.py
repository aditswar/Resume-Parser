from flask import Flask, render_template, request
from parser import *
from database import insert_candidate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["resume"]

        file.save(file.filename)

        text = extract_text(file.filename)

        result = {
            "name": extract_name(text),
            "emails": extract_email(text),
            "phones": extract_phone(text),
            "skills": extract_skills(text)
        }

        insert_candidate(
        result["name"],
        result["emails"][0] if result["emails"] else None,
        result["phones"][0].strip() if result["phones"] else None,
        ", ".join(result["skills"])
        )

        return render_template("index.html", result=result)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)