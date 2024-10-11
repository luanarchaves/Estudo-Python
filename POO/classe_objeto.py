class Vendedor:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(self.nome, "Bateu a meta")
        else:
            print(self.nome, "Não bateu a meta")

vendedores = [
    {"nome": "Luana", "vendas": 500, "meta": 450},
    {"nome": "Luiz", "vendas": 600, "meta": 500}
]

vendedores_lista = []

for i in range(len(vendedores)):
    vendedor = Vendedor(vendedores[i]["nome"])
    vendedor.vendeu(vendedores[i]["vendas"])
    vendedor.bateu_meta(vendedores[i]["meta"])
