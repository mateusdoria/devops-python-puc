import unittest
from datetime import datetime

from main import analisar_data_nascimento


class TestCalculoIdade(unittest.TestCase):

    def test_data_valida_maior_de_idade(self):
        data = "10/04/2000"
        resultado = analisar_data_nascimento(data)
        self.assertIn("idade", resultado)
        self.assertTrue(resultado["idade"] >= 18)
        self.assertTrue(resultado["maior_de_idade"])

    def test_data_valida_menor_de_idade(self):
        hoje = datetime.today()
        ano = hoje.year - 10
        data = f"01/01/{ano}"
        resultado = analisar_data_nascimento(data)
        self.assertTrue(resultado["idade"] < 18)
        self.assertFalse(resultado["maior_de_idade"])

    def test_data_invalida(self):
        resultado = analisar_data_nascimento("31-02-2020")
        self.assertEqual(resultado["erro"], "Formato de data inválido. Use dd/mm/aaaa.")

    def test_data_futura(self):
        futuro = datetime.today().replace(year=datetime.today().year + 1)
        data = futuro.strftime("%d/%m/%Y")
        resultado = analisar_data_nascimento(data)
        self.assertEqual(resultado["erro"], "Data de nascimento no futuro!")

    def test_dia_da_semana(self):
        resultado = analisar_data_nascimento("11/04/1995")
        self.assertEqual(resultado["dia_nasc_semana"], "terça-feira")  # verifique com um calendário se precisar

if __name__ == "__main__":
    unittest.main()
