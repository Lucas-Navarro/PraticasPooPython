from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, snome, email, tel, salario):
        super().__init__(nome, snome, email, tel)
        self.salario = salario

    def ExibirSalario(self, salario):
        if salario  > 4000:
            return 'Salário acima da média'
        else:
            return 'Salário abaixo da média'
        
prof1 = Professor('Maria', 'Santos', 'maria123@gmail.com', '11 7878-5858', 5000)
print(prof1.ExibirNome_Completo())
print(prof1.ExibirSalario(prof1.salario))

