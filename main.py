import pandas as pd
tabela = pd.read_csv("cancelamentos.csv") # Lendo base de dados
display(tabela)

tabela = tabela.drop(columns="CustomerID") 
display(tabela)

display(tabela.info()) # Saber informações sobre cada coluna na tabela antes de excluir itens vazios
tabela = tabela.dropna() # Escluir valores vazios -> dropna (NaN)

display(tabela.info()) # Saber informações sobre cada coluna na tabela atualizada

display(tabela["cancelou"].value_counts(normalize=True)) # normalize=True é utilizado para ver em porcentagem (x/100)
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format)) # Exibir em porcentagem

import plotly.express as px

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    grafico.show()

### Possíveis soluções 
# Criar política na empresa para que os problemas de atraso de pagamento sejam resolvidos em até 10 dias <br>
# Todo o cliente que ligar para o callcenter 3 vezes terão seus problemas resolvidos <br>
# Oferecer descontos nos planos anuais e trimestrais para que o cliente compre eles ao invés do mensal

#Analisar novamente a porcentagem de cancelamentos da empresa

display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format)) 

#Realizar as mudanças 
tabela = tabela[tabela["dias_atraso"] < 20]
tabela = tabela[tabela["ligacoes_callcenter"] < 4]
tabela = tabela[tabela["duracao_contrato"] != "Monyhly"]

display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))