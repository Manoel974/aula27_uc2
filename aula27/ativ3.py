import polars as pl
from datetime import datetime




ENDERECO_DADOS = r'./dados/'



try:


 hora_inicio = datetime.now()

 df_dados = pl.read_csv(ENDERECO_DADOS + 'dados_teste.csv', separator=',', encoding='utf-8')

 df_dados_lazy = df_dados.lazy()


 df_dados_lazy = (
       df_dados_lazy
        .group_by('regiao')
        .agg([
         pl.col('forma_pagamento').value_counts().first().alias('metodo_pagamento_mais_usado'),
         ((pl.col('quantidade') * pl.col('preco')).mean()).alias('valor_medio_vendas')
        ])
    )  

 df_bf = df_dados_lazy.collect()

    
 print(df_bf)

except ImportError as e:
 print(f'Erro ao obter dados: {e}')