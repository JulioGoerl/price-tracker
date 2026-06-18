import sqlite3


def criar_banco():
    conn = sqlite3.connect("precos.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS historico (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        titulo TEXT,
        preco REAL
    )
    """)

    conn.commit()
    conn.close()


def salvar_produto(data, titulo, preco):
    conn = sqlite3.connect("precos.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO historico(data, titulo, preco)
    VALUES (?, ?, ?)
    """, (data, titulo, preco))

    conn.commit()
    conn.close()


def ultimo_preco(titulo):
    conn = sqlite3.connect("precos.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT preco
    FROM historico
    WHERE titulo = ?
    ORDER BY id DESC
    LIMIT 1
    """, (titulo,))

    resultado = cursor.fetchone()

    conn.close()

    if resultado is None:
        return None

    return resultado[0]


def listar_historico():
    conn = sqlite3.connect("precos.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT data, titulo, preco
    FROM historico
    ORDER BY id DESC
    """)

    dados = cursor.fetchall()

    conn.close()

    return dados