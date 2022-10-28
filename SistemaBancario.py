# Sitema basico de um banco

from mostraMenu import mostrarMenu
valor = 0
saldo = 100
encerraPrograma = bool
letraDig = ""


encerraPrograma = False

while encerraPrograma == False:
        opcaoSelecionada = mostrarMenu(letraDig) # Chama função mostrar menu
        
        
        if opcaoSelecionada == "a":
                print("Seu saldo é: ",saldo)
        elif opcaoSelecionada == "b":
                valor = int(input("Digite valor a depositar: "))
                saldo = valor + saldo
                print ("Deposito efetuado")
        elif opcaoSelecionada == "c":
                valor = int(input("Digite o valor a retirar: "))
                if valor > saldo:
                        print("Saldo insuficiente, seu saldo é : ",saldo)
                else:
                        saldo = saldo - valor
                        print("Saque efetuado")
        elif opcaoSelecionada == "d":
                encerraPrograma = True
        else:
                print("Opcao invalida, tente novamente")
                