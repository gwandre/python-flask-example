import requests
import json

from flask import Flask, request, Response
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

# Open files to get response data
f = open("response200.html", "r")
htmlReturn = f.read()

f = open("response200.xml", "r")
xmlReturn = f.read()

f = open("response200.json", "r")
jsonReturn = f.read()

f = open("response404.html", "r")
notfoundReturn = f.read()

# Define Classes
class Consulta(Resource):
	def get(self, retType):
		if retType == "xml":
			return Response(response=xmlReturn,content_type="text/xml",status=200)
		elif retType == "html":
			return Response(response=htmlReturn,content_type="text/html", status=200)
		elif retType == "json":
			return Response(response=jsonReturn,content_type="application/json",status=200)
		else:
			return Response(status=404)

# Add Routes
api.add_resource(Consulta, '/consulta/<retType>')

# Main
if __name__ == '__main__':
	app.run(host='0.0.0.0',port='5002')
