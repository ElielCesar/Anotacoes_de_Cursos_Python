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



# Exemplo 02 - Buscando os recursos da classe Base coo Super()
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
    # Fora dos metodos e funcoes nao se usa o Super(), entao a referencia deve ser direta.
    atributo = Base.atributo # vai buscar da classe Base

     # super() eh uma funcao pra trabalhar com polimorfismo
    def __init__(self):
        super().__init__() # vai chamar o construtor da classe Base
        print('construtor da derivada')

    def metodo(self):
        super().metodo() # vai chamar o metodo da classe Base
        print('metodo da derivada')

    def funcao(self):
        print(super().funcao()) # vai chamar a funcao da classe Base
        return 'funcao da derivada'

    def __del__(self):
        print('destrutor da derivada')


d = Derivada()
print(d.atributo)
print(d.funcao())
d.metodo()


'''____________________________________________________________________'''

# Exemplo 03
class Pai:
    def metodo(self):
        print('metodo do pai')

class Filho(Pai):
    def metodo(self):
        print('metodo do filho')

    def metodo_principal(self):
        super().metodo() # vai chamar o metodo do pai que tem o mesmo nome.
        # para usar um recurso dentro da mesma classe use o self.
        self.metodo()  # vai chamar o metodo do filho.

f = Filho()
f.metodo_principal()













