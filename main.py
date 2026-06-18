from datetime import datetime
from scraper import obter_produto
from database import (
    criar_banco,
    salvar_produto,
    ultimo_preco,
    historico_produto,
    quantidade_registros
)

URLS = [
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "https://books.toscrape.com/catalogue/the-nicomachean-ethics_75/index.html",
    "https://books.toscrape.com/catalogue/the-little-prince_72/index.html"
]


def main():

    criar_banco()

    data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for url in URLS:
        titulo, preco = obter_produto(url)

        preco_anterior = ultimo_preco(titulo)

        quantidade = quantidade_registros(titulo)

        print(f"\nProduto: {titulo}")
        print(f"Preço atual: £{preco:.2f}")

        if preco_anterior is None:
            print("Primeira vez monitorando esse produto")

        elif preco < preco_anterior:
            print(f"Preço anterior: £{preco_anterior:.2f}")
            print("O preço caiu!")

        elif preco > preco_anterior:
            print(f"Preço anterior: £{preco_anterior:.2f}")
            print("O preço aumentou!")

        else:
            print(f"Preço anterior: £{preco_anterior:.2f}")
            print("️O preço não mudou.")


        salvar_produto(
            data_atual,
            titulo,
            preco
        )

        print(f"Monitorado {quantidade} vezes")

        historico = historico_produto(titulo)

        print("\nÚltimos preços:")

        for data, preco in historico:
            print(f"{data} -> £{preco:.2f}")


if __name__ == "__main__":
    main()