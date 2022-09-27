MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Iforme sua idade: "))

if idade >= 18:
    print("Maior de idade, apto a tirar CNH!")


if idade < MAIOR_IDADE:
        print("Menor de idade não pode tirar CNH.")



if idade >= 18:
    print("Maior de idade, apto a tirar CNH!")
else:
    print("Menor de idade não pode tirar CNH.")



if idade >= MAIOR_IDADE:
    print("Maior de idade, apto a tirar CNH!")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar CNH.")



