from datetime import datetime


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
