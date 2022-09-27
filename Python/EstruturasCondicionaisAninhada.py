
conta_nomral = False
conta_universitaria = False
conta_especial = True

saldo = 5000
saque = 1500
cheque_especial = 1500

if conta_nomral:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso de cheque especial!")

    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")
    
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucessso!")

    else:
        print("Saldo Insuficiente!")
        
elif conta_especial:
    print("Conta especial selecionada")

else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o gerente!")

