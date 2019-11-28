'''Metodo é um bloco de codigo que é executado e não retorna nenhum valor'''
# Exemplo 01
class Classe:
    def metodo(self):
        print('metodo executado')

c = Classe()
c.metodo()

# Exemplo 02
class Classe2:
    def __init__(self):
        print('construtor executado')

    def metodo(self):
        print('metodo executado')

    def __del__(self):
        print('destrutor executado')


d = Classe2()
d.metodo()
del d

'''____________________________________________________________________________'''

'''Uma classe que nao instanciar seu construtor somente
podera utilizar o metodo se algum valor for passado como
parametro no lugar do self, ex: metodo(self)'''

class Classe3:
    def __init__(self):
        print('construtor executado')

    def metodo(self):
        print('metodo executado')

    def __del__(self):
        print('destrutor executado')


Classe3.metodo(None) # nesse caso passamos o None mas poderia ser outro valor.















