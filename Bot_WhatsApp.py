# 1º Ler dados da planilha (nome, telefone e data de vencimento da fatura)
# 2º Criar mensagem
# 3º Abrir o whatsApp Web por meio do link personalizado
# 4º Enviar mensagem para cada cliente

import openpyxl
import webbrowser
from urllib.parse import quote
import pyautogui
from time import sleep

workbook = openpyxl.load_workbook('clientes(4).xlsx')    #nome do arquivo com os dados
pagina = workbook['Página1']                             #pagina onde se encontram os dados

for linha in pagina.iter_rows(min_row=2):
    nome_cliente = linha[0].value
    telefone = linha[1].value
    vencimento_fatura = linha[2].value

    if vencimento_fatura is not None:
        mensagem = f'Olá {nome_cliente}! Seu boleto vence no dia {vencimento_fatura.strftime("%d/%m/%Y")}. Favor pagar no link https://www.pagarfatura.com\nTenha um bom dia! '
    else:
        mensagem = f'Olá {nome_cliente}! Seu boleto está sem data de vencimento definida. Favor pagar no link https://www.pagarfatura.com\nTenha um bom dia! ' 

    try:
        link_whats = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_whats)
        sleep(15)

        seta= pyautogui.locateCenterOnScreen('seta2.png')  #localiza o botão "enviar" por meio da imagem fornecida
        sleep(7)

        pyautogui.click(seta[0], seta[1])  #coordenada x e y contido na variável seta
        sleep(7)

        pyautogui.hotkey('crtl','w')
        sleep(7)
    except:
        print(f'Não foi possivel enviar mensagem para {nome_cliente}')

       


