from flask import Flask, render_template, request
from ner import SpacyDocument

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    

@app.route("/result", methods=["POST"])
def result():

    sentence = request.form["query"]

    doc = SpacyDocument(sentence)
    xml = doc.get_entities_with_markup()
    entities = doc.get_entities() # each ent is a tuple of (range, type, string)
    tokens = doc.get_tokens()

    return render_template("result.html", xml=xml, ent=entities, tok=tokens)

if __name__ == "__main__":
    app.run(debug=True, port=5000)