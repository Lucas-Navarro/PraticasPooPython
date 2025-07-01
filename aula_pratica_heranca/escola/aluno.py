from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, snome, email, tel, N_Matricula):
        super().__init__(nome, snome, email, tel)
        self.N_Matricula = N_Matricula

    def ExibirMatricula(self):
        return "Número da mátricula: " + self.N_Matricula
    
aluno1 = Aluno('Elenne', 'Vitória', 'elenne444@gmail.com', '11 98424-2391', '1209391')
print(aluno1.ExibirNome_Completo())
print(aluno1.ExibirMatricula())