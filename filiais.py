import os

filiais = []

def exibir_nome_do_programa():

    print("""

███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░░█████╗░██╗░█████╗░
██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗██║██╔══██╗
█████╗░░███████║██████╔╝██╔████╔██║███████║██║░░╚═╝██║███████║
██╔══╝░░██╔══██║██╔══██╗██║╚██╔╝██║██╔══██║██║░░██╗██║██╔══██║
██║░░░░░██║░░██║██║░░██║██║░╚═╝░██║██║░░██║╚█████╔╝██║██║░░██║
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝╚═╝░░╚═╝\n""")

def exibir_opcoes():
    '''Esta função exibe as opções disponíveis no menu principal'''

    print('1. Cadastrar Filial')
    print('2. Listar Filial')
    print('3. Alternar Status da Filial')
    print('4. Sair\n')

def finalizar_app():
    '''Esta função exibe a mensagem de finalização do aplicativo'''

    exibir_subtitulo('Finalizar App')

def voltar_ao_menu_principal():
    '''Esta função solicita uma tecla para voltar ao menu principal
     
    Outputs:

    - Retorna ao menu principal
     
    '''

    input('\nDigite uma tecla para voltar ao menu principal.')
    main()  


def opcao_invalida():
    '''Esta função exibe mensagem de opção inválida e retorna ao menu principal
     
    Outputs:

    - Retrona ao menu principal
     
    '''

    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Esta função exibe um subtítulo estilizado na tela
     
    Inputs:
     
    - Texto: str o texto do subtitulo
     
    '''

    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_nova_filial():
    '''Esta função é responsável por cadastrar uma nova Filial
    
    Inputs:

    - Nome da Filial
    - Número da Filial
    - Categoria

    Outputs:

    - Adiciona uma nova filial a lista de filiais
    
    
    '''
    exibir_subtitulo('Cadastro de Novas Filiais')
   
    numero_da_filial = input('Digite o Número da Filial que deseja cadastrar: ')
    print()
    nome_da_filial = input('Digite o Nome da Filial que deseja Cadastrar: ')
    print()
    categoria = input(f'Digite a Categoria da Filial {nome_da_filial}: ')
    
    dados_da_filial = {'nome':nome_da_filial, 'numero_da_filial':numero_da_filial, 'categoria':categoria, 'ativa':False}
    filiais.append(dados_da_filial)
    print(f'A Filial {nome_da_filial} foi cadastrada com sucesso!')
    print()
    input('Digite uma tecla para voltar ao menu principal.')
    main()

def listar_filial():
    '''Esta função lista as filiais presentes na lista
     
    Outputs: 

    - Exibe a lista de filiais na tela
     
     
    '''
    exibir_subtitulo('Listando Filiais')
    print(f'{'Número da Filial'.ljust(23)} | {'Nome da Filial'.ljust(20)} | {'Categoria'.ljust(20)} | Status')

    for filial in filiais:
        
        numero_da_filial = filial['numero_da_filial']
        nome_da_filial = filial['nome']
        categoria = filial['categoria']
        ativa = 'Ativada' if filial['ativa'] else 'Desativada'
        print(f'{numero_da_filial.ljust(23)} | {nome_da_filial.ljust(20)} | {categoria.ljust(20)} | {ativa}') 

    voltar_ao_menu_principal()

def alternar_status_filial():
    '''Esta função altera o status ativa/desativada da filial
     
    Outputs:

    - Exibe a mensagem indicando o sucesso da operação
     
     
    '''
    exibir_subtitulo('Alternando Status da Filial') 
    numero_da_filial = input('Digite o Número da Filial que deseja alterar o Status: ')
    filial_encontrada = False

    for filial in filiais:
        if numero_da_filial == filial['numero_da_filial']:
            filial_encontrada = True
            filial['ativa'] = not filial['ativa']
            mensagem = f'A Filial {numero_da_filial} foi ativada com Sucesso!' if filial['ativa'] else f'A Filial {numero_da_filial} foi desativado com Sucesso!'
            print(mensagem)
    if not filial_encontrada:
       print('Esta Filial não foi encontrada!')
    
    voltar_ao_menu_principal()   

def escolher_opcao():
    '''Esta função solicita e executa a opção escolhida pelo usuário
     
    Outputs:

    - Executa a opção escolhida pelo usuário
     
    '''
    try:

        opcao_escolhida = int(input('Escolha uma Opção: '))
            
        if opcao_escolhida == 1:
            cadastrar_nova_filial()
        elif opcao_escolhida == 2:
            listar_filial()
        elif opcao_escolhida == 3:
            alternar_status_filial()
        elif opcao_escolhida == 4:
            finalizar_app()    
        else:
            opcao_invalida()
    except:
        opcao_invalida()        

def main():
    '''Função principal que inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

