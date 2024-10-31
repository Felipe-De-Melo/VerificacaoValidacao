import unittest
from media import calcular_media

class TestCalcularMedia(unittest.TestCase):
    def test_media_basica(self):
        """Esse teste verifica se a média desses 3 números está correta"""
        self.assertEqual(calcular_media(7, 8, 9), 8)

    def test_media_todos_zero(self):
        """Faz a verificação se o usuário inserir todas a notas como zero o sistema retornará média igual a zero."""
        self.assertEqual(calcular_media(0, 0, 0), 0)

    def test_media_notas_maximas(self):
        """Utilizado para garantir se ao preencher a médias todas como 10 o algorítmo irá retornar uma média final igual a 10."""
        self.assertEqual(calcular_media(10, 10, 10), 10)

    def test_media_com_decimais(self):
        """Garante o funcionamento correto ao calcular as notas com números decimais"""
        self.assertAlmostEqual(calcular_media(7.5, 8.3, 9.2), 8.33, places=2)

if __name__ == '__main__':
    unittest.main()