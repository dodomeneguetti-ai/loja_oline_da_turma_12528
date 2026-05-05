from produto import produto

class roupa (produto):
    def __init__(self, nome, preco,tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho
        def exibir_detalhes(self):
            print(f"Produto: {self.nome} | Preço: R${self._preco()}")