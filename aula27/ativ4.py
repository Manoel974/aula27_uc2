import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    # utf-8, iso-8859-1, latin1, cp1252
    df_dados = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    df_lesao_corp = df_dados[['cisp','lesao_corp_culposa' , 'lesao_corp_dolosa']]

    df_total = df_lesao_corp.groupby(['cisp']).sum(['lesao_corp_culposa' , 'lesao_corp_dolosa']).reset_index()

    print(df_total.head())

    print('Dados obtidos com sucesso!')

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()

try:
    print('Calculando a correlação...')

    correlacao = np.corrcoef(
        df_total['lesao_corp_culposa'], df_total['lesao_corp_dolosa'])[0, 1]
    
    print(f'Correlação {correlacao}')

    plt.scatter(df_total['lesao_corp_culposa'],
                df_total['lesao_corp_dolosa'])
    plt.title(f'Correlação: {correlacao}')
    plt.xlabel('Lesões corporais')
    plt.show()
                


except ImportError as e:
 print(f'Erro ao obter dados: {e}')
 exit()
    