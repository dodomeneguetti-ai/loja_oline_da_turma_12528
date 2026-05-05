from roupa import roupa
from eletronico import eletronico
from carrinho import carrinhodecompras

def exibir_menu():
    print("\n" + "="*45)
    print("MENU DA LOJA ONLINE".center(45))
    print("="*45)
    print("[1] Adicionar Roupa")
    print("[2] Adicionar Eletrônico")
    print("[3] Ver Resumo do Carrinho")
    print("[0] Sair do Sistema")
    print("="*45)

def main():
    
    carrinho = carrinhodecompras()
    
    print("\nBem-vindo ao sistema de gestão de loja")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Cadastrar Roupa ---")
            nome = input("Nome da roupa: ")
            try:
                preco = float(input("Preço: R$ "))
                tamanho = input("Tamanho (P/M/G): ")
                
                nova_roupa = roupa(nome, preco, tamanho)
                carrinho.adicionar_produto(nova_roupa)
                print("Roupa adicionada com sucesso!")
            except ValueError:
                print("Erro: por favor, digite um valor numérico válido para o preço.")

        elif opcao == "2":
            print("\n--- Cadastrar Eletrônico ---")
            nome = input("Nome do eletrônico: ")
            try:
               
                preco = float(input("Preço: R$ "))
                voltagem = input("Voltagem (ex. 110V/220V): ")
                novo_eletronico = eletronico(nome, preco, voltagem)
                carrinho.adicionar_produto(novo_eletronico)
                print("Eletrônico adicionado com sucesso!")
            except ValueError:
                print("Erro: por favor, digite um valor numérico válido para o preço.")

        elif opcao == "3":
          
            carrinho.exibir_resumo()

        elif opcao == "0":
            print("Encerrando sistema... Até logo!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()