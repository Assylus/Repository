curso = "curso de python"
nome_curso = curso
saldo, limite = 199, 300

print(curso is nome_curso)
print(curso is not nome_curso)
print(curso is limite)



saldo = 1000
limite = 5000

print(saldo is limite)
print(saldo is not limite)