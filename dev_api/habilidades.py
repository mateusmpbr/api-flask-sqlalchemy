from flask_restful import Resource


lista_habilidades= ['Python','Java','PHP','Flask']


class Habilidade(Resource):
    def get(self):
        return lista_habilidades