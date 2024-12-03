

class Cliente:
    def __init__(self, id_cliente, nome, endereco):
        self.id_cliente = id_cliente
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        return f"Cliente ID: {self.id_cliente}, Nome: {self.nome}, Endereço: {self.endereco}"


# Criar instâncias de clientes
cliente1 = Cliente(id_cliente=1, nome="Antonio Silva", endereco="Rua das Quintas, 150")
cliente2 = Cliente(id_cliente=2, nome="Mario Gomes", endereco="Avenida Rollemberg, 180")

# Exibir os dados dos clientes
print(cliente1)
print(cliente2)
