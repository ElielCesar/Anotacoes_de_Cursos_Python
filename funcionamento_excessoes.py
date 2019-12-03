class Divisao:
    def dividir(self, n1=0, n2=0):
        try:
            print(f'{n1} / {n2} = {n1/n2}')
        except:
            print('Ocorreu um erro.')

d = Divisao()
d.dividir(10, 2)
d.dividir(10, 'a')
d.dividir(10, 0)

'''______________________________________________________________'''

# capturando a mensagem de erro original com exception
class Divisao2:
    def dividir(self, n1=0, n2=0):
        try:
            print(f'{n1} / {n2} = {n1/n2}')
        except Exception as erro: # esse trecho pega o erro original
            print(erro)

d = Divisao2()
d.dividir(10, 2)
d.dividir(10, 'a')
d.dividir(10, 0)

'''______________________________________________________________'''

# eh possivel criar algumas excessoes personalizadas para um caso
# especifico usando o raise
class Divisao3:
    def dividir(self, n1=0, n2=0):
        try:
            if n2 == 'a': # se a condicao for verdadeira gera uma exception personalizada.
                raise Exception('O segundo argumento nao eh inteiro')
            print(f'{n1} / {n2} = {n1/n2}')

        except Exception as erro:
            print(erro)


d = Divisao3()
d.dividir(10, 2)
d.dividir(10, 'a')
d.dividir(10, 0)

'''______________________________________________________________'''

# para ignorar o erro do except simplimente adicione um pass ao final.

except:
    pass

