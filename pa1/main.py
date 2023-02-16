from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "this is where you interface with NER <h1>Header </h1>"

if __name__ == "__main__":
    app.run()