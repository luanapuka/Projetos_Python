print("                                                       ")
print("\n\033[1;91mBem-vindo(a) a sua agenda virtual!\033[0;0m")
print("                                                       ")
datas = []

for i in range(1, 31):
    mes = input("Para iniciar as anotações, digite o nome do mês: ")
    mes = mes.upper()
    dia = int(input("Agora, digite o dia: "))
    horario=str(input("Horário: "))
    compromisso = input("Compromisso/Anotação: ")
    compromisso = compromisso.upper()
    prosseguir = input("\nDeseja fazer mais anotações? [S/N]\n")
    prosseguir = prosseguir.upper()
    datas.append({'Mês': mes, 'Dia': dia, 'Horário':  horario, 'Compromisso/Anotação': compromisso})
    if prosseguir == "S":
        continue
    else:
        print("\n------------Anotações finalizadas------------\n")
        break

verificar_anotacoes = input("\nDeseja verificar suas anotações? [S/N]\n")
verificar_anotacoes = verificar_anotacoes.upper()
if verificar_anotacoes == 'S':
    for data in datas:
        print('\n')
        for chave, valor in data.items():
            print("{} -> {}".format(chave, valor))
else:
    if verificar_anotacoes != "N":
        print("Opção inválida")

print("\n------------- Finalizando Agenda! ----------------")