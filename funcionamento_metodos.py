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
# Exemplo 3
class Classe3:
    def __init__(self):
        print('construtor executado')

    def metodo(self):
        print('metodo executado')

    def __del__(self):
        print('destrutor executado')


Classe3.metodo(None) # nesse caso passamos o None mas poderia ser outro valor.

'''____________________________________________________________________________'''

'''Podemos passar 2 ou mais parametros para o metodo sem problemas '''
# Exemplo 04
class Classe4:
    def metodo(self, msg1, msg2):
        print(msg1)
        print(msg2)

f = Classe4()
f.metodo('Estou aprendendo python', 'Eu sou um hacker')

#Obs: podemos passar os fora de ordem desde que os nomeemos
f.metodo(msg2='mensagem 2', msg1='mensagem 1')

'''____________________________________________________________________________'''


# Exemplo 5
'''É possivel chamar um metodo a partir de outro na mesma classe'''
class Classe5:
    def metodo1(self):
        print('metodo 1')

    def metodo2(self):
        self.metodo1()
        print('metodo 2 ')

g = Classe5()
g.metodo2()

'''____________________________________________________________________________'''

# Exemplo 6
'''E possivel chamar um metodo de uma outra classe apenas instanciando-a'''
class Classe6:
    def metodo(self):
        print('metodo da classe 6')


class Classe7:
    def metodo7(self):
        print('metodo da classe 7')

    def metodo_principal(self):
        Classe6().metodo() # veja que aqui a Classe6 foi instanciada.
        self.metodo7() # aqui eu chamo o metodo da propria Classe7 usando self


c7 = Classe7()
c7.metodo_principal()

'''____________________________________________________________________________'''

# usando metodos em cascata

'''Nesse exemplo o metodo2 recebe msg1 e joga para o metodo1, 
o metodo2 recebe msg2 e imprime na tela.

Resumindo: A ideia de cascata é um método jogando parametros para 
outro metodo na mesma classe.
'''

class Classe8:
    def metodo1(self, msg1):
        print(msg1.upper()) # transforma em maiuscula apenas para fins didaticos

    def metodo2(self, msg1, msg2):
        self.metodo1(msg1)
        print(msg2)


k = Classe8()
k.metodo2('mensagem 1', 'mensagem 2')

'''____________________________________________________________________________'''

# Usando parametros com valores/argumentos padrao
class Padrao:
    def metodo(self, msg='valor default'):
        print(msg)

p = Padrao()
p.metodo()
p.metodo('eu passei esse valor')
# caso eu nao passe nenhum valor o 'valor default' seria impresso.

