class Cliente:
    def __init__(self, codigo, endereco, data_cadastro):
        self.codigo = codigo
        self.endereco = endereco
        self.data_cadastro = data_cadastro

    def LocalizarEndereco(self):
        return 'Endereço: ' + self.endereco
    
cliente1 = Cliente('9762397', 'Rua Ordilon de Souza, 240, Apartamento 132', '23/07/2023')
print(cliente1.LocalizarEndereco())