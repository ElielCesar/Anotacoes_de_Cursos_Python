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

 '''_____________________________________________'''

# Exemplo 02 - mesma coisa do exemplo 01
class Linguagens:
    nomes = ['C', 'C++', 'Java', 'Python', 'Java Script', 'Ruby']

class Profissional:
    nome = 'Eliel Cesar'
    idade = 27
    salario = 3500.00
    sexo = 'M'
    habilidades = Linguagens()

p = Profissional()
nome = p.nome
idade = p.idade
salario = p.salario
sexo = p.sexo
habilidades = p.habilidades.nomes

print('Informacoes profissionais:')
print(f'Nome: {nome}')
print(f'idade: {idade}')
print(f'salario: {salario}')
print(f'sexo: {sexo}')
print(f'Habilidades:')
for h in habilidades:
    print(h)
