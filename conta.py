class ContaBancaria:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de ${valor} realizado. Saldo atual: ${self._saldo}")
        else:
            print(f"Valor de depósito inválido.")
    
    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            print(f"Saque de ${valor} realizado. Saldo atual: ${self._saldo}")
        else:
            print("Operação Cancelada.\nSaldo Insuficiente.")
            
    def get_saldo(self):
        return self._saldo
    
minha_conta = ContaBancaria(1000)
minha_conta.depositar(100)
minha_conta.sacar(200)

print(f"Saldo final: ${minha_conta.get_saldo()}")