class CRUD:
    def __init__(self):
        import os
        self.os = os # torna o modulo os disponivel para toda classe
        os.system('cls')
        print('Cadastro')
        
    # Funcao para ler os dados cadastrados
    def ler(self):
        # cria a base_dados se nao existir
        if not self.os.path.exists('base_dados.txt'):
            escrita = open('base_dados.txt', 'w')
            escrita.write('')
            escrita.close()
        
        # le a base de dados
        leitura = open('base_dados.txt', 'r')
        retorno = ''

        # itera nas linhas da base_dados
        for linha in leitura:
            retorno += linha.strip() + '\n' # remove espaços indesejados

        # encerra a leitura
        leitura.close()

        # traz o retorno ou nao.
        if len(retorno) > 0:
            return retorno
        else:
            return 'Nenhum registro cadastrado'


    # Funcao para gerar o ID
    def codigo_id(self):
        self.ler()
        leitura = open('base_dados.txt', 'r')
        ultima_linha = ''

        for linha in leitura:
            ultima_linha = linha.strip()

        if len(ultima_linha) <= 0:
            ultima_linha = 'ID: 0000000'

        # nao entendi essa porra abaixo mas isso sera o gerador de id
        id = int(ultima_linha[ultima_linha.find('ID: ')+4:11])+1
        id = str(id).rjust(7, '0')

        # encerra a leitura da base_dados
        leitura.close()
        return id    

