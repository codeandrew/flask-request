from flask import Flask
from flask_restful import Resource, Api
import requests as req

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        url='http://example.org'
        
        res = req.get(url)

        print(res.text)
        return [
            str(res),
            str(res.headers),
            res.text
        ]

api.add_resource(Product, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=80, debug=True)
