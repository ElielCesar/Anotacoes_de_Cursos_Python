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
        except Exception as erro:
            print(erro)

d = Divisao2()
d.dividir(10, 2)
d.dividir(10, 'a')
d.dividir(10, 0)

'''______________________________________________________________'''






