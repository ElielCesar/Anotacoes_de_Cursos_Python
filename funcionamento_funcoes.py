class Classe:
    def funcao(self):
        return 'retorno' # retorno da funcao

c = Classe()
ret = c.funcao()
print(ret)

'''_______________________________________________________'''

# Exemplo 02
class Calculadora:
    def somar(self, n1, n2):
        valor = n1 + n2
        return valor # retorna a soma


    def subtracao(self, n1, n2):
        valor = n1 - n2
        return valor # retorna a subtracao

    def dividir(self, n1, n2):
        valor = n1 / n2
        return valor # retorna a divisao

    def multiplicar(self, n1, n2):
        valor = n1 * n2
        return valor # retorna a multiplicacao

# instanciando a classe e chamando as funcoes.
d = Calculadora()

print(d.somar(2, 2))
print(d.subtracao(5, 2))
print(d.multiplicar(3, 3))
print(d.dividir(9, 3))

'''_______________________________________________________'''
