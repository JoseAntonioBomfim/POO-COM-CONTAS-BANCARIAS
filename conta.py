import datetime
from extrato import Extrato
from cliente import Cliente  # Importe a classe Cliente, se necessário

class Conta:
    def __init__(self,clientes,numero,saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.abertura = datetime.datetime.today()
        self.extrato = Extrato () 

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO", valor, "Data",datetime.datetime.today ()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()]) 
            return True

    def transfereValor(self, contadestino, valor):
        if self.saldo < valor:
            return "Não existe saldo suficiente"
        else:
            contadestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()]) 
            return "Transferencia Realizada"

    def extrato(self, extrato):
        extrato.extrato(self.numero)
        
    def gerarsaldo(self):
        print(f"numero: {self.numero}\n saldo:{self.saldo}")


# Criar instâncias de Cliente
cliente1 = Cliente(id_cliente=1, nome="João Silva", endereco="Rua das Flores, 123")
cliente2 = Cliente(id_cliente=2, nome="Maria Oliveira", endereco="Avenida Brasil, 456")

# Criar instâncias de Conta
conta1 = Conta(clientes=[cliente1], numero="001", saldo=1500)
conta2 = Conta(clientes=[cliente2], numero="002", saldo=800)

# Exibir saldos iniciais
print("Saldos iniciais:")
conta1.gerarsaldo()
conta2.gerarsaldo()

# Realizar operações
print("\nRealizando operações...")

# Depositar na conta1
conta1.depositar(500)
print("\nApós depósito de R$500 na conta1:")
conta1.gerarsaldo()

# Sacar da conta2
sucesso_saque = conta2.sacar(300)
print("\nTentativa de saque de R$300 na conta2:")
if sucesso_saque:
    print("Saque realizado com sucesso.")
else:
    print("Saldo insuficiente.")
conta2.gerarsaldo()

# Transferência de conta1 para conta2
resultado_transferencia = conta1.transfereValor(conta2, 1000)
print("\nTentativa de transferência de R$1000 de conta1 para conta2:")
print(resultado_transferencia)
conta1.gerarsaldo()
conta2.gerarsaldo()

