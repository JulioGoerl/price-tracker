# Price Tracker

Um rastreador de preços desenvolvido em Python que monitora produtos de um site, armazena o histórico de preços em um banco SQLite e informa quando o preço aumentou, diminuiu ou permaneceu igual.

## Funcionalidades

- Monitoramento de múltiplos produtos
- Web Scraping com BeautifulSoup
- Armazenamento de histórico em SQLite
- Comparação com o último preço registrado
- Exibição do histórico de preços
- Estatísticas por produto

## Tecnologias Utilizadas

- Python 3
- Requests
- BeautifulSoup4
- SQLite

## Estrutura do Projeto

```
price-tracker/
│
├── main.py
├── scraper.py
├── database.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/price-tracker.git
cd price-tracker
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como Executar

```bash
python main.py
```

## Exemplo de Saída

```text
Produto: The Little Prince
Preço atual: £45.17
Preço anterior: £45.17
O preço não mudou.

Últimos preços:
2026-06-18 10:00:00 -> £45.17
2026-06-17 10:00:00 -> £45.17
```

## Conceitos Aplicados

- Funções
- Loops
- Listas
- Módulos
- Banco de Dados SQLite
- SQL (SELECT, INSERT, WHERE, ORDER BY, COUNT, AVG)
- Web Scraping
- Tratamento de dados

## Autor

Júlio Goerl