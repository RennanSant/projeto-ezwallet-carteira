from genericpath import exists
from tkinter import *
import requests
from urllib import response

from uteisArquivo import *


### Funcao API para requisitar valores das moedas
def get_coin_value(coin:str):
    coin = coin.lower()
    url = f'https://www.mercadobitcoin.net/api/{coin}/ticker'
    response = requests.get(url)    
    coin_current_value = response.json()
    coin_value_last = coin_current_value['ticker']['last']
    #print(f'{response}\n')
    value = float(coin_value_last)
    return f'{value:.2f}'


### valor moedas para real
def mycoin_to_real(mycoins, coin_value):
    mycoins=float(mycoins)
    coin_value=float(coin_value)
    value_real=mycoins*coin_value
    return f'{value_real}'

### Refresh do valor total da carteira
def Draw_total_wallet():
    global total_wallet_value
    
    frame_wallet = Frame(app, width=100, height=100, bd=1, background='#181c27')
    frame_wallet.place(x=80, y=60)
    total_wallet_value=Label(frame_wallet, background="#181c27" ,foreground="#fff", text='HELLO', font=('Calibri',40))
    total_wallet_value.pack()


def Refresher_total_wallet():
    global total_wallet_value
    valorteste = 0
    dados_txt = read_txt()
    for i in dados_txt:
        valorteste += float(mycoin_to_real(dados_txt[i], get_coin_value(f'{i}')) )
    total_wallet_value.configure(text=f'R$ {valorteste:.2f}')
    app.after(5000, Refresher_total_wallet) # cada 5 segundos...
    print('Refreshing total_wallet_value...')


### Form da moeda
def Draw_coin_wallet(coin_wallet_selected):
    global coin_frame_wallet
    global coinvsreal_frame

    dados_txt = read_txt()
    for i in dados_txt:
        if i == coin_wallet_selected:
            coin_wallet_value = dados_txt[i]
    
    try:
        coin_frame_wallet.destroy()
        coinvsreal_frame.destroy()
        ###
        ### coin = real frame
        coinvsreal_frame = Frame(app, width=395, height=245, bd=1, background='#181c27')
        coinvsreal_frame.place(x=405, y=0)

        value2 = f'''
         1 {coin_wallet_selected} 
           =
        R$ {float(get_coin_value(coin_wallet_selected)):.2f}
        '''
        valuecoinprint = Label(coinvsreal_frame, background="#181c27" ,foreground="#fff", text=value2, font=('Calibri',30))
        valuecoinprint.place(x=1, y=1)

        ### coin wallet frame
        coin_frame_wallet = Frame(app, width=395, height=480, bd=1, background='#181c27')
        coin_frame_wallet.place(x=405, y=245)
        
        coin_wallet_value_text = Label(coin_frame_wallet, text=f'Você possui {coin_wallet_value} {coin_wallet_selected}', background="#181c27", foreground="#fff", font=('Calibri',20))
        coin_wallet_value_text.place(x=10 , y=100)

        v_add_coin_value_text = Label(coin_frame_wallet, text=f'Adicionar {coin_wallet_selected}:', background="#181c27", foreground="#fff", font=('Calibri',20))
        v_add_coin_value_text.place(x = 50 , y = 210)
        v_add_coin_value = Entry(coin_frame_wallet) 
        v_add_coin_value.place(x = 50 , y = 250 , width=300, height=30)

        Button(coin_frame_wallet, text="Exportar", command= lambda: load_to_data(coin_wallet_selected, v_add_coin_value.get(), coin_frame_wallet)).place(x=290, y=300)

    except Exception as a:
        # print(a)
        ### coin = real frame
        coinvsreal_frame = Frame(app, width=395, height=245, bd=1, background='#181c27')
        coinvsreal_frame.place(x=405, y=0)

        value2 = f'''
         1 {coin_wallet_selected} 
           =
        R$ {float(get_coin_value(coin_wallet_selected)):.2f}
        '''
        valuecoinprint = Label(coinvsreal_frame, background="#181c27" ,foreground="#fff", text=value2, font=('Calibri',30))
        valuecoinprint.place(x=1, y=1)

        ### coin wallet frame
        coin_frame_wallet = Frame(app, width=395, height=480, bd=1, background='#181c27')
        coin_frame_wallet.place(x=405, y=245)
        
        coin_wallet_value_text = Label(coin_frame_wallet, text=f'Você possui {coin_wallet_value} {coin_wallet_selected}', background="#181c27", foreground="#fff", font=('Calibri',20))
        coin_wallet_value_text.place(x=10 , y=100)

        v_add_coin_value_text = Label(coin_frame_wallet, text=f'Adicionar {coin_wallet_selected}:', background="#181c27", foreground="#fff", font=('Calibri',20))
        v_add_coin_value_text.place(x = 50 , y = 210)
        v_add_coin_value = Entry(coin_frame_wallet) 
        v_add_coin_value.place(x = 50 , y = 250 , width=300, height=30)

        Button(coin_frame_wallet, text="Exportar", command= lambda: load_to_data(coin_wallet_selected, v_add_coin_value.get(), coin_frame_wallet)).place(x=290, y=300)


### Carregar para o arquivo data
def load_to_data(moeda, valor, frame):
    print('LOAD_TO_DATA: ADICIONANDO MOEDAS NA WALLET')
    valor = float(valor)
    try:
        add_value_txt(moeda, valor)
        Label(frame, text="Conteúdo gravado!", background="#181c27",foreground="#fff").place(x=290, y=335)
    except Exception as b:
        print(b)
        Label(frame, text="Ocorreu um erro!", background="#181c27",foreground="#fff").place(x=290, y=335)


### Divisórias
def app_divisor():
    frame = Frame(app, width=5, height=600, bd=1)
    frame.place(x=400, y=0)
    frame1 = Frame(app, width=405, height=5, bd=1)
    frame1.place(x=0, y=200)


### Botoes do menu lateral
def menu_lateral():
    global img  # Essa variaveis precisam ser globais, A interface Tk não lida adequadamente com referências a objetos de imagem; (bug pesquisado na internet)
    global img1
    
    #BTC
    img = PhotoImage(file='./img/bitcoin_logo1.png')
    label1 = Button(app, highlightthickness=0, borderwidth=0, image=img, command= lambda: (Draw_coin_wallet('BTC')))
    label1.place(x=10, y=250)
    #ETH
    img1 = PhotoImage(file='./img/ethereum_logo1.png')
    label2 = Button(app, highlightthickness=0, borderwidth=0, image=img1, command= lambda: (Draw_coin_wallet('ETH')))
    label2.place(x=10, y=400)

    txt_total=Label(app, text="Total", background="#181c27" ,foreground="#fff", font=('Calibri',20))
    txt_total.place(x=18, y=10)
    



# valores teste para data.txt    
# ETH;0.01106651
# BTC;0.00189701

print('running EZWALLET app...')
app=Tk()
app.title("EZWallet")
app.geometry("800x600")
app.configure(background="#181c27")
app.resizable(width=False, height=False)

app_divisor()
menu_lateral()

Draw_total_wallet()
Refresher_total_wallet()

app.mainloop()




