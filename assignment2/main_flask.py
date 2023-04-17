from flask import Flask, render_template, request
from ner import SpacyDocument

from methods import todf
import sqlite3
connection = sqlite3.connect('ner.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS entities (entity TEXT PRIMARY KEY, count INTEGER DEFAULT 0)')


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

    entities = [entity[3] for entity in entities]

    connection1 = sqlite3.connect('ner.db')
    cursor = connection1.cursor()

    for ent in entities:
        # if entity exists, update its count. else, insert into db 
        cursor.execute(
            "INSERT INTO entities (entity, count) VALUES (?, 1) ON CONFLICT(entity) DO UPDATE SET count = COALESCE(count, 0) + 1", (ent,))
    connection1.commit()

    return render_template("result.html", xml=xml)

@app.route("/db")
def db():
    connection2 = sqlite3.connect('ner.db')
    cursor = connection2.cursor() 
    rows = cursor.execute("SELECT entity, count FROM entities").fetchall()
    df = todf(rows)
    html_table = df.to_html(index=False)
    return render_template("db.html", table=html_table)

if __name__ == "__main__":
    app.run(debug=True)