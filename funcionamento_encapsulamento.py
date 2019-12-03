''' 
Encapsulamento em Python:

Permissao pode ser publica, protegida e privada.

Permissao Publica:
Permite que o recurso seja acessado de qualquer ponto do codigo.
Os recursos publicos (atributos, metodos, funcoes) sempre vao
iniciar com uma letra do alfabeto.

'''
# Exemplo de atributos, metodos e funcoes publicos.
class Classe:
    atributo_publico = 'atributo publico'

    def metodo_publico(self):
        print('metodo publico')

    def funcao_publica(self):
        return 'funcao publica'


# Instanciando o objeto
obj = Classe()

obj.metodo_publico()
print(obj.atributo_publico)
print(obj.funcao_publica())


