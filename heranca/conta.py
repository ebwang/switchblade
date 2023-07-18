import cliente

class Conta(cliente.Cliente):
    def __init__(self, numero, titular, limite, saldo):
        super().__init__(titular)
        self.__numero__ = numero
        self.__saldo__ = saldo
        self.__limite__ = limite

    def deposito(self, valor):
        self.__saldo__ += valor
        print("Deposito de {} efetuado com sucesso".format(valor))

    def saque(self,valor):
        if(self.__validar_saldo_transacao(valor)):
            self.__saldo__ -= valor
            print("Saque de {} efetuado com sucesso".format(valor))
            return True
        else:
            print("Saldo insuficiente para transacao de {}".format(valor))
            return False

    def extrato(self):
        print("Seu saldo {} é de {}".format(self.titular, self.__saldo__))

    def transferir(self,destino,valor):
        if(self.saque(valor)):
            destino.deposito(valor)
            print("Valor de {} foi transferido da conta do {} para {}".format(valor, self.titular, destino.titular))
        else:
            print("Nao foi possivel a transferencia do valor {}".format(valor))

    #Isso funciona como uma anotacao de get 
    @property
    def saldo(self):
        return self.__saldo__
    
    #Isso funciona como uma anotacao para o set
    @saldo.setter
    def saldo(self, valor):
        self.__saldo__ = valor
 
    @property
    def limite(self):
        return self.__limite__

    @limite.setter
    def limite(self, limite):
        self.__limite__ = limite

    def __validar_saldo_transacao(self,valor):
        saldo_transacao = self.__limite__ + self.__saldo__
        return (saldo_transacao > valor)


