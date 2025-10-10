import unittest

from exerciciosbasicospython import *

class TesteCompleto(unittest.TestCase):
    #def testar_se_numero_eh_par(self):
     #   numero_a_ser_testado = 14
     #   self.assertTrue(numero_a_ser_testado % 2 == 0)

   # def testar_se_numero_eh_impar(self):
       # numero_a_ser_testado = 11
       # self.assertTrue(numero_a_ser_testado % 2 == 1)

    #def testar_conta(self):
       # resultado_conta = 10 + 5 
       # self.assertEqual(resultado_conta, 15)

    #def testar_classificar_faixa_etaria(self):
        #self.assertEqual(classificar_faixa_etaria(10), 'Criança')
        #self.assertEqual(classificar_faixa_etaria(15), 'Adolescente')
        #self.assertEqual(classificar_faixa_etaria(25), 'Adulto')
        #self.assertEqual(classificar_faixa_etaria(-5), 'Idade inválida')
        #self.assertEqual(classificar_faixa_etaria(150), 'Idade inválida')

  #def testar_comparar_dois_numeros(self):
        #self.assertEqual(comparar_dois_numeros(10, 5), '10 é maior que 5')
        #self.assertEqual(comparar_dois_numeros(5, 10), '5 é menor que 10')
        #self.assertEqual(comparar_dois_numeros(7, 7), '7 é igual a 7')

    #def testar_verificar_vogal_ou_consoante(self):
        #self.assertEqual(verificar_vogal_ou_consoante('a'), 'A letra digitada é uma vogal.')
        #self.assertEqual(verificar_vogal_ou_consoante('b'), 'A letra digitada é uma consoante.')
        #self.assertEqual(verificar_vogal_ou_consoante('E'), 'A letra digitada é uma vogal.')
        #self.assertEqual(verificar_vogal_ou_consoante('Z'), 'A letra digitada é uma consoante.')

  #def test_comparacao_de_senhas(self):
        #self.assertEqual(comparacao_de_senhas('senha123', 'senha123'), 'Acesso permitido!')
        #self.assertEqual(comparacao_de_senhas('senha123', 'senha456'), 'Acesso negado!')

    #def teste_calcular_media(self):
        #self.assertEqual(calcular_media(8, 7, 9), 'O aluno está aprovado com média: 8.0!')
        #self.assertEqual(calcular_media(5, 6, 4), 'O aluno está reprovado com média: 5.0!')
        #self.assertEqual(calcular_media(10, 10, 10), 'O aluno está aprovado com média: 10.0!')
        #self.assertEqual(calcular_media(0, 0, 0), 'O aluno está reprovado com média: 0.0!')
        #self.assertEqual(calcular_media(11, 5, 6), 'Média inválida!')

    #def testar_ordenar_numeros_decrescente(self):
        #self.assertEqual(ordenar_numeros_decrescente(5, 2, 8), [8, 5, 2])
       # self.assertEqual(ordenar_numeros_decrescente(1, 1, 1), [1, 1, 1])
       # self.assertEqual(ordenar_numeros_decrescente(-1, -5, -3), [-1, -3, -5])
        #self.assertEqual(ordenar_numeros_decrescente(0, 10, 5), [10, 5, 0])

       def testar_calcular_litros_usados(self):
           self.assertAlmostEqual(calcular_litros_usados(2, 60), 10.0)  # 2 horas a 60 km/h = 120 km; 120/12 = 10 litros
           self.assertAlmostEqual(calcular_litros_usados(1.5, 80), 10.0)  # 1.5 horas a 80 km/h = 120 km; 120/12 = 10 litros
           self.assertAlmostEqual(calcular_litros_usados(3, 40), 10.0)   # 3 horas a 40 km/h = 120 km; 120/12 = 10 litros
if __name__ == "__main__":
    unittest.main()