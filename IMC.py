
print("--- Calculadora de indice de massa corporal (IMC) ---")
nome = str(input('Olá, qual o seu nome? '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura*altura)
if imc < 18.5:
    print('Você está abaixo do peso ideal! Seu IMC é de: {:.1f}' .format(imc))
elif 18.5 < imc < 25:
    print('{}, você está no peso ideal! Seu IMC é de: {:.1f}' .format(nome, imc))
elif 25 < imc < 40:
    print('{}, você está com sobrepeso! Seu IMC é de: {:.1f}' .format(nome, imc))
else:
    print('{}, você está com obesidade morbida! Seu IMC é de: {:.1f}'.format(nome, imc))
