import requests


class Extract:

    def buscar_universidades(self, pais: str) -> list:

        url = f"http://universities.hipolabs.com/search?country={pais}"
        resposta = requests.get(url)
        resposta.raise_for_status()
        return resposta.json()
