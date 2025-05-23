from datetime import datetime, timedelta
from main import analisar_data_nascimento, gerar_conteudo_txt, salvar_no_s3_local
import unittest

class TestAnalisarDataNascimento(unittest.TestCase):

# Testes para analisar_data_nascimento
    def test_data_valida_maior_de_idade(self):
        data = "01/01/2000"
        resultado = analisar_data_nascimento(data)
        assert resultado["idade"] >= 18
        assert resultado["maior_de_idade"] is True

    def test_data_valida_menor_de_idade(self):
        hoje = datetime.today()
        data = f"{hoje.day:02d}/{hoje.month:02d}/{hoje.year - 10}"
        resultado = analisar_data_nascimento(data)
        assert resultado["idade"] < 18
        assert resultado["maior_de_idade"] is False

    def test_data_invalida(self):
        resultado = analisar_data_nascimento("31-02-2020")
        assert resultado["erro"] == "Formato de data inválido. Use dd/mm/aaaa."

    def test_data_futura(self):
        futuro = (datetime.today() + timedelta(days=1)).strftime("%d/%m/%Y")
        resultado = analisar_data_nascimento(futuro)
        assert resultado["erro"] == "Data de nascimento no futuro!"

    # Teste para gerar_conteudo_txt
    def test_gerar_conteudo_txt_valido(self):
        resultado = {
            "idade": 25,
            "maior_de_idade": True,
            "proximo_aniversario": "01/01/2026",
            "dias_faltando": 100,
            "dia_nasc_semana": "segunda-feira"
        }
        texto = gerar_conteudo_txt(resultado)
        assert "Você tem 25 anos." in texto
        assert "Você é maior de idade." in texto
        assert "Próximo aniversário" in texto

    def test_gerar_conteudo_txt_erro(self):
        resultado = {"erro": "Formato de data inválido. Use dd/mm/aaaa."}
        texto = gerar_conteudo_txt(resultado)
        assert "Erro: Formato de data inválido" in texto
