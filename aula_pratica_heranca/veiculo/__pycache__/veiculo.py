class Veiculo:
    def __init__(self, tipo, chassi, marca, modelo, ano, preco):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def ExibirChassi(self):
        return "Chassi: " + self.chassi
    
    def ExibirAnoMarcaModelo(self):
        return "Ano: " + self.ano + "/ Marca: " + self.marca + "/ Modelo: " + self.modelo
    
    def PrecoVeiculo(self):
        return self.preco + (self.preco * 0.50)

veiculo1 = Veiculo('Carro', '38921083121JAA', 'Chevrolet', 'Camaro v2', '2012', 10000.0)
print(veiculo1.ExibirChassi())
print(veiculo1.ExibirAnoMarcaModelo())
print(veiculo1.PrecoVeiculo())