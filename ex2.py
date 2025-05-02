class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def atualizar_quantidade(self):
        valor = int(input("Digite a quantidade que deseja adicionar: "))
        return valor

    def valor_total(self, quantidade):
        return self.preco * quantidade

def exibir(produto, valor_total):
    quantidade = produto.atualizar_quantidade()
    valor_total += produto.valor_total(quantidade)
    print(f"\n|Carrinho|\n{produto.nome}: {quantidade} unidade(s)")
    print(f"Valor da compra: R${valor_total}")
    return valor_total

def menu():
    print("\n|Escolha um produto|")
    print("1. Suco\n2. Bolacha\n3. Fruta\n4. Doce\n5. Sair\n")

def produtos():
    suco = Produto("Suco", 5)
    bolacha = Produto("Bolacha", 3.5)
    fruta = Produto("Fruta", 7)
    doce = Produto("Doce", 6.3)

    valor_total = 0

    while True:
        menu()
        escolha = input("\nDigite o número do produto que deseja escolher: ")

        if escolha == '1':
            valor_total = exibir(suco, valor_total)
        elif escolha == '2':
            valor_total = exibir(bolacha, valor_total)
        elif escolha == '3':
            valor_total = exibir(fruta, valor_total)
        elif escolha == '4':
            valor_total = exibir(doce, valor_total)
        elif escolha == '5':
            print(f"Valor total: R${valor_total}\nFinalizando programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

produtos()