'''Podemos criar um atributo diretamente dentro da classe
fora do metodo construtor e acessa-la perfeitamente.'''
# Exemplo 01
class Classe:
    atributo = 'aprendendo python'


c = Classe()
print(c.atributo)

'''_______________________________________________________________'''


'''Podemos tambem criar um atributo dentro do construtor para
que o atributo seja iniciado automaticamente na instanciação
o atributo declarado dentro do construtor deve ser precedido
por self. '''
# Exemplo 02
class Classe2:
    def __init__(self):
        self.atributo2 = 'atributos em python'


d = Classe2()
print(d.atributo2)


'''_______________________________________________________________'''

'''Uma função pode alterar o valor de um atributo dentro da classe.'''

# Exemplo 03

class Classe3:
    def __init__(self):
        self.atributo = 'Valor padrao'

    # See a funcao for chamada ela vai alterar o valor de atributo.
    def funcao(self):
        self.atributo = 'Valor atualizado'
        return self.atributo

    def metodo(self):
        print(self.atributo)


#instanciando a classe no objeto
e = Classe3()

# mostrando que o valor ainda é o 'valor padrao'
print(e.atributo)

# chama a funcao que altera o valor do atributo
retorno = e.funcao()

# aqui vc ja pode ver que o atributo foi alterado.
print(e.atributo)





