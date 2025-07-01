from veiculo import Veiculo

class Motocicleta(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, preco, cilindrada):
        super().__init__(tipo, chassi, marca, modelo, ano, preco)
        self.cilindrada = cilindrada

    def ExibirCilindrada(self):
        return 'Cilindradas: ' + self.cilindrada
    
    def PrecoVeiculo(self):
        return self.preco + (self.preco * 0.30)
    
motocicleta1 = Motocicleta('Motocicleta', '38291DKAS', 'Honda', 'AKUMA', '2015', 30000.0, '200c')
print(motocicleta1.ExibirCilindrada())
print(motocicleta1.PrecoVeiculo())