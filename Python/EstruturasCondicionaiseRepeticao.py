def sacar(valor):
    saldo = 200

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")
    if saldo <= valor:
        print("Saldo Invalido")
    
    print("Tenha um bom dia!")

sacar(300)



def depositar(valor):
    saldo = 200
    saldo += valor

