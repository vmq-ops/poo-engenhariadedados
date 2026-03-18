import sqlite3


class Load:
    """Classe responsável por salvar os dados em um banco de dados SQLite."""

    def salvar_no_banco(self, lista_universidades: list, nome_tabela: str):
        """
        Cria o banco de dados e insere as informações extraídas.

        Parâmetros:
            lista_universidades (list): Dados retornados pela extração.
            nome_tabela (str): Nome da tabela onde os dados serão armazenados.
        """
        conexao = sqlite3.connect("universidades_mac.db")
        cursor = conexao.cursor()

        # Criando a tabela
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {nome_tabela} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                pais TEXT,
                estado TEXT,
                paginas_web TEXT
            )
        """
        )

        # Inserindo os dados
        for uni in lista_universidades:
            cursor.execute(
                f"""
                INSERT INTO {nome_tabela} (nome, pais, estado, paginas_web)
                VALUES (?, ?, ?, ?)
            """,
                (
                    uni.get("name"),
                    uni.get("country"),
                    uni.get("state-province"),
                    ", ".join(uni.get("web_pages", [])),
                ),
            )

        conexao.commit()
        conexao.close()
