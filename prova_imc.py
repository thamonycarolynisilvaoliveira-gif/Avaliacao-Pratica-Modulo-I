# Entrada de dados
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibição do valor formatado
print(f"IMC: {imc:.2f}")

# Classificação do IMC
if imc < 18.5:
    print("Abaixo do peso ⚖️")
elif imc < 24.9:
    print("Peso normal 💪")
elif imc < 29.9:
    print("Sobrepeso 🍔")
elif imc < 34.9:
    print("Obesidade Grau I 🟠")
elif imc < 39.9:
    print("Obesidade Grau II 🔴")
else:
    print("Obesidade Grau III (mórbida) 🚨")