from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidade
import json

app = Flask('__name__')
api = Api(app)

desenvolvedores = [
    {
        'nome':'Mateus',
        'habilidades':['Python','Django'],
    },
    {
        'nome':'Pereira',
        'habilidades':['PHP','Laravel'],
    }
]


# Retorna, altera e deleta um desenvolvedor pelo ID
class Desenvolvedor(Resource):

    def get(self, id):
        try:
            response = desenvolvedores[id]
        except Exception:
            response = {'erro': 'Nao foi possivel buscar desenvolvedor'}
        return response

    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'Sucesso ao remover desenvolvedor'}


# Lista todos os desenvolvedores e cria um novo desenvolvedor
class DesenvolvedoresCL (Resource):

    def post(self):
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return desenvolvedores[-1]

    def get(self):
        return desenvolvedores


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(DesenvolvedoresCL,'/dev/')
api.add_resource(Habilidade, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)