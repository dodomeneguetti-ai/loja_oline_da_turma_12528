class carrinhodecompra:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self,produto):
        self.itens.append(produto)
        print (f"{produto.nome}foi adicionado ao carrinho")

    def exibir_resumo(self):
        print("\n --- resumo do carrrinho---")
        total = 0 

        for item in self.itens :
            item.exiri_detales()
            total += item.get_preco()
        print(f"total a pagar : rs {total}")
        print("-"*45)
