class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
    
    def mostrardados(self):
        return 'Nome: ' + self.nome + ' ' + 'Salário: ' + str(self.salario)
    
    def receber_bonificacao(self):
        return self.salario * 0.5
    
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self.senha = senha
        self.qtd_funcionarios = qtd_funcionarios
    
    def receber_bonificacao(self):
        return self.salario * 0.8
    
class Estagiario(Funcionario):
    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario)
        self.senha = senha
    
    def receber_bonificacao(self):
        return super().receber_bonificacao() + 180
    
gerente = Gerente('José', '222222222-22', 5000.0, '1234', 0)
print(gerente.mostrardados())
print(gerente.receber_bonificacao())


funcionario = Funcionario('Maria', '123432567', 5000.0)
funcionario = Funcionario('João', '111111111-11', 5000.0)
print(funcionario.mostrardados())
print(funcionario.receber_bonificacao())

estagiario = Estagiario('Lucas', '33333333-33', 5000.0, '123454')
print(estagiario.mostrardados())
print(estagiario.receber_bonificacao())

