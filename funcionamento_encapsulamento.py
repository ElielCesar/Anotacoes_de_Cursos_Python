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


'''_______________________________________________________________'''


''' 
Recursos protegidos devem ser usados somente por classes 
filhas que vao herdar esses recursos da classe pai.

Os recursos protegidos devem ser usados somente dentro da classe que o 
declarou ou dentro da classe filha.

Para proteger apenas coloque um underline _ no inicio do nome.
'''
# Forma errada de usar os recursos protegidos
class Classe:
    _atributo_protegido = 'atributo protegido'

    def _metodo_protegido(self):
        print('metodo protegido')

    def _funcao_protegida(self):
        return 'funcao protegida'


# Instanciando o objeto
obj = Classe()

# todas as formas abaixo embora possiveis sao incorretas de acordo com o padrao do python
print(obj._atributo_protegido)
print(obj._funcao_protegida())
obj._metodo_protegido()


'''_______________________________________________________________'''

# Forma correta de usar os recursos protegidos
class Pai:
    _atributo_protegido = 'atributo protegido'

    def _metodo_protegido(self):
        print('metodo protegido')

    def _funcao_protegida(self):
        return 'funcao protegida'


class Filha(Pai):
    atributo_publico = Pai()._atributo_protegido

    def metodo_publico(self):
        self._metodo_protegido()

    def funcao_publica(self):
        return self._funcao_protegida()


# Instanciando o objeto
obj = Filha()

print(obj.atributo_publico)
print(obj.funcao_publica())
obj.metodo_publico()

