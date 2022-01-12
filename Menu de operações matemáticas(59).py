#Aula 14

valor1 = 1
valor2 = 1
menu = 0
while menu != 5:
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    print('[1]Somar \n[2]Multiplicar \n[3]Subtrair \n[4]Maior número\n[5]Novos números \n[6]Sair do programa')
    menu = int(eval(input('Qual operação do menu você deseja? ')))
    if menu == 1:
        soma = valor1 + valor2
        print('A soma dos valores {} e {} é: {}' .format(valor1, valor2, soma))
    elif menu == 2:
        mult = valor1*valor2
        print('A multiplicação dos valores {} e {} é: {}'.format(valor1, valor2, mult))
    elif menu == 3:
        subt = valor1 - valor2
        print('A subtração dos valores {} e {} é: {}' .format(valor1, valor2, subt))
    elif menu == 4:
        if valor1 > valor2:
            print('O valor {} é maior que o valor {}' .format(valor1, valor2))
        else:
            print('O valor {} é maior que o valor {}'.format(valor2, valor1))
    elif menu == 5:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
        print('[1]Somar \n[2]Multiplicar \n[3]Subtrair \n[4]Maior número\n[5]Novos números \n[6]Sair do programa')
        menu = int(eval(input('Qual operação do menu você deseja? ')))
if menu == 6:
  print('Encerrando o programa!')
