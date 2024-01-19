import random
def jogar():
    print('                                      ')
    print(' - - - - - - - - - - - - - - - - - - -')
    print(' Olá, bem-vindo ao jogo de advinhação!')
    print(' - - - - - - - - - - - - - - - - - - -')
    print('                                      ')
    numero_secreto = random.randrange(1, 11)
    tentativas = 0

    print('Decida o nível de dificuldade')
    print('[1]Fácil  [2]Médio  [3]Difícil')
    nivel = int(input('Nivel: '))

    if nivel == 1:
        tentativas = 3
    elif nivel == 2:
        tentativas = 2
    elif nivel == 3:
        tentativas = 1

    for rodada in range(0, tentativas):
        print(f'Tentativa {rodada} de {tentativas}')
        entrada = int(input("Digite um numero de 0 a 10: "))
        if entrada < 0 or entrada > 10:
            print("O numero digitado não está entre 0 e 10! Tente novamente")
            continue
        if numero_secreto == entrada:
            print(f'\n****** UHUL, você acertou!******\n')
            print('            \n--------\nEND GAME\n--------')
            break
        else:
            if numero_secreto < entrada:
                print(f'Que pena, você errou! O numero secreto é menor que {entrada}')
            else:
                print(f'\nQue pena, você errou! O numero secreto é maior que {entrada}')                          
if (__name__=="__main__"):
    jogar()