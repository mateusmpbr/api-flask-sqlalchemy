from models import Pessoas


def insere_pessoa():
    pessoa = Pessoas(nome='LuK',idade=20)
    print(pessoa)
    pessoa.save()


def consulta_todos():
    pessoa = Pessoas.query.all()
    print(pessoa)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Jorgim').first()
    pessoa.nome = 'Jorgim'
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='LuK').first()
    pessoa.delete()


if __name__ == '__main__':
    exclui_pessoa()
    consulta_todos()