from datetime import datetime
import boto3

def analisar_data_nascimento(data_nascimento_str: str) -> dict:
    try:
        hoje = datetime.today()
        data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

        if data_nascimento > hoje:
            return {"erro": "Data de nascimento no futuro!"}

        idade = hoje.year - data_nascimento.year - (
                (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day)
        )

        proximo_aniversario = data_nascimento.replace(year=hoje.year)
        if proximo_aniversario < hoje:
            proximo_aniversario = proximo_aniversario.replace(year=hoje.year + 1)

        dias_faltando = (proximo_aniversario - hoje).days
        dia_nasc = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira",
                    "sexta-feira", "sábado", "domingo"][data_nascimento.weekday()]

        return {
            "idade": idade,
            "proximo_aniversario": proximo_aniversario.strftime("%d/%m/%Y"),
            "dias_faltando": dias_faltando,
            "dia_nasc_semana": dia_nasc,
            "maior_de_idade": idade >= 18
        }

    except ValueError:
        return {"erro": "Formato de data inválido. Use dd/mm/aaaa."}


def gerar_conteudo_txt(resultado: dict) -> str:
    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"
    status = "maior de idade" if resultado["maior_de_idade"] else "menor de idade"
    return (
        f"Você tem {resultado['idade']} anos.\n"
        f"Você é {status}.\n"
        f"Próximo aniversário: {resultado['proximo_aniversario']} (faltam {resultado['dias_faltando']} dias)\n"
        f"Você nasceu em uma {resultado['dia_nasc_semana']}."
    )


def salvar_no_s3_local(conteudo: str, nome_arquivo: str):
    s3 = boto3.client(
        "s3",
        endpoint_url="http://localhost:4566",  # LocalStack
        aws_access_key_id="test",
        aws_secret_access_key="test",
        region_name="us-east-1"
    )
    bucket = "idade-bucket"

    # Cria o bucket se não existir
    try:
        s3.head_bucket(Bucket=bucket)
    except:
        s3.create_bucket(Bucket=bucket)

    s3.put_object(Bucket=bucket, Key=nome_arquivo, Body=conteudo.encode("utf-8"))
    print(f"Arquivo '{nome_arquivo}' enviado para o bucket '{bucket}' com sucesso.")


if __name__ == "__main__":
    entrada = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    resultado = analisar_data_nascimento(entrada)
    conteudo_txt = gerar_conteudo_txt(resultado)
    print(conteudo_txt)
    salvar_no_s3_local(conteudo_txt, "resultado_idade.txt")
