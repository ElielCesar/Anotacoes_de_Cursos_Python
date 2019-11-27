'''Trabalhando com instancias em POO'''

# exemplo 01
'''instanciando uma classe'''
class Classe:
    def __init__(self):
        print('classe instanciada')
        
'''ao chamar com os () a classe eh instanciada e o construtor executado'''
Classe() 

'''--------------------------------------------------------------------'''

# exemplo 02
class Classe2:
    def __init__(self):
        print('classe instanciada')

    def metodo(self):
        print('metodo executado')
        
'''instanciando uma classe e executando um metodo'''
Classe2().metodo()

'''--------------------------------------------------------------------'''

# exemplo 03
'''instanciando uma classe sem executar o construtor automaticamente'''
class Classe3:
    def __init__(self):
        print('classe instanciada')

    def metodo(self):
        print('metodo executado')

'''
Sem colocar o () ao instanciar a classe o construtor nao
sera executado automaticamente, mas se vc precisar usar
um metodo dessa classe vc tem que passar um argumento para
o metodo '''

Classe3.metodo(None)

'''--------------------------------------------------------------------'''

# exemplo 04
class Classe4:
    def __init__(self):
        print('classe instanciada')

    def metodo(self):
        print('metodo executado')


'''com e sem a instanciacao do construtor para resumir'''
Classe4().metodo()
Classe4.metodo(None)
