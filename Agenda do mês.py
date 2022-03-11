
print("\n\033[1;91mBem-vindo(a) a sua agenda virtual!\033[0;0m")
mes = input("Para fazer suas anotações, digite o nome do mês: ")
mes = mes.upper()
datas = []

for i in range(1, 31):
    dia = int(input("Digite a data: "))
    compromisso = input("Compromisso dessa data: ")
    compromisso = compromisso.upper()
    horario=str(input("Horário do compromisso: "))
    prosseguir = input(f"Deseja anotar outro compromisso em {mes}? [S/N] ")
    prosseguir = prosseguir.upper()
    datas.append({'Dia': dia, 'Horário':  horario, 'Compromisso': compromisso})
    if prosseguir == "S":
        continue
    else:
        print("\n------------Anotações finalizadas------------\n")
        break

verificar_anotacoes = input("Deseja verificar suas anotações? [S/N] ")
verificar_anotacoes = verificar_anotacoes.upper()
if verificar_anotacoes == 'S':
    print('\n-------------\033[1;91m     Mês:{}\033[0;0m    ----------------'.format(mes))
    for data in datas:
        print('\n')
        for chave, valor in data.items():
            print("{} -> {}".format(chave, valor))
else:
    if verificar_anotacoes != "N":
        print("Opção inválida")

print("\n------------- Finalizando Agenda! ----------------")
