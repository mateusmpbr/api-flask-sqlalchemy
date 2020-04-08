from models import Pessoas, Usuarios


def insere_pessoa():
    pessoa = Pessoas(nome='LuK',idade=20)
    print(pessoa)
    pessoa.save()


def consulta_todas_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Jorgim').first()
    pessoa.nome = 'Jorgim'
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='LuK').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

def altera_usuario():
    usuarios = Usuarios.query.filter_by(login='rafael').first()
    usuarios.senha = '321'
    usuarios.save()

def exclui_usuario():
    usuarios = Usuarios.query.filter_by(login='galleani').first()
    usuarios.delete()

if __name__ == '__main__':
    # insere_usuario('rafael','aaa')
    # insere_usuario('galleani','bbb')
    altera_usuario()
    consulta_todos_usuarios()
    # exclui_usuario()