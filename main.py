from datetime import datetime


def calcular_idade():
    data_nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    try:
        data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
        hoje = datetime.today()
        idade = hoje.year - data_nascimento.year - (
                    (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
        if data_nascimento > hoje:
            print("Data de nascimento no futuro! Verifique e tente novamente.")
            return

        proximo_aniversario = data_nascimento.replace(year=hoje.year)
        if proximo_aniversario < hoje:
            proximo_aniversario = proximo_aniversario.replace(year=hoje.year + 1)

        dias_faltando = (proximo_aniversario - hoje).days
        print(
            f"Seu próximo aniversário será em {proximo_aniversario.strftime('%d/%m/%Y')}, faltam {dias_faltando} dias.")

        dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado",
                       "domingo"]
        dia_nasc = dias_semana[data_nascimento.weekday()]
        print(f"Você nasceu em uma {dia_nasc}.")

        print(f"Você tem {idade} anos.")

        if idade >= 18:
            print("Você é maior de idade.")
        else:
            print("Você é menor de idade.")
    except ValueError:
        print("Formato de data inválido. Use dd/mm/aaaa.")


calcular_idade()
