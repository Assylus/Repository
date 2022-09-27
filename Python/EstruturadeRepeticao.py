#texto = input("informe um texto:")
from timeit import repeat


texto = ""
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end = "")
else:
    print() # adiciona uma quebra de linha
    print("Executa no final do laço")


for numero in range(0, 11):
    print(numero, end=" ")

#Exibindo tabuada
for numero in range(0, 91, 9):
    print(numero, end=" ")


#opcao = -1
#while opcao !=0:
#    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n:"))
#    if opcao == 1:
#        print("Eita poha olha o dinheiro!!!")
#    elif opcao == 2:
#        print("Exibindo o extrato...")


#while True:
#    numero = int(input("Informe um número: "))

#    if numero == 10:
#        break

#    print(numero)

for numero in range(100):

    if numero % 2 == 0 :
        continue

    print(numero, end=" ")