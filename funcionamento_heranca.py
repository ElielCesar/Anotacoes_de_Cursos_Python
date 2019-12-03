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
