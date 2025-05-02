class Calculadora:
    def soma(soma, a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c
        
calc = Calculadora()
print(calc.soma(2, 3))
print(calc.soma(1, 1, 5))