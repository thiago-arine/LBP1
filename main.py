class Jogo:
    def __init__(self,titulo,genero,classificacao,preço):
        self.titulo = titulo
        self.genero = genero
        self.classificacao = classificacao
        self.preço = preço
    def exibir_detalhes(self):
        detalhes = {"titulo" : self.titulo,  "genero" :self.genero, "classificacao" : self.classificacao  ,"preço": self.preço}
        return detalhes.values()
    

class Jogador:
    def __init__(self,nick,id,saldo):
            self.nick = nick
            self.id = id
            self.jogos = []
            self.saldo = saldo
    def exibir_perfil(self):
        detalhes_perfil = {"nick" : self.nick,  "id" :self.id,"saldo": self.saldo}
        return detalhes_perfil.values()
    def adicionar_jogo(self,jogo):
        self.jogo = jogo
        self.jogos.append(jogo)
        print(*self.jogos)
        return self.jogos
    def adicionar_saldo(self):
         self.newValor = float(input("Qual o valor a ser depositado?"))
         self.saldo += self.newValor
         print(self.saldo)
         return self.saldo
    def debitar_saldo(self):
        self.newDebito = float(input("Qual o valor a ser debitado?"))
        if self.newDebito <= self.saldo:
              self.saldo -= self.newDebito
              print(self.saldo)
        else:
             print("Saldo insuficiente!")
        return self.saldo
    
class Plataforma:
    def __init__(self,todos_jogos, lista_jogadores):
          self.todos_jogos = todos_jogos
          self.lista_jogadores = lista_jogadores
    
    def adicionar_jogo(self,jogo):
        self.jogo = jogo
        self.todos_jogos.append(jogo)
        return self.todos_jogos

     
    def adicionar_jogador(self,jogador):
        self.jogador = jogador
        self.lista_jogadores.append(jogador)
        return self.lista_jogadores
    def buscar_jogo_titulo(self):
        self.busca_nome = input("Qual o nome do jogo")
        for i in self.todos_jogos:
             if self.busca_nome == self.jogo:
                  return self.jogo



jogador1 = Jogador("123", 456, 0.0)
jogador2 = Jogador("Eduzinho", 432, 0.0)
jogo1 = Jogo("Cs", "tiro", "+18", 00.0)
jogo2 = Jogo("Minecraft", "aventura","L", 90.00 )
jogador1.adicionar_jogo(jogo1.titulo)
jogador1.adicionar_jogo(jogo2.titulo)
# jogador1.adicionar_saldo() 
# jogador1.debitar_saldo()
jogos = []
listaJogadores = []
plataforma1 = Plataforma(jogos,listaJogadores)
plataforma1.adicionar_jogador(jogador1.nick)
plataforma1.adicionar_jogo(jogo1.titulo)
print(*plataforma1.adicionar_jogador(jogador2.nick))
print(*plataforma1.adicionar_jogo(jogo2.titulo))
print(*plataforma1.buscar_jogo_titulo())