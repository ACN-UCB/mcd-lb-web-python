from flask import Flask
from flask_restful import Resource, Api
import datetime
import socket

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, name):
        hostname = socket.gethostname()
        return {
            'hello': name,
            'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'hostname': hostname
        }

api.add_resource(HelloWorld, '/api/hello/<string:name>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
