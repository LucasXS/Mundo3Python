from sistemaCadastros.lib.arquivo.arquivoModulo import *
from sistemaCadastros.lib.interface.face import *
from sistemaCadastros.lib.arquivo import *
from time import sleep

arq = 'lpessoascadastradas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:

        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema...Até logo!')
        break
    else:
        print('\033[1;31mErro! Digite uma opção válida!\033[m')
        sleep(2)



