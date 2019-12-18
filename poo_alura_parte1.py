class Conta:
    # construtor e atributos
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self._titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # metodo
    def depositar(self, valor=0):
        self.__saldo += valor
        print(f'Seu Novo Saldo eh de: {self.__saldo}\n')

    # metodo
    def sacar(self, valor=0):
        if (self.__saldo - valor) < 0:
            print(f'Saldo Insuficiente para realizar esse saque!\n')
        else:
            self.__saldo -= valor
            print(f'Seu Novo Saldo eh de: {self.__saldo}\n')

    # metodo
    def extrato(self):
        print('Dados Bancarios:')
        print(f'Conta: {self.__numero}')
        print(f'Titular: {self._titular}')
        print(f'Saldo: {self.__saldo}')
        print(f'Limite: {self.__limite}\n')

    # metodo
    def transferir(self, destino, valor_transf=0):
        # veja que o self vale para o objeto instanciado atual
        self.sacar(valor_transf) 
        destino.depositar(valor_transf)
        # veja que o self vale para o objeto instanciado atual
        self.extrato()
        destino.extrato()


# Instanciando objetos
c1 = Conta(1, 'Eliel Cesar', 3000, 1000)
c2 = Conta(2, 'Renilce', 5000, 1000)
c3 = Conta(3, 'Aline', 1500, 1000)

# Chamando os metodos
#c3.depositar()
#c3.sacar()

# Listando extratos
#c1.extrato()
#c2.extrato()
#c3.extrato()

# Transferindo valores
c1.transferir(c3, 1400)


