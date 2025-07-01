from cliente import Cliente

class ClienteFisico(Cliente):
    def __init__(self, codigo, endereco, data_cadastro, nome, cpf):
        super().__init__(codigo, endereco, data_cadastro)
        self.nome = nome
        self.cpf = cpf

    def VerificarCPF(self):
        return 'CPF: ' + self.cpf 
    
clientefisico1 = ClienteFisico('9762397', 'Rua Ordilon de Souza, 240, Apartamento 132', '23/07/2023', 'Lucas', '11122233333')
print(clientefisico1.VerificarCPF())