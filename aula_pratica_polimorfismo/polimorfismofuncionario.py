class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def Calcular_salario(self):
        pass

class Contratado_Carteira(Funcionario):
    def __init__(self, nome, quantidade_horas, valor_hora):
        super().__init__(nome)
        self.quantidade_horas = quantidade_horas
        self.valor_hora = valor_hora

    def Calcular_salario(self):
        return self.quantidade_horas * self.valor_hora
    
class Comissionado_Temporario(Funcionario):
    def __init__(self, nome, total_vendas):
        super().__init__(nome)
        self.total_vendas = total_vendas

    def Calcular_salario(self):
        return self.total_vendas * 0.1
    
empregado = Contratado_Carteira('Elenne', 160, 8.50)
comissonado = Comissionado_Temporario('Lucas', 1200)
print('Salário: ', empregado.Calcular_salario())
print('Comissão: ', comissonado.Calcular_salario())