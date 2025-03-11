#Desafio, criar uma função que calcule a gorjeta de uma conta em um restaurante

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

total_conta = 100.00
porcentagem = 15
gorjeta = calcular_gorjeta(total_conta, porcentagem)
print(f'Para uma conta de R$ {total_conta:.2f} com gorjeta de {porcentagem}% a gorjeta é R$ {gorjeta:.2f}')