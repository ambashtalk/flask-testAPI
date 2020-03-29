from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from base64 import b64decode
import json

app = Flask(__name__)

api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument('key1')
parser.add_argument('key2')
parser.add_argument('media')
parser.add_argument('type')

# 1st Resource of our api that saves sent image and returns the same data with acknowledgement
class first_api(Resource):
    def get(self):
        #Parameters to parse from received data
        data = parser.parse_args()
        
        #Retriving image save it
        f = 'imageToSave.'+data['type']
        img = open(f,'wb')
        img.write(b64decode(data['media']))
        img.close()
        #Our Response
        msg = {'response':'Recieved Using GET', 'sent':data}
        
        return jsonify(msg)

    def post(self):
        data = parser.parse_args()

        #Save received image
        f = 'imageToSave.'+data['type']
        img = open(f,'wb')
        img.write(b64decode(data['media']))
        img.close()

        #Return Response
        msg = {'response':'Received using POST', 'sent':data}
        
        return jsonify(msg)

# Another resource of our API that returns square of number
class square(Resource):
    def get(self, num):
        response = {'val':num**2}
        return jsonify(response)

    def post(self):
        data = request.get_json()
        response = {'val':data['num']**2}
        return jsonify(response)

#Adding our 1st resource
api.add_resource(first_api, '/api/test1')
#Another type of get request
api.add_resource(square, '/api/test2','/api/test2/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)