from typing import Dict


def read_txt(path='data.txt'):
    dados = dict()
    arq1 = open(path, 'r')
    for linha in arq1.read().splitlines():
        moeda, valor = linha.split(';')
        valor = float(valor)
        dados[f'{moeda}'] = valor
    arq1.close()
    return dados

def add_value_txt(moeda, valor, path='data.txt'):
    arq_read = read_txt()
    if moeda in arq_read: # Retorna True quando a moeda esta no arquivo  
        for i in arq_read:
            if moeda == i:
                valor_lido = arq_read[moeda]
                valor_novo = valor + valor_lido
                arq_read[moeda] = valor_novo

        arq1= open(path, 'w')
        for j in arq_read:
            arq1.write(f'{j};{arq_read[j]}\n')
        arq1.close()
    else: # Caso nao esteja ele adiciona a moeda no arquivo
        arq1= open(path, 'a')
        arq1.write(f'{moeda};{valor}\n')
        arq1.close()


try:
    read_txt()
except:
    arq_default = open('data.txt','w')
    arq_default.write(f'BTC;0\n')
    arq_default.write('ETH;0')
    arq_default.close()
# dados = read_txt()
# # for i in dados:
# #     print(f'{i};{dados[i]}')
# # add_value_txt('BTC', 2)
# # add_value_txt('ETH', 1)
# # # add_value_txt('ETH', 0.15)
# # print('Valores atualizados')
# # dados = read_txt()
# for i in dados:
#     print(f'{i};{dados[i]}') ### BTC;30.0 ---COIN;VALOR
#     print(type(dados[i]))



    
