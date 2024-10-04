#Calculo de bonus com entrada do usuario
bonus2024 = 1000

nome = input("Digite seu nome? ")

salario = float(input("Qual seu salario? "))

bonus_percent = float(input("Qual o valor do bonus recebido? "))

total_bonus = (salario * bonus_percent) + bonus2024

print(f"{nome}, seu bonus sera de: {total_bonus}")


#bugs possiveis
#nao ha tratamento de erros de tipos (string, float, int)
#nao ha tratamento de erros de divisão por zero
#nao ha tratamento de erros de entrada de dados (input)