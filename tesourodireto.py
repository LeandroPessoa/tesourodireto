#Para obter tabela de taxas e valores

import rows, requests
import pandas as pd

from io import BytesIO


#obtendo tabelas

url = 'http://www.tesouro.fazenda.gov.br/tesouro-direto-precos-e-taxas-dos-titulos'
response = requests.get(url)
html = response.content

titulos = pd.read_html(BytesIO(html),skiprows=2)

print(titulos)