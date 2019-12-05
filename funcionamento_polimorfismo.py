# Exemplo 01 - Sobreposicao 
class Base:
    atributo = 'atributo da base'

    def __init__(self):
        print('construtor da base')

    def metodo(self):
        print('metodo da base')

    def funcao(self):
        return 'funcao da base'

    def __del__(self):
        print('destrutor da base')


class Derivada(Base):
    atributo = 'atributo da derivada'

    def __init__(self):
        print('construtor da derivada')

    def metodo(self):
        print('metodo da derivada')

    def funcao(self):
        return 'funcao da derivada'

    def __del__(self):
        print('destrutor da derivada')


d = Derivada()
print(d.atributo) # vai buscar o atributo da classe filha
print(d.funcao()) # vai buscar a funcao da classe filha
d.metodo() # vai buscar o metodo da classe filha


'''____________________________________________________________________'''
















