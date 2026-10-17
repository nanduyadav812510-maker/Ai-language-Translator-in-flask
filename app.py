from flask import Flask, render_template, request
from utils.ai_client import translate_text

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Translate Route
@app.route("/translate", methods=["POST"])
def translate():
    text = request.form.get("text", "").strip()
    source_language = request.form.get("source_language", "").strip()
    target_language = request.form.get("target_language", "").strip()

    if not text or not source_language or not target_language:
        return render_template("index.html", error="Please complete all fields."), 400

    try:
        translated_text = translate_text(text, source_language, target_language)
    except Exception:
        app.logger.exception("Translation failed")
        return render_template(
            "index.html",
            error="Translation could not be completed. Please try again.",
        ), 502

    return render_template(
        "result.html",
        original_text=text,
        translated_text=translated_text,
        source_language=source_language,
        target_language=target_language
    )

if __name__ == "__main__":
    app.run(debug=True)
