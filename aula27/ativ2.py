import polars as pl
from datetime import datetime




ENDERECO_DADOS = r'./dados/'



try:


 hora_inicio = datetime.now()

 df_dados = pl.read_csv(ENDERECO_DADOS + 'dados_teste.csv', separator=',', encoding='utf-8')

 df_dados_lazy = df_dados.lazy()


 df_dados_lazy = (
       df_dados_lazy
        .filter(pl.col('total_vendas') > 1500)
        .group_by('regiao' , 'forma_pagamento')
        .agg((pl.col('quantidade') * pl.col('preco')).sum().alias
        ('total de vendas'))
    )  

 df_bf = df_dados_lazy.collect()

    
 print(df_bf)

except ImportError as e:
 print(f'Erro ao obter dados: {e}')