from veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, preco, eixo):
        super().__init__(tipo, chassi, marca, modelo, ano, preco)
        self.eixo = eixo
    
    def ExibirTipoEixo(self):
        if(self.eixo == 1):
            return '1 eixo: Até 6 toneladas'
        elif (self.eixo == 2):
            return '2 eixos: Até 13 toneladas'
        elif (self.eixo == 3):
            return '3 eixos: Até 30 toneladas'
        else:
            return 'Valor Inválido'
    
    def PrecoVeiculo(self):
        return self.preco + (self.preco * 0.80)
    
caminhao1 = Caminhao('Caminhão', '129038129', 'Mercedes', '23AB', '2015', 200000.0, 2)
print(caminhao1.ExibirTipoEixo()) 
print(caminhao1.PrecoVeiculo())
