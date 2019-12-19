class Conta:
    # construtor e atributos privados
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
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
        print(f'Titular: {self.__titular}')
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

    # Usando a nomeclatura get e set
    ''' 
    get e set nao fazem nada de especial, sao apenas convencoes de nomes de metodos em python, basicamente sao usados para que
    o desenvolvedor nao saia usando nomes de metodos aleatorios. a ideia eh: se for retornar um valor use GET se for modificar 
    um valor use SET no nome do metodo.
    '''
    '''
    Outro recurso interressante sao os decorators use @property quando quiser chamar um metodo como
    se fosse chamar um atributo privado tipo um get e @atributo.setter para setar um valor ao atributo privado
    '''
    # vou usar funcoes ao inves de metodos aqui apenas por conveniencia.
    
    #Ambas as versoes abaixo fazem a mesma coisa, apenas escrito de forma diferente.
    
    #def get_titular(self):
    #   return self.__titular
    
    @property
    def titular(self):
        return self.__titular
'''-------------------------------------------------------------------------'''

    #def get_saldo(self):
    #   return self.__saldo

    @property
    def saldo(self):
        return self.__saldo
'''-------------------------------------------------------------------------'''
    
    @property  # estou chamando um metodo com o mesmo nome do atributo.
    def limite(self):
        return self.__limite
    
'''-------------------------------------------------------------------------'''

    #def set_limite(self, novo_limite):
    #    self.__limite = novo_limite

    @limite.setter  # estou chamando um metodo com o mesmo nome do atributo.
    def limite(self, novo_limite):
        self.__limite = novo_limite
'''-------------------------------------------------------------------------'''

# Instanciando objetos
c1 = Conta(1, 'Eliel Cesar', 3000, 1000)
c2 = Conta(2, 'Renilce', 5000, 1000)
c3 = Conta(3, 'Aline', 1500, 1000)

# Chamando os metodos
# c3.depositar()
# c3.sacar()

# Listando extratos
# c1.extrato()
# c2.extrato()
# c3.extrato()

# Transferindo valores
#c1.transferir(c3, 1400)

# testando os getters e setters
# print(c1.get_titular())
# print(c1.get_saldo())
# print(c1.get_limite())
# c1.set_limite(5000)
# print(c1.get_limite())

# testando agora com os decorators acima, para retorno de funcao precisa
# usar o print, se fosse um metodo nao precisaria.
print(c1.titular) # executando o @property
print(c1.limite)  # executando o @property
c1.limite = 2500  # executando o @limite.setter
print(c1.limite)  # executando o @property

