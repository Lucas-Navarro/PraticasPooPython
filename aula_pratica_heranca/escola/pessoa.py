class Pessoa:
    def __init__(self, nome, snome, email, tel):
        self.nome= nome
        self.snome = snome
        self.email = email
        self.tel = tel
    
    def ExibirNome_Completo(self):
        return "Nome Completo: " + self.nome + " " + self.snome
    
    def ExibirEmail(self):
        return 'E-mail: ' + self.email
    
    def ExibirTel(self):
        return 'Telefone: ' + self.tel
    
p1 = Pessoa('Maria', 'Santos', 'maria123@gmail.com', "11 7878-5858")
print(p1.ExibirNome_Completo())

p2 = Pessoa('José', 'Ferreira', 'jferreira321@gmail.com', '11 5252-2323')
print(p2.ExibirNome_Completo())
