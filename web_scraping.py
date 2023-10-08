import requests
from bs4 import BeautifulSoup

# Defina a URL que você deseja raspar
url = "https://example.com"

# Faça uma solicitação GET para a URL
response = requests.get(url)

# Crie um objeto BeautifulSoup com a resposta da solicitação
soup = BeautifulSoup(response.content, "html.parser")

# Encontre os elementos HTML que contêm os dados que você deseja raspar
# Por exemplo, para raspar o título da página, você pode usar o seguinte código:
title = soup.find("title").text

# Imprima o título da página
print(title)
