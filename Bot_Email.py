#    Automação acessando API financeira do Yahoo
# 1- buscar automaticamente os dados
# 2- gerar as análises de forma automática 
# 3- enviar um email com os dados

import yfinance as yf
import matplotlib.pyplot as plt
import warnings
import pyautogui
import pyperclip
from time import sleep
import webbrowser

# Ignorar avisos de FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)  

ticker = input("Digite o ticker da ação desejada: ")

# Obtém os dados históricos
dados = yf.Ticker(ticker).history("6mo")

# Plota o gráfico e obtém a figura
figura = plt.figure()
dados['Close'].plot()
plt.title(f'Histórico de Fechamento para {ticker}')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
figura.savefig('meu_grafico.png')  #salvar 


fechamento=dados['Close']  #Aqui considero apenas a coluna "Close"
maxima=fechamento.max()
minima=fechamento.min()
atual=fechamento.iloc[-1]


#enviar por email
email = f'https://gmail.com' 
webbrowser.open(email)
sleep(6)
pyautogui.click(x=108, y=212)
sleep(3)
pyperclip.copy("email@gmail.com")
pyautogui.hotkey("ctrl", "v")
sleep(3)
pyautogui.hotkey("tab")
sleep(3)
pyperclip.copy("Análises diárias")
pyautogui.hotkey("ctrl", "v")
sleep(3)
pyautogui.hotkey("tab")
sleep(3)

mensagem = f"Seguem as análises diárias dos ultimos seis meses da ação: {ticker}\nCotação máxima: R${round(maxima,2)}\nCotação mínima R${round(minima,2)}\nCotação atual R${round(atual,2)}.\nQualquer dúvida estou a disposição!"
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

sleep(6)
pyautogui.click(x=850, y=695)
