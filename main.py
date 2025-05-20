class Jogo:
    def __init__(self, titulo, genero, classificacao, preco):
        self.titulo = titulo
        self.genero = genero
        self.classificacao = classificacao
        self.preco = preco

    def exibir_detalhes(self):
        detalhes = {
            "titulo": self.titulo,
            "genero": self.genero,
            "classificacao": self.classificacao,
            "preco": self.preco
        }
        return detalhes.values()


class Jogador:
    def __init__(self, nick, id, saldo):
        self.nick = nick
        self.id = id
        self.jogos = []
        self.saldo = saldo

    def exibir_perfil(self):
        detalhes_perfil = {
            "nick": self.nick,
            "id": self.id,
            "saldo": self.saldo
        }
        return detalhes_perfil.values()

    def adicionar_jogo(self, jogo):
        self.jogos.append(jogo)
        return self.jogos

    def adicionar_saldo(self):
        novo_valor = float(input("Qual o valor a ser depositado: "))
        self.saldo += novo_valor
        print(f"Novo saldo: {self.saldo:.2f}")
        return self.saldo

    def debitar_saldo(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Novo saldo: {self.saldo:.2f}")
            return True
        else:
            print("Saldo insuficiente!")
            return False


class Plataforma:
    def __init__(self, todos_jogos, lista_jogadores):
        self.todos_jogos = todos_jogos
        self.lista_jogadores = lista_jogadores

    def adicionar_jogo(self, jogo):
        self.todos_jogos.append(jogo)
        print(f"Jogo '{jogo.titulo}' adicionado à plataforma.")
        return self.todos_jogos

    def adicionar_jogador(self, jogador):
        self.lista_jogadores.append(jogador)
        print(f"Jogador '{jogador.nick}' adicionado à plataforma.")
        return self.lista_jogadores

    def buscar_jogo_titulo(self):
        busca_nome = input("Qual o nome do jogo: ")
        for jogo in self.todos_jogos:
            if busca_nome.lower() == jogo.titulo.lower():
                return jogo
        return None
    
    def buscar_jogador_id(self):
        busca_id = int(input("Qual o ID do usuário: "))
        for jogador in self.lista_jogadores:
            if busca_id == jogador.id:
                return jogador
        return None
    
    def listar_jogos_catalogo(self):
        print("\nCatálogo de Jogos:")
        for jogo in self.todos_jogos:
            detalhes = jogo.exibir_detalhes()
            print(f"Título: {jogo.titulo}, Gênero: {jogo.genero}, Classificação: {jogo.classificacao}, Preço: R$ {jogo.preco:.2f}")
    
    def realizar_compra(self):
        jogador_comprador = self.buscar_jogador_id()
        if jogador_comprador is None:
            print("Usuário não cadastrado.")
            return

        jogo_desejado = self.buscar_jogo_titulo()
        if jogo_desejado is None:
            print("Jogo não encontrado.")
            return

        if jogo_desejado in jogador_comprador.jogos:
            print("O usuário já possui esse jogo.")
            return

        if jogador_comprador.debitar_saldo(jogo_desejado.preco):
            jogador_comprador.adicionar_jogo(jogo_desejado)
            print("Compra realizada com sucesso!")
        else:
            print("Saldo insuficiente.")

def menu(plataforma):
    while True:
        print("\nMenu:")
        print("1. Listar jogos do catálogo")
        print("2. Buscar jogo pelo título")
        print("3. Buscar jogador pelo ID")
        print("4. Adicionar saldo a jogador")
        print("5. Realizar compra de jogo")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            plataforma.listar_jogos_catalogo()
        elif escolha == "2":
            jogo = plataforma.buscar_jogo_titulo()
            if jogo:
                detalhes = jogo.exibir_detalhes()
                print(f"Detalhes do jogo: Título: {jogo.titulo}, Gênero: {jogo.genero}, Classificação: {jogo.classificacao}, Preço: R$ {jogo.preco:.2f}")
            else:
                print("Jogo não encontrado.")
        elif escolha == "3":
            jogador = plataforma.buscar_jogador_id()
            if jogador:
                perfil = jogador.exibir_perfil()
                print(f"Perfil do jogador: Nick: {jogador.nick}, ID: {jogador.id}, Saldo: R$ {jogador.saldo:.2f}")
                if jogador.jogos:
                    print("Jogos do jogador:")
                    for j in jogador.jogos:
                        print(f"- {j.titulo}")
                else:
                    print("O jogador não possui jogos.")
            else:
                print("Jogador não encontrado.")
        elif escolha == "4":
            jogador = plataforma.buscar_jogador_id()
            if jogador:
                jogador.adicionar_saldo()
            else:
                print("Jogador não encontrado.")
        elif escolha == "5":
            plataforma.realizar_compra()
        elif escolha == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Criação de jogadores e jogos
jogador1 = Jogador("123", 456, 100.0)
jogador2 = Jogador("Eduzinho", 432, 50.0)
jogo1 = Jogo("CS", "Tiro", "18+", 0.0)
jogo2 = Jogo("Minecraft", "Sandbox", "L", 90.00)

# Inicializando a plataforma
jogos = []
lista_jogadores = []
plataforma1 = Plataforma(jogos, lista_jogadores)

# Adicionando jogadores e jogos à plataforma
plataforma1.adicionar_jogador(jogador1)
plataforma1.adicionar_jogador(jogador2)
plataforma1.adicionar_jogo(jogo1)
plataforma1.adicionar_jogo(jogo2)

# Iniciando o menu
menu(plataforma1)
