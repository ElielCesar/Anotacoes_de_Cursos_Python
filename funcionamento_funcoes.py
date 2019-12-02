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


# é possivel fazer o mesmo exemplo acima com menos linhas de codigo
# ficando assim o codigo final
# Exemplo 02
class Calculadora:
    def somar(self, n1, n2): return n1 + n2
    def subtracao(self, n1, n2): return n1 - n2
    def dividir(self, n1, n2): return n1 / n2
    def multiplicar(self, n1, n2): return n1 * n2
        
d = Calculadora()
print(d.somar(2, 2))
print(d.subtracao(5, 2))
print(d.multiplicar(3, 3))
print(d.dividir(9, 3))

'''_______________________________________________________'''

# Chamando funcoes dentro de funcoes.
class Classe:
    def funcao1(self):
        return 'retorno da funcao 1'

    def funcao2(self):
        return self.funcao1()

c = Classe()
print(c.funcao2())

# outro exemplo agora passando agurmentos para os parametros
class Classe2:
    def funcao1(self, msg):
        return 'mensagem recebida: ' + msg

    def funcao2(self, msg):
        return self.funcao1(msg)

c = Classe2()
print(c.funcao2('estou aprendendo python em 2019'))



