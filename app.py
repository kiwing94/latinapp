from flask import Flask, render_template, jsonify
from renderer import generate_sentence  # Use your main sentence generator

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("grammar.html")

@app.route("/grammar/sentence/meta")
def sentence_meta():
    return jsonify(generate_sentence())

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)