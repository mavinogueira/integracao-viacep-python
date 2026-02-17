import requests
import psycopg2
import json


#Configurações globais


CEP = "01001000"

DB_CONFIG = {
    "host": "localhost",
    "database": "enderecos",
    "user": "postgresql",
    "password": "5323ms",
    "port": 5432
}


#Função para consultar CEP via API

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()

            if "erro" in data:
                print("CEP não encontrado.")
                return None

            print("Resposta da API:")
            print(json.dumps(data, indent=4, ensure_ascii=False))

            return data
        else:
            print(f"Erro HTTP: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None


#Função para salvar no BD


def salvar_no_banco(dados):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO enderecos (
                cep, logradouro, complemento, bairro, localidade, uf
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (cep) DO NOTHING;
        """

        cursor.execute(insert_query, (
            dados.get("cep"),
            dados.get("logradouro"),
            dados.get("complemento"),
            dados.get("bairro"),
            dados.get("localidade"),
            dados.get("uf")
        ))

        conn.commit()
        print("Dados salvos com sucesso (ou já existentes).")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Erro ao salvar no banco: {e}")

#Função principal

def main():
    dados = consultar_cep(CEP)

    print("Dados retornados:", dados)

    if dados:
        print("Chamando função salvar_no_banco...")
        salvar_no_banco(dados)

# Ponto de entrada


if __name__ == "__main__":
    main()
