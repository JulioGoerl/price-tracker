import requests
from bs4 import BeautifulSoup


def obter_produto(url):

    response = requests.get(url)
    response.encoding = "utf-8"

    if response.status_code != 200:
        raise Exception("Erro ao acessar a página")

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    titulo = soup.find("h1").text

    preco = soup.find(
        "p",
        class_="price_color"
    ).text

    preco = float(
        preco.replace("£", "")
    )

    return titulo, preco