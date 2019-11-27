'''
Classe = Estrutura maior
Instancia = permite acessar recursos da classe
Obejeto = A variavel que recebera uma classe.
atributo = variaveis internas da classe
metodo = funcoes que existem dentro de uma classe
'''

# criando uma classe 
class Classe:
    def metodo(self):
        print('teste')

# instanciando a classe
variavel = Classe()
# chamando um metodo da classe
variavel.metodo()

'''------------------------------------------------------------'''

# criando classes - 02
class Classe1:
    def metodo1(self):
        print('Metodo da classe 1')

class Classe2:
    def metodo2(self):
        print('metodo da classe 2')

# chamando a classe e seus metodos diretamente sem 
# instanciar um objeto para isso.
Classe1().metodo1()
Classe2().metodo2()

'''------------------------------------------------------------'''

# criando classes 03
class Mensagens:
    def saudacao(self):
        print('Seja bem vindo!')

    def despedida(self):
        print('ate logo!')


Mensagens().saudacao()
Mensagens().despedida()

'''------------------------------------------------------------'''

# varias formas de declarar uma classe.

# forma mais utilizada
class Classe1:
    def metodo(self):
        print('classe 1')

# segunda forma mais utilizada
class Classe2():
    def metodo(self):
        print('classe 2')

# menos utilizada 
class Classe3(object):
    def metodo(self):
        print('classe 3')
        
'''------------------------------------------------------------'''

'''
Quando o script .py roda, o interpretador carrega na memoria(ponteiro)
todas as classes existentes no arquivo, depois disso ele 
somente vai usar a classe se ela for referenciada em algum lugar
no codigo.

Resumindo: primeiro o interpretador python lê todo o codigo e 
depois volta do inicio executando linha por linha.
'''

# metodo construtor - 01
class Classe:
    ''' 
    o metodo construtor sera executado automaticamente toda
    vez que instanciarmos a classe '''

    def __init__(self):
        print('classe carregada em memoria...')


Classe()

'''------------------------------------------------------------'''

# metodo construtor - 02
class Classe2:
    ''' 
    o metodo construtor sera executado automaticamente toda
    vez que instanciarmos a classe '''

    def __init__(self):
        print('classe carregada em memoria...')

    def metodo(self):
        print('metodo acionado...')

'''Vai chamar o construtor automaticamente e tambem o metodo'''
Classe2().metodo()

'''------------------------------------------------------------'''

# metodo construtor - 03
class Classe3:
    def __init__(self, msg):
        print(msg)

Classe3('Eu passei essa mensagem')

'''
Veja que eu passei a mensagem e ela foi chamada automaticamente
sem que eu precisa-se invocar nenhum metodo, pois o construtor 
se autoexecuta toda vez que a classe eh instanciada.
Nesse caso o parametro msg obrigatoriamente tem que ser passado 
ao executarmos a classe.
'''

# da pra usar o construtor e o metodo juntos
class Classe:
    
    def __init__(self, msg):
        print(msg)

    def metodo(self):
        print('metodo acionado...')

Classe('Aprendendo POO em Python').metodo()

'''------------------------------------------------------------'''

'''
Metodo destrutor - sera acionado toda vez que a classe
for descarregada da memoria.

Boas praticas de programacao:
- O construtor deve ser definido no inicio da classe
- O destrutor deve ser definido no final da classe.

para descarregar uma classe use o del.
'''
# exemplo 01
class Classe:
    def __del__(self):
        print('classe descarregada da memoria')


c = Classe()
# descarrega a classe da memoria.
del c

# exemplo 02
class Classe2:
    def metodo(self):
        print('metodo executado')

    def __del__(self):
        print('classe descarregada da memoria')

d = Classe2()
d.metodo()
# descarrega a classe da memoria.
del d

# exemplo 03
class Classe3:
    def __init__(self):
        print('classe carregada na memoria')

    def metodo(self):
        print('O metodo foi executado com sucesso')

    def __del__(self):
        print('classe descarregada da memoria')

e = Classe3()
e.metodo()
# descarrega a classe da memoria.
del e



