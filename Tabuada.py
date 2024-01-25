print('=======Tabuada==========')
num=int(input('Digite um numero: '))
for c in range(1,11,1):
    mult = num * c
    print('{} x {:2} = {}'.format(num, c, mult))
print('Fim')
