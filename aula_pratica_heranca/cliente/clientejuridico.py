from cliente import Cliente

class ClienteJuridico(Cliente):
    def __init__(self, codigo, endereco, data_cadastro, cnpj, razaosocial):
        super().__init__(codigo, endereco, data_cadastro)
        self.cnpj = cnpj
        self.razaosocial = razaosocial
    
    def VerificarCNPJ(self):
        return 'CNPJ: ' + self.cnpj
    
clientejuridico = ClienteJuridico('9762397', 'Rua Ordilon de Souza, 240, Apartamento 132', '23/07/2023', '12893273123', '93012')
print(clientejuridico.VerificarCNPJ())