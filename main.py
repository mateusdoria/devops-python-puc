from datetime import datetime


def calcular_idade():
    data_nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    try:
        data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
        hoje = datetime.today()
        idade = hoje.year - data_nascimento.year - (
                    (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
        print(f"Você tem {idade} anos.")
    except ValueError:
        print("Formato de data inválido. Use dd/mm/aaaa.")


calcular_idade()
