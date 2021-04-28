import requests
import json

from flask import Flask, request, Response
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

def lerArquivo(tipo, teste):
	try:
		f = open("files/%s_%s.txt" % (tipo, teste), "r")
	except Exception:
		f = open("files/default.html", "r")

	return f.read()

def tipoContent(tipo):
	if tipo == "json":
		return "application/json"
	elif tipo == "html":
		return "text/html"
	elif tipo == "xml":
		return "text/xml"
	else:
		return "text/plain"

# Define Classes
class Simulador(Resource):
	def get(self, reqType, testType):
		return Response(response=lerArquivo(reqType, testType),content_type=tipoContent(reqType),status=200)
	def post(self, reqType, testType):
		return Response(response=lerArquivo(reqType, testType),content_type=tipoContent(reqType),status=200)

# Add Routes
api.add_resource(Simulador, '/<reqType>/<testType>')

# Main
if __name__ == '__main__':
	app.run(host='0.0.0.0',port='5002')
