# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intersivao/login
# Passo 2: Fazer login
# Passo 3: Importar a base de produtos para cadastrar
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o processo de cadastro até o fim

#########################################################################################################################################

# Passo 1: Entrar no sistema da empresa

import pyautogui
import time

# pyaytogui.write   escrever um texto
# pyautogui.press   apertar 1 tecla
# pytoautogui.click    clica em algum lugar da tela
# pyautogui.hotkey   combinação de teclas
# pyautogui.PAUSE = 1    um tempo de pausa entre cada acao e determinada em segundo

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3) # espera 3 segundos nesta linha




# Passo 2: Fazer login

pyautogui.press("tab")
# pyautogui.click(x=973, y=490)
pyautogui.write("pythondospythons@gmail.com")
pyautogui.press("tab")
pyautogui.write("lalabilou")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3) # espera 3 segundos nesta linha
pyautogui.press("tab")

# Passo 3: Importar a base de produtos pra cadastrar

import pandas as pd

tabela = pd.read_csv("produtos.csv")





# Passo 4: Cadastrar um produto e 5

for linha in tabela.index:

    # pegar da tabela um valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"] # serve para pegar o valor que tem na linha e na coluna determinada la da base

    # preencher o campo

    pyautogui.write(str(codigo)) # necessario converter para string para ter certeza de funcionar com o write
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    for _ in range(7):
        pyautogui.hotkey("shift", "tab")