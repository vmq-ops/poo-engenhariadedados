from src import Extract, Load


def executar_pipeline():
    pais_alvo = "Brazil"
    nome_tabela = "universidades_brasil"

    print(f"Buscando dados para: {pais_alvo}...")
    extrator = Extract()
    dados = extrator.buscar_universidades(pais_alvo)

    print("Salvando no banco de dados")
    carregador = Load()
    carregador.salvar_no_banco(dados, nome_tabela)


if __name__ == "__main__":
    executar_pipeline()