from flask import Flask
from flask_restful import Resource, Api, reqparse
import requests

app = Flask(__name__)
api = Api(app)

class Ping(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str)
        parser.add_argument('port', type=str)

        url=parser.parse_args().url
        port=parser.parse_args().port

        resp = requests.get(url + ":" + port)

        print(resp.text)
        return [
            str(resp),
            str(resp.headers),
            resp.text,
        ]

api.add_resource(Ping, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=80, debug=True)
