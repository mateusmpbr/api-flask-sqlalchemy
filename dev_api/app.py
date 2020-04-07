from flask import Flask, jsonify, request
import json

app = Flask('__name__')


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
@app.route('/dev/<int:id>', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except:
            response = {'erro': 'Nao foi possivel buscar desenvolvedor'}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'Sucesso ao remover desenvolvedor'})


# Lista todos os desenvolvedores e cria um novo desenvolvedor
@app.route('/dev', methods=['POST','GET'])
def desenvolvedores_cl():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify((desenvolvedores[-1]))
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)
