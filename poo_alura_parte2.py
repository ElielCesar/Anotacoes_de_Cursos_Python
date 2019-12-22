class Programa:             # Classe mae.
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):     # metodo
        self._likes += 1

    @property               # gettter
    def nome(self):
        return self._nome

    @nome.setter            # setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property               # funcao
    def likes(self):
        return self._likes


class Filme(Programa):                       # heranca
    def __init__(self, nome, ano, duracao):  # super traz as variaveis nome e ano da classe pai
        super().__init__(nome, ano)          # usando super nao precisa do self
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


# Instanciando objetos
vingadores = Filme('vingadores guerra infinita', 2017, 120)
atlanta = Serie('Atlanta', 2017, 2)

# Dando Likes
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()

# Imprimindo
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} minutos - Likes: {vingadores.likes}')
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Duracao: {atlanta.temporadas} temporadas - Likes: {atlanta.likes}')
