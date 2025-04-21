from flask import Flask, render_template, jsonify
from Grammar import generate_sentence

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("grammar.html")

@app.route("/grammar/sentence/meta")
def sentence_meta():
    return jsonify(generate_sentence())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)