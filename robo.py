import pyautogui
from time import sleep

pyautogui.click(615,261, duration=1)
pyautogui.press('enter')
sleep(3)
pyautogui.click(986,615, duration=2)
pyautogui.write('thiago123')
pyautogui.press('enter')
sleep(2)
pyautogui.press('enter')
#Clicar em novo produto
pyautogui.click(66,45, duration= 1)

#Adicionar produtos
with open('itens_novo.txt', 'r') as arquivo:
    for linha in arquivo:
        id_prod = linha.split(',')[0]
        nome = linha.split(',')[1]
        qntd = linha.split(',')[2]
        preco = linha.split(',')[3]


        pyautogui.click(215,87)
        pyautogui.write(id_prod)
        pyautogui.click(216,150)
        pyautogui.write(nome)
        pyautogui.click(256,217)
        pyautogui.write(qntd)
        pyautogui.click(220,277)
        pyautogui.write(preco)
        pyautogui.click(235,324)
        sleep(1)
        pyautogui.press('enter')