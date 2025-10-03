import unittest

from exerciciosbasicospython import *
class TesteCompleto(unittest.TestCase):
    def testar_se_numero_eh_par(self):
        numero_a_ser_testado = 18
        self.assertTrue(numero_a_ser_testado % 2 == 0)

    def testar_se_numero_eh_impar(self):
        numero_a_ser_testado = 17
        self.assertTrue(numero_a_ser_testado % 2 == 1)

    def testar_conta(self):
        resultado_conta = 15 + 5 + 25 + 7
        self.assertEqual(resultado_conta, 52)

    def testar_classificar_por_idade(self):
        self.assertEqual(classificar_por_idade(10), 'Criança')
        self.assertEqual(classificar_por_idade(15), 'Adolescente')
        self.assertEqual(classificar_por_idade(25), 'Adulto')
        self.assertEqual(classificar_por_idade(-5), 'Idade Inválida')
        self.assertEqual(classificar_por_idade(150), 'Idade Inválida')

if __name__ == "__main__":
    unittest.main()
