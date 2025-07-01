class Conta:
    def __init__(self, numero_conta, nome_cliente):
        self.__saldo = 0
        self.numero_conta = numero_conta
        self.nome_cliente = nome_cliente
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, novo_saldo):
        raise ValueError('Impossivel modificar diretamente o saldo!!')

    def deposito(self, valor_deposito):
        self.__saldo += valor_deposito
        return self.__saldo

    def saque(self, valor_saque):
        self.__saldo -= valor_saque
        return self.__saldo

cliente1 = Conta('25000', 'Yan Schimitt')
cliente1.saldo = 8000

class ContaCorrente(Conta):
    def __init__(self, numero_conta, nome_cliente):
        super().__init__(numero_conta, nome_cliente)

    def saque(self, valor_saque):
        if(valor_saque > self.__saldo):
            diferenca = valor_saque  - self.__saldo
            self.__saldo = (diferenca * 0.1) + diferenca
            return self.__saldo

cliente2 = ContaCorrente(100, 'Thais')
print(cliente2.saldo)

cliente2.deposito(100)
print('Saldo: ', cliente2.saldo)

cliente2.saque(200)
print('Saldo: -', cliente2.saldo)