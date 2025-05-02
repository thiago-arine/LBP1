class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def emitir_som(self):
        print("Som animal")
    
    def identidade(self):
        print(f"Meu nome é {self.nome}")
        
class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")
        
class Gato(Animal):
    def emitir_som(self):
        print("Miau miau...")
        
class Peixe(Animal):
    def emitir_som(self):
        print("🫧")
        
def fazer_som(Animal):
    Animal.emitir_som()
        
# meu_gato = Gato("Neymar", 4)
# meu_gato.emitir_som()
# meu_gato.identidade()
# meu_cachorro = Cachorro("Santos", 1)
# meu_cachorro.emitir_som()
# meu_cachorro.identidade()
meu_peixe = Peixe("Tralalelo Tralala", None)
# meu_peixe.emitir_som()
# meu_peixe.identidade()

fazer_som(meu_peixe)