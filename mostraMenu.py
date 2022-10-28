#Função mostrarmenu

def mostrarMenu(letra):
    menu = 1
    if menu <= 1:
        print("Menu de opções")
        print("a - Mostrar Saldo")
        print("b - Efetuar Deposito")
        print("c - Efetuar Saque")
        print("d - Finalizar")
    
    letra = input("Selecione uma letra: ")
    menu = 2
    return letra
    

