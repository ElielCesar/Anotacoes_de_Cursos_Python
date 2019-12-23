class Programa:                             # Classe mae.
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):                     # metodo
        self._likes += 1

    @property                               # gettter
    def nome(self):
        return self._nome

    @nome.setter                            # setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property                               # funcao
    def likes(self):
        return self._likes

    def __str__(self):                      # representacao textual do objeto
        return f'Nome: {self._nome} Ano: {self.ano} Likes: {self._likes}'


class Filme(Programa):                       # heranca
    def __init__(self, nome, ano, duracao):  # super traz as variaveis nome e ano da classe pai
        super().__init__(nome, ano)          # usando super nao precisa do self
        self.duracao = duracao               # conceito de extensao da classe pai eh usado

    def __str__(self):
        return f'Nome: {self._nome} Ano: {self.ano} Duracao: {self.duracao} Minutos Likes: {self._likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} Ano: {self.ano} Temporadas: {self.temporadas} Likes: {self._likes}'


#class Playlist:                       
#    def __init__(self, nome, programas):
#        self.nome = nome
#        self.programas = programas

    #def tamanho(self):
    #    return len(self.programas)

class Playlist(list):                       # herda da classe list (builtin)
    def __init__(self, nome, programas):    # construtor da classe Playlist
        self.nome = nome
        super().__init__(programas)         # passa a lista de programas para o construtor da classe list


# Instanciando objetos
vingadores = Filme('vingadores guerra infinita', 2017, 120)
atlanta = Serie('Atlanta', 2017, 2)
cap_america_f_a = Filme('Capitao america o primeiro vingador', 2016, 120)
homem_de_ferro = Filme('Homem de ferro', 2015, 145)
walking_dead = Serie('The walking dead', 2008, 10)

# Dando Likes
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
walking_dead.dar_like()
walking_dead.dar_like()
walking_dead.dar_like()
walking_dead.dar_like()


# criando um catalogo de filmes
filmes_e_series = [vingadores, atlanta,
                   cap_america_f_a, homem_de_ferro, walking_dead]

# criando uma playlist
playlist_fim_de_semana = Playlist('Fim de Semana', filmes_e_series)

# percorrendo a playlist_fim_de_semana
#for programa in playlist_fim_de_semana.programas:
#    print(programa)

# usando a heranca que veio de list
print(f'O tamanho da Playlist eh: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

