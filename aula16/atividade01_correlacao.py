import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# obter dados
try:
    print("Obtendo os dados...")

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # delimitando as variáveis
    df_lesao_corp = df_ocorrencias[['cisp', 'lesao_corp_dolosa', 'lesao_corp_morte']]
    
    # agrupar por cisp
    df_lesao_corp = df_lesao_corp.groupby('cisp', as_index=False)[['lesao_corp_dolosa', 'lesao_corp_morte']].sum()

    print(df_lesao_corp)
    print("\nDados obtidos com sucesso!")

except Exception as e:
    print(f'Erro ao obter os dados: {e}')


# Calculando correlação entre ocorrências de lesão corporal dolosa e lesões corporais seguidas de morte
    
try:
    print("\nCalculando a correlação entre ocorrências de lesão corporal dolosa e lesões corporais seguidas de morte...")

    # calcular correlação
    correlacao = np.corrcoef(df_lesao_corp['lesao_corp_dolosa'], df_lesao_corp['lesao_corp_morte'])[0, 1]

    print(f'Correlação: {correlacao}')

    # import matplotlib.pyplot as plt
    # criar um gráfico de dispersão
    plt.scatter(df_lesao_corp['lesao_corp_dolosa'], df_lesao_corp['lesao_corp_morte'])
    plt.title('Correlação entre ocorrências de lesão corporal dolosa e lesões corporais seguidas de morte')
    plt.xlabel('Lesão Corporal Dolosa')
    plt.ylabel('Lesão Corporal por morte')
    # mostrar correlaçao no gráfico
    plt.text(0.1, 0.9, f'Correlação: {correlacao:.2f}', transform=plt.gca().transAxes)
    # mostrar linha de tendencia no gráfico
    m, b = np.polyfit(df_lesao_corp['lesao_corp_dolosa'], df_lesao_corp['lesao_corp_morte'], 1)
    plt.plot(df_lesao_corp['lesao_corp_dolosa'], m*df_lesao_corp['lesao_corp_dolosa'] + b, color='red')
  
    
    plt.show()

   
except Exception as e:
    print(f'Erro ao calcular correlação: {e}')


    
    # relação linear forte, lesão corporal dolosa aumenta proporcional a lesão corporal por morte
    # Correlação positiva perfeita
    # cada bolinha do gráfico é uma cisp