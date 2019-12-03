class Classe1: # Classe Pai, Classe mae ou Classe primaria
    atributo1 = 'atributo da classe 1'

    def metodo1(self):
        print('metodo da classe 1')

    def funcao1(self):
        return 'funcao da classe 1'

# Classe filha ou Classe secundaria
class Classe2(Classe1): # heranca aqui
    atributo2 = 'atributo da classe 2'

    def metodo2(self):
        print('metodo da classe 2')

    def funcao2(self):
        return 'funcao da classe 2'

# Instanciando a Classe2 no objeto.
c2 = Classe2()

print(c2.atributo1) # veja que a Classe2 acessa os atributos da classe1
print(c2.atributo2)
c2.metodo1()        # veja que a Classe2 acessa os metodos da classe1
c2.metodo2()

'''
OBS: Quando a classe pai e a classe filha tiverem os mesmos nomes de atributos, métodos ou funcoes
os metodos da classe filha vao sobrescrever os da classe pai, dessa forma preste atencao aos nomes
destes quando estiver programando.
'''


# utilizando herancas multiplas em cascata

class Classe1:
    def metodo1(self):
        print('Metodo da Classe1')

class Classe2(Classe1): # herda da Classe1
    def metodo2(self):
        print('Metodo da Classe2')

class Classe3(Classe2): # herda da Classe2
    def metodo3(self):
        print('Metodo da Classe3')

class Classe4(Classe3):# herda da Classe3
    def metodo4(self):
        print('Metodo da Classe4')


c4 = Classe4() # Acessa atributos e metodos de Todas as classes devido a heranca multipla.
c4.metodo1()
c4.metodo2()
c4.metodo3()

