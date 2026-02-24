import os

catalogo  = []

#limpa o cmd anterior
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#funçao usada para informa e dps utilizada para ser armazenado
def exibir_informacao(**informacao):
       for chave, valor in informacao.items():
            print(f"{chave}: {valor}")

def subMenu():
    print("\n=== Menu de Cadastro ===\n")
    print("-Escolha uma opção-\n")
    print("1 - Continuar")
    print("2 - Voltar pro Menu\n")

def subMenuBusca():
     print("\n=== Menu de Busca  ===\n")
     print("-Escolha uma opção-\n")
     print("1 - Continuar busca")
     print("2 - Remover Jogo")
     print("3 - Atualizar informações")
     print("4 - Voltar pro Menu\n")

def subMenuAtualizar():
     print("\n=== Sub Menu  ===\n")
     print("-Escolha uma opção-\n")
     print("1 - Nome")
     print("2 - Plataforma")
     print("3 - ano_de_lancamento")
     print("4 - preco_pago")
     print("5 - status")
     print("6 - Voltar pro menu da Busca\n")

def sair():
     # para sair 
     try:
       print("\n=== Voltar Menu ===")
       menu_cadastro = int(input("\nDigite 1 para sair: "))
     except ValueError:
       print("\nEntrada invalida. Por favor, digite um valor numero valido")
       return main()

     match menu_cadastro:
         case 1: main()

#cadastrar os jogos 
def cadastro():
    limpar_tela()
    print("\n===== Novo cadastro =====")
    nome = str(input("\nDigite o nome do Jogo: ")).lower().strip()

     #faz a verificação se algum jogo com mesmo nome
    for jogo in catalogo:
        if jogo['nome'] == nome:
            print("\nErro: esse jogo ja existe na Coleção")
            return main()

    plataforma = str(input("Digite o nome da Plataforma disponivel: ")).lower().strip()

    #tratamento de erro caso digite errado o tipo string
    try:
        ano_lancamento = int(input("Ano de lançamento: "))
    except ValueError:
        print("\nEntrada invalida. Por favor, digite um valor numero valido")
        return main()
    
    try:
      preco_pago = float(input("Valor pago quando comprou: "))
    except ValueError:
          print("\nEntrada invalida. Por favor, digite um valor numero valido")
          main()

    #fim do tratamento de erro acima
    status = str(input("status do jogo exemplo( zerado, andamento, Interrompido ou nao_iniciado ): ")).lower().strip()

    #usado para armazenar os valores por jogo
    novo_catalago = {
         "nome":  nome,
         "Plataforma": plataforma,
         "ano_de_lancamento": ano_lancamento, 
         "preco_pago": preco_pago,
         "status": status
    }
    
    #armazenado numa array
    catalogo.append(novo_catalago)
    #apenas mostrar
    print("=== Informações adicionadas ===")
    exibir_informacao(**novo_catalago)


   # para sair ou continuar
    subMenu()
    
    #tramento erro 
    try:
      menu_cadastro = int(input("\n: "))
    except ValueError:
      print("\nEntrada invalida. Por favor, digite um valor numero valido")
      return main()

    match menu_cadastro:
         case 1: cadastro()
         case 2: main()


def lista():
     limpar_tela()

     # verificar se um valor está vazio
     if not catalogo:
          print("\n*****nenhum jogo encontrado ainda.*****\n")
     
     #ordem a  ate z
     catalago_ordem = sorted(catalogo, key=lambda jogo:jogo['nome']) 
     # o enumerate adiciona um contador a um objeto iterável, como uma lista ou string, e o retorna como um objeto enumerado.
     for i, jogos in enumerate(catalago_ordem):
          print(f"\nJogo #{i+1}:")

          #usado para mostrar todos os jogos
          exibir_informacao(**jogos)

     sair()

#busca o item pelo nome dps passa as informaçoes
def busca():
     limpar_tela()

     print("====== Busca =====")

     try:
       nome_jogo = str(input("\nDigite nome do jogo que deseja encontrar: ")).lower().strip()
     except ValueError:
         print("ERRO: Valor Invalido tente novamente.")
         return busca()
         

    #Usa next() com um gerador para encontrar o primeiro dicionário com o nome correspondente.
    # O valor None é retornado se nenhum jogo for encontrado.
     busca_jogo = next((jogo for jogo in catalogo if jogo['nome'] == nome_jogo), None)
     

     if busca_jogo:
          exibir_informacao(**busca_jogo)
     else: 
        print("\n*****Jogo não encontrado.*****")
        main()

     #remove item da busca
     def remover():
         catalogo.remove(busca_jogo)
         print("\njogo removido da coleção\n")
     
     #atualizar cada item que deseja alterara essa funçao serve para substuir o anterior
     #utilizei strip() para remover qualquer espaço que tiver no começo e fim
     def atualizar():
       
       subMenuAtualizar()
        
       try:  
         editar = int(input("\n: "))
       except ValueError:
           print("\nEntrada invalida. Por favor, digite um valor numero valido")
           return main()
  
       
       match editar:
            case 1:
                 novo_nome = str(input("Digite o Novo nome: ")).strip()
                 busca_jogo['nome'] = novo_nome #substituir valor
                 exibir_informacao(**busca_jogo) #apenas para ver a alteração
                 Tela_de_busca() 
            case 2:
                 novo_plataforma = str(input("Digite as novas plataformas: ")).strip()
                 busca_jogo['Plataforma'] = novo_plataforma
                 exibir_informacao(**busca_jogo)
                 Tela_de_busca() 
            case 3:
                 try:
                  novo_lançamento = int(input("Digite o ano lançamento correto: "))
                 except ValueError:
                      print("\nEntrada invalida. Por favor, digite um valor numero valido")
                      return Tela_de_busca()
                 busca_jogo['ano_de_lancamento'] = novo_lançamento
                 exibir_informacao(**busca_jogo)
                 Tela_de_busca() 
            case 4: 
                 try:
                   novo_pago = float(input("Digite o pagamento correto: "))
                 except ValueError:
                     print("\nEntrada invalida. Por favor, digite um valor numero valido")
                     return Tela_de_busca()
                 busca_jogo['preco_pago'] = novo_pago
                 exibir_informacao(**busca_jogo)
                 Tela_de_busca() 
            case 5:
                 novo_status = str(input("Digite o novo status: ")).strip()
                 busca_jogo['status'] = novo_status
                 exibir_informacao(**busca_jogo)
                 Tela_de_busca() 
            case 6:
                 Tela_de_busca() 
            case _:
                 print("erro valor invalido")
                 main()
            
     # foi so para retornar para Tela de busca de vez pro main direto
     def Tela_de_busca():
          subMenuBusca()

          try:
            menu_busca = int(input("\n: "))
          except ValueError:
              print("\nEntrada invalida. Por favor, digite um valor numero valido")
              return Tela_de_busca()
     
          match menu_busca:
             case 1:
                busca()
             case 2:
               remover()
               main()
             case 3:
               atualizar()
             case 4:
               main() 

     Tela_de_busca()     
      
#ver estatisticas max, min, quantidade dos itens e media deles. 
def Estatisticas():
     limpar_tela()

     if not catalogo:
          print("\nNenhum jogo cadastrado para calcular as estatísticas.\n")
          main()
          return

     quantidade = len(catalogo)
     preco_max = max(catalogo, key=lambda jogo: jogo['preco_pago'])
     preco_min = min(catalogo, key=lambda jogo: jogo['preco_pago'])

     # Extrai a lista de preços usando um gerador 
     precos = (jogo['preco_pago'] for jogo in catalogo)

     media = sum(precos) / quantidade

     zerado,andamento,Não_iniciado, Interrompido  = 0,0,0,0
     for jogo in catalogo:
         if jogo['status'] == 'zerado' :
             zerado += 1
         elif jogo['status'] == 'andamento':
             andamento += 1
         elif jogo["status"] == 'nao_iniciado':
             Não_iniciado += 1
         else:
             Interrompido += 1
     
     print("\n====== Estatísticas ======\n")
     print(f"O Total de jogos na coleção é: {quantidade}")
     print(f"O valor medio dos jogos são R$ {media:.2f}")
     print(f"O jogo mais caro é **{preco_max['nome']}**, custando R$ {preco_max['preco_pago']:.2f}.")
     print(f"O jogo mais barato é **{preco_min['nome']}**, custando R$ {preco_min['preco_pago']:.2f}.")
     print(f"A Quantidade de Jogos zerados são {zerado}")
     print(f"A Quantidade de Jogos em andamento são {andamento}")
     print(f"A Quantidade de Jogos Não iniciado são {Não_iniciado}")
     print(f"A Quantidade de Jogos Interrompido são {Interrompido}")

     sair()

def main():
    limpar_tela()
    print("\n========== Menu ===========\n")
    print("-Escolha uma opção-\n")
    print("1 - Cadastrar jogo")
    print("2 - Lista de jogos")
    #na busca tbm remove e atualiza o item.
    print("3 - Busca")
    print("4 - Estatisticas")
    print("5 - finalizar\n")


     #caso escreva errado volta pro main()
    try:
     menu = int(input(": "))
    except ValueError:
      print("\nEntrada invalida. Por favor, digite um valor numero valido")
      return main()

    
    match menu:
        case 1:
            cadastro()
        case 2: 
            lista()
        case 3:
             busca()
        case 4:
            Estatisticas()
        case 5:
              print("\nobrigado, saida concluida. \n")
        case _:
              print("\nvalor invalido")
              main()
            
             
main()