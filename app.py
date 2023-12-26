import os

restaurantes = [{
      'nome': 'Ohana',
      'categoria': 'Oriental',
      'ativo': True
},{
      'nome': 'Outback',
      'categoria': 'Carne',
      'ativo':True
},{
      'nome': 'Ghebella',
      'categoria': 'Pizza',
      'ativo': True
}, {
      'nome': 'The Best Açai',
      'categoria': 'Açai',
      'ativo': False
}]

def exibir_nome_programa():

      '''
      Exibe o nome do programa de maneira estilizada na tela.
      '''

      print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      \n""")

def exibir_opcoes():

      '''
      Responsável para exibir as opções de escolha para o usuário
      '''

      print("1. Cadastrar restaurante")
      print("2. Listar restaurante")
      print("3. Alternar o status do restaurante")
      print("4. Sair")

def finalizar_app():

      '''
      Responsável por finalizar nosso sistema
      '''

      exibir_subtitulo("Finalizando o app...")

def opcao_invalida():
      
      '''
      Essa função é responsavel por não quebrar nosso programa, ou seja, faz um tratamento de um possível erro 'invalid literal' no momento que o usuário digita uma opção que não corresponde com as opções.

      Outputs:
      - Retorna ao menu principal
      '''

      print("Opção inválida!\n")
      input("Digite qualquer tecla para voltar ao menu principal: ")
      main()

def exibir_subtitulo(text):

      '''
      Responsável por exibir um subtitulo após a opção escolhida pelo usuário

      Inputs:
      - text: str - O texto do subtítulo
      '''

      os.system('clear')
      exibir_nome_programa()
      linha = '*'*(len(text) + 4)
      print(linha)
      print(text)
      print(linha)
      print()

def voltar_menu_principal():

      '''
      Responsável por voltar ao menu principal

      Outputs:
      - Retorna ao menu principal
      '''
      
      input("\nDigite qualquer tecla para voltar ao menu principal: ")
      main()

def cadastrar_novo_restaurante():

      '''
      Essa função é responsável por cadastrar um novo restaurante
      
      Inputs:
      - Nome do restaurante
      - Categoria do restaurante

      Outputs:
      - Adiciona um novo restaurante ao dicionário de restaurantes
      '''

      exibir_subtitulo("Cadastro de novos restaurantes")

      nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
      categoria = input(f'Digite o nome da categoria do {nome_do_restaurante}: ')

      dados_do_restaurante = {
            'nome': nome_do_restaurante,
            'categoria': categoria,
            'ativo': False
      }

      restaurantes.append(dados_do_restaurante)

      print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

      voltar_menu_principal()

def listar_restaurantes(): 

      '''
      Responsável por listar os restaurantes disponíveis no dicionário

      Esta função exibe na tela a lista de restaurantes presentes em um dicionário.
      Para cada restaurante, mostra o nome, categoria e status (ativo ou desativado).
      A lista é exibida com formatação adequada e um contador numérico é utilizado para enumerar os restaurantes.

      Outputs:
      - Exibe a lista de restaurantes na tela
      '''

      exibir_subtitulo("Lista de Restaurantes disponíveis: ")

      contador = 1
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            #ativo = restaurante['ativo']
            ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'

            print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
            print(f'{contador}.{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}\n')
            contador = contador + 1

      voltar_menu_principal()
      
def alternar_status_restaurante():

      '''
      Altera o status de um restaurante entre ativo e desativado.

      Solicita o nome do restaurante ao usuário.
      Verifica se o restaurante existe na lista e, se sim, inverte o status (ativo/desativado).
      Exibe uma mensagem indicando se o restaurante foi ativado ou desativado com sucesso.
      Se o restaurante não for encontrado, exibe uma mensagem informando isso.
      Retorna ao menu principal após a operação.

      Outputs:
      - Exibe mensagem indicando o sucesso da operação
      '''

      exibir_subtitulo("Alterando estado do restaurante: ")

      nome_restaurante = input("Digite o nome do restaurante que deseja alterar o status: ")

      restaurante_encontrado = False

      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                  restaurante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo'] #inverte o status 
                  mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
                  print(mensagem)
      if not restaurante_encontrado:
            print("O restaurante não foi encontrado!")
                  
      voltar_menu_principal()

def escolher_opcao():

      '''
      Obtém e executa a opção escolhida pelo usuário.
      Captura exceções se a entrada não for um número-  except - opcao_invalida().

      Outputs:
      - Executa a opção escolhida pelo usuário

      '''

      try:
            opcao_escolhida = int(input("Escolha uma opção: "))

            if opcao_escolhida == 1:
                  cadastrar_novo_restaurante()
            elif opcao_escolhida == 2:
                  listar_restaurantes()
            elif opcao_escolhida == 3:
                  alternar_status_restaurante()
            elif opcao_escolhida == 4:
                  finalizar_app()
            else:
                  opcao_invalida()
      except:
            opcao_invalida()

def main():
      '''
      Função principal que controla o fluxo do programa.
      Inicializa e executa as funcionalidades do sistema.
      '''
      os.system("clear")
      exibir_nome_programa()
      exibir_opcoes()
      escolher_opcao()

if __name__ == '__main__':
    main()