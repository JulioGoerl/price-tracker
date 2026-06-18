from datetime import datetime
from scraper import obter_produto
from database import (
    criar_banco,
    salvar_produto,
    ultimo_preco,
    listar_historico
)

URL = (
    "https://books.toscrape.com/"
    "catalogue/"
    "a-light-in-the-attic_1000/"
    "index.html"
)


def main():

    criar_banco()

    titulo, preco = obter_produto(URL)

    preco_anterior = ultimo_preco(titulo)

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
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        titulo,
        preco
    )


if __name__ == "__main__":
    main()

print("\nHistórico:")

for data, titulo, preco in listar_historico():
    print(f"{data} | {titulo} | £{preco:.2f}")