from datetime import datetime
from time import sleep


class Conta:
    from datetime import date
    def __init__(self,idConta,Cpf,titularConta,saldo):
        self.idConta=idConta
        self.Cpf=Cpf
        self.titularConta=titularConta
        self.saldo=saldo

    def extrato(self):
        print(f'{"EXTRATO DA CONTA":^40}')
        print('='*40)
        data=datetime.today().date().strftime("%d/%m/%y")
        print(f'{"DATA":.<30} {data}')
        saldo=self.saldo
        print(f'{"SALDO":.<30} R${saldo:.2f}')
        return f'status: concluido\n'

    def depositar(self,valor):
        self.saldo+=valor
        print(f'status:Deposito de R${valor:.2f} realizado com sucesso!')

    def sacar(self,sacar):
        if sacar>self.saldo:
            print(f'status:seu saldo é insuficiente para o saque!')
            return False
        else:
            self.saldo-=sacar
            print(f'status:Saque de R${sacar:.2f} realizado com sucesso!')
            return True
    def transferir(self,contaDestino,valor):
        if transferir>self.saldo:
            print('status:Seu saldo é insuficiente para a transferência')
        else:
            contaDestino.depositar(valor)
            self.saldo-=valor
            print(f'status:A transferência de R${transferir} foi realizada com sucesso!')
    def dados(self):
        print(f'{"SUA CONTA:":.<36}{self.idConta:>3}')
        print(f'{"TITULAR DA CONTA:":.<32}{self.titularConta:>3}')
        print(f'{"CPF:":.<25}{self.Cpf:>7}')
        return f'status:concluido com sucesso!'


#conta cadastradas
conta1=Conta(242,"111.111.111-11","Leandro",1200.00)
conta2=Conta(243,"000.000.000-00","Solangy",3000.00)
#metodos e chamadas de funções

resp='N'
while resp !='S':
    print(f'{"BANCO PYTHON":^40}')
    print('='*40)
    print(f'{"EXTRATO[0]":<28}{"DEPOSITAR[1]":>7}')
    print()
    print(f'{"SACAR[2]":<28}{"TRANSFERIR[3]":>7}')
    print()
    print(f'{"SEUS DADOS[4]":<28}{"ENCERRAR[5]":>7}')
    print('='*40)
    opcoes=int(input('Digite sua opção:'))

    print()
    if opcoes==0:
        print('gerando...')
        sleep(1.5)
        print(f'{conta1.extrato()}')
        continue
    elif opcoes==1:
        depositar=float(input('Quanto deseja depositar?:'))
        sleep(1.5)
        conta1.depositar(depositar)
        continue
    elif opcoes==2:
        sacar=float(input('Quanto deseja sacar?:'))
        sleep(1.5)
        conta1.sacar(sacar)
        continue
    elif opcoes==3:
        transferir=float(input('Quanto deseja transferir?:'))
        print('CONFIRA OS DADOS PARA A TRANSFÊNCIA')
        print(f'Conta que será depositada: {conta2.idConta}')
        print(f'Titular da conta: {conta2.titularConta}')
        conta1.transferir(conta2,transferir)
        continue
    elif opcoes==4:
        print('aguarde...')
        sleep(1)
        print(conta1.dados())
        continue
    elif opcoes==5:
        print('saindo....')
        sleep(1.5)
        break
    resp=str(input('Deseja sair da conta [S/N]:')).upper().strip()[0]

