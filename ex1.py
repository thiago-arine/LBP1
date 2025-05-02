class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def detalhes(self):
        details = {
            'titulo': f'{self.titulo}\n',
            'autor': f'{self.autor}\n',
            'paginas': self.paginas
        }
        
        return details.values()
        
livro1 = Livro('Maze Runner: Correr ou Morrer', 'James Dashner', 428)
livro2 = Livro('Fragmentos de Uma Vida', 'Rita Braun', 158)
livro3 = Livro('Fahrenheit 451', 'Ray Bradbury', 216)
livro4 = Livro('Adultos', 'Emma Jane Unsworth', 400)
livro5 = Livro('Fundação', 'Isaac Asimov', 320)

meu_livro = livro1
format = meu_livro.detalhes()

print(*format)