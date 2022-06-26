from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

from node2vec import Node2Vec
from gensim.models import Word2Vec


app = Flask(__name__)
#
CORS(app)
# creating an API object
api = Api(app)

#prediction api call
class prediction(Resource):
    def get(self, topic):
        #topic = request.args.get('topic')
        print(topic)

        # Load package
        model = Word2Vec.load("word2vec.model")

        prediction = model.wv.most_similar(topic)

        return str(prediction)


#data api
# class getData(Resource):
#     def get(self):
#         df = pd.read_excel('data.xlsx')
#         res = df.to_json(orient='records')

#         return res

api.add_resource(prediction, '/prediction/<string:topic>')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')