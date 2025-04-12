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
        print(f'\33[1;34m{"EXTRATO DA CONTA":^40}\33[m')
        print('='*40)
        data=datetime.today().date().strftime("%d/%m/%y")
        print(f'\33[33m{"DATA":.<30} {data}')
        saldo=self.saldo
        print(f'{"SALDO":.<30} R${saldo:.2f}\33[m')
        return f'status: concluido\n'

    def depositar(self,valor):
        self.saldo+=valor
        print()

    def sacar(self,sacar):
        if sacar>self.saldo:
            print(f'status:seu saldo é insuficiente para o saque!')
            print()
            return False
        else:
            self.saldo-=sacar
            print(f'status:Saque de R${sacar:.2f} realizado com sucesso!')
            print()
            return True
    def transferir(self,contaDestino,valor):
        if transferir>self.saldo:
            print('status:Seu saldo é insuficiente para a transferência')
            print()
        else:
            contaDestino.depositar(valor)
            self.saldo-=valor
            print(f'{"status:"}{"A transferência de R$":^23}{transferir:>1.2f}\n '
                  f'{"foi realizada com sucesso!":^40}')
            print()
    def dados(self):
        print(f'\33[1;34m{"DADOS":^40}\33[m')
        print("~"*40)
        print(f'\33[33m{"SUA CONTA:":.<36}{self.idConta:>3}')
        print(f'{"TITULAR DA CONTA:":.<32}{self.titularConta:>3}')
        print(f'{"CPF:":.<25}{self.Cpf:>7}\33[m')
        print('~'*40)
        print()
        return f'status:concluido com sucesso!'


#conta cadastradas
conta1=Conta(242,"111.111.111-11","Leandro",1200.00)
conta2=Conta(243,"000.000.000-00","Solangy",3000.00)
#metodos e chamadas de funções

resp='N'
while resp !='S':
    print(f'\33[1;33m{"BANCO PYTHON":^40}\33[m')
    print('='*40)
    print(f'\33[33m{"EXTRATO[0]":<28}{"DEPOSITAR[1]":>7}')
    print()
    print(f'{"SACAR[2]":<28}{"TRANSFERIR[3]":>7}')
    print()
    print(f'{"SEUS DADOS[4]":<28}{"ENCERRAR[5]":>7}\33[m')
    print('='*40)


    try:
            opcoes = int(input(f'\33[31m{"Digite sua opção:"}\33[m'))
            print()
            if opcoes==0:
                print('gerando...')
                sleep(1.5)
                print(f'{conta1.extrato()}')
                continue
            elif opcoes==1:
                depositar=float(input('Quanto deseja depositar?:R$'))
                sleep(1.5)
                conta1.depositar(depositar)
                print('status:Operação realizado com sucesso!')
                continue
            elif opcoes==2:
                sacar=float(input('Quanto deseja sacar?:R$'))
                sleep(1.5)
                conta1.sacar(sacar)
                continue
            elif opcoes==3:
                sleep(0.5)
                transferir=float(input('Quanto deseja transferir?:R$'))
                print(f'\33[1;34m{"CONFIRA OS DADOS PARA A TRANSFÊNCIA":^40}\33[m')
                print("~"*40)
                print(f'\33[33m{"CONTA:":.<35} {conta2.idConta:>2}')
                print(f'{"TITULAR DA CONTA:":.<31} {conta2.titularConta:>7}\33[m')
                print("~"*40)
                confirme=str(input('Os dados estão corretos?[S/N]:')).upper().strip()[0]
                if confirme=='S':
                    sleep(2)
                    conta1.transferir(conta2,transferir)
                    continue
                elif confirme=='N':
                    print('Retornar ao menu principal')
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
            else:
                print('Erro ao digitar numero!')
    except (ValueError,TypeError):
        print('erro!Digito incompativel com a opção')
        continue
    except (KeyboardInterrupt):
        print('Usuario optou por sair do programa!')
        continue
    else:





        resp=str(input('Deseja sair da conta [S/N]:')).upper().strip()[0]

