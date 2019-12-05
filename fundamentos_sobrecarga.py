'''
Sobrecarga em programacao orientada a objetos significa que a depender da quantidade, tamanho ou dos tipo
de parametro a classe vai ou nao realizar uma atividade, eh basicamente um if else dentro da classe.
'''

class classe:

    def metodo(self, msg=''):
        if len(msg.strip()) == 0:
            print('sem mensagem') # se nao for passado argumento

        else:
            print(f'mensagem recebida: {msg}') # se for passado argumento

c = classe()
c.metodo()
c.metodo('teste')

'''_____________________________________________________________________________'''

# Exemplo 02
class Classe2:

    def metodo(self, parametro=''):
        if type(parametro) == str:  # se o tipo do argumento for string
            print(f'o parametro eh uma string')

        else:
            print(f'o parametro nao eh uma string')

c = Classe2()
c.metodo('texto')
c.metodo(5)

'''_____________________________________________________________________________'''

# Exemplo 03
class Classe3:

    def funcao(self, msg=''):
        if len(msg.strip()) == 0: # se o tamanho for igual a zero
            return 'sem mensagem'

        else:
            print(f'mensagem recebida: {msg}')


c = Classe3()
c.metodo()
c.metodo('teste')

