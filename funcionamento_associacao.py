class Filhos:
    nomes = ['fulano de tal', 'beltrana da silva', 'ciclano de tal']

class Pessoa:
    nome = 'Beltrano de tal'
    idade = 40
    salario = 5200.55
    filhos = Filhos() 
    '''veja que a variavel recebe uma classe, logo ela tambem pode acessar atributos da Classe filhos '''

# Instanciando a classe e os objetos.
p = Pessoa()
nome = p.nome
idade = p.idade
salario = p.salario
filhos = p.filhos.nomes

# imprimindo os valores das variaveis.
print('informacoes pessoais')
print(f'Nome: {nome}')
print(f'idade: {idade}')
print(f'salario: {salario}')
print('filhos')

for f in filhos:
    print(f)
