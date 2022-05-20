from unittest import TestCase
from main import reverso


class TestExerciciosFuncoes(TestCase):


    def test_numero_reverso(self):
        # Dado
        valor = [127, 123, 12141]
        resultado = []
        
        # Quando        
        for i in valor:
            resultado.append(reverso(i))

        # Entao
        valor_retorno = [721, 321, 14121]            
        self.assertEqual(resultado, valor_retorno)