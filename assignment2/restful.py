from flask import Flask, request
from flask_restful import Resource, Api
from ner import SpacyDocument

app = Flask(__name__)
api = Api(app)

doc = ""
explanation = "use POST method to enter a .txt file. The API will return a json file of all entities."
#entities = []

class NER(Resource):
    def get(self):
        return explanation

    def post(self):
        #head = request.headers['Content-Type']
        doc = str(request.get_data(as_text=True))
        entities = SpacyDocument(doc).get_entities_with_markup()
        return entities

api.add_resource(NER, '/api')

if __name__ == '__main__':
    app.run(debug=True)