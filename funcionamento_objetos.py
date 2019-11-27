'''
A diferenca entre um metodo e uma funcao dentro da POO eh que:
- o metodo executa um codigo sem retornar nenhum tipo de valor.
- a funcao executa um codigo e retorna um valor.
'''

# exemplo 01
class Instancia:
    def __init__(self):
        print('Classe instanciada')

    def metodo(self, msg):
        print(msg)


'''Objeto se torna uma instancia da classe Instancia e acessa seus metodos e funcoes'''
objeto = Instancia()
objeto.metodo('mensagem de teste')


# exemplo 02
class Instancia2:
    def __init__(self):
        print('Classe instanciada')

    '''metodo nao retorna nada'''
    def metodo(self, msg):
        print(msg)

    '''funcao sempre retorna um valor'''
    def funcao(self):
        return 'funcao executada'

objeto2 = Instancia2()

'''
ao se tornar uma instancia o objeto2 consegue acessar metodos e funcoes da classe Instancia.
o valor do retorno da funcao deve ir para uma variavel.
'''
objeto2.metodo('mensagem de teste')
retorno = objeto2.funcao()
print(retorno)
