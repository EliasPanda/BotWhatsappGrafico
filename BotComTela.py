from tkinter import *
import customtkinter
import pyautogui as bot
from PIL import Image

tela = customtkinter.CTk(fg_color='black')

my_image = customtkinter.CTkImage(light_image=Image.open('imgs/pngwing.com.png'),
                                  dark_image=Image.open('imgs/pngwing.com.png'),
                                  size=(80, 80))
LabelImagem = customtkinter.CTkLabel(
                       tela, text='', image=my_image).place(x=210, y=10)
customtkinter.CTkLabel(tela,text='Bot', font=('Arial', 40, 'bold')).place(x=210, y=90)

tela.title('Calculando Tudo')
largura = 500
altura = 500
largura_tela = tela.winfo_screenwidth()
altura_tela = tela.winfo_screenheight()
posX = largura_tela / 2 - largura / 2
posY = altura_tela / 2 - altura  / 2
tela.geometry("%dx%d+%d+%d"%(largura, altura, posX, posY))
tela._set_appearance_mode('System')

entradaNavegador = customtkinter.CTkEntry(tela, width=300, placeholder_text='Digite O Nome do Navegador')
entradaNavegador.place(x=100, y=150)

entradaSite = customtkinter.CTkEntry(tela, width=300, placeholder_text='Digite O Nome do Site')
entradaSite.place(x=100, y=200)

entradaNomeGrupo = customtkinter.CTkEntry(tela, width=300, placeholder_text='Digite O Nome do Contato ou Grupo')
entradaNomeGrupo.place(x=100, y=250)

entradaMenssagem = customtkinter.CTkEntry(tela, width=300, placeholder_text='Digite A Menssagem a Ser Enviada')
entradaMenssagem.place(x=100, y=300)

def whats():
    bot.press('win') # press() ele pressiona a tecla, nesse caso mandei pressionar a tecla do windows 
    bot.sleep(3)
    bot.write(entradaNavegador.get())# write() é uma função para escrever algo, nesse caso ele escreve na pesquisa do menu inicar
    bot.sleep(3)
    bot.press('enter')# aqui ele preciona o ENTER
    bot.sleep(3) #aqui você da um tempo de pesquisa, nesse caso eu dei 1s
    bot.write(entradaSite.get()) #aqui você passará o endereço desejado, no nosso caso é do whats.
    bot.sleep(3)
    bot.press('enter')
    bot.sleep(5)
    bot.press('tab')
    bot.press('tab')
    bot.press('tab')
    bot.press('tab')
    bot.press('tab')
    bot.sleep(3)
    bot.write(entradaNomeGrupo.get())
    bot.press('enter')
    bot.sleep(3)
    bot.write(entradaMenssagem.get())
    bot.sleep(3)
    bot.press('enter')

def pegarposi():
    bot.mouseInfo()

comecar = customtkinter.CTkButton(tela,text='Começar', width=300 ,command=whats, fg_color='#075E54',hover_color='#25D366')
comecar.place(x=100, y=360)

botaoPegaPosi = customtkinter.CTkButton(tela,text='Pegar Posição Da Tela', width=300 ,command=pegarposi, fg_color='#075E54',hover_color='#25D366')
botaoPegaPosi.place(x=100, y=400)




tela.mainloop()
