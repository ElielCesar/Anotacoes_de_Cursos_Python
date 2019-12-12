'''
Interfaces - Sao estruturas de declaracao que serao 
declaradas pelo projetista de software para serem implementadas
pela equipe de desenvolvimento.

Resumindo: Nada mais eh do que alguem que escreve uma parte do codigo 
mas não termina e passa pra equipe de desenvolvimento ou seja apenas
da um norte do que deve ser feito.

'''
class Interface:
    def soma(self, n1=0, n2=0): pass # retornar n1 + n2
    def subtracao(self, n1=0, n2=0): pass # retornar n1 - n2
    def divisao(self, n1=0, n2=0): pass # retornar n1 / n2
    def multiplicacao(self, n1=0, n2=0): pass # retornar n1 * n2


class Classe(Interface):
    def metodo(self):
        print('Interface em orientacao a objetos')


c = Classe()
c.metodo()

'''
Veja que não obtivemos qualquer mensagem de erro ou aviso,
essa é a ideia da interface, projetar para posteriormente implementar.

A Forma correta de utilização das interfaces é na classe que vai 
herdar a interface fazermos a sobrescrita (implementar dentro da classe filha) dos metodos e funcoes.

'''

class Interface2:
    def soma(self, n1=0, n2=0): pass # retornar n1 + n2
    def subtracao(self, n1=0, n2=0): pass # retornar n1 - n2
    def divisao(self, n1=0, n2=0): pass # retornar n1 / n2
    def multiplicacao(self, n1=0, n2=0): pass # retornar n1 * n2


class Classe2(Interface2):
    def soma(self, n1=0, n2=0): 
        return n1 + n2

    def subtracao(self, n1=0, n2=0): 
        return n1 - n2

    def divisao(self, n1=0, n2=0): 
        return n1 / n2

    def multiplicacao(self, n1=0, n2=0): 
        return n1 / n2

'''
Veja que a unica coisa feita foi implementar o codigo da forma que o projetista queria, aparentemente é algo bem sem 
sentido essa parada de interfaces pois se o cara consegue escrever a interface ele tambem consegue escrever o codigo todo...  
'''


c2 = Classe2()
print(c2.soma(2,2))
print(c2.subtracao(3,3))
print(c2.divisao(4,4))
print(c2.multiplicacao(5,5))

