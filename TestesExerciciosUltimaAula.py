import unittest

import ExerciciosUltimaAula

class TesteCompleto(unittest.TestCase):



    def test_primos_no_intervalo(self):
        self.assertEqual(ExerciciosUltimaAula.primos_no_intervalo(10, 20), [11, 13, 17, 19])
        self.assertEqual(ExerciciosUltimaAula.primos_no_intervalo(1, 10), [2, 3, 5, 7])
        self.assertEqual(ExerciciosUltimaAula.primos_no_intervalo(14, 16), [])
        self.assertEqual(ExerciciosUltimaAula.primos_no_intervalo(7, 7), [7])
        self.assertEqual(ExerciciosUltimaAula.primos_no_intervalo(-5, 1), [])

    def test_ordenar_sem_repeticao(self):
        self.assertEqual(ExerciciosUltimaAula.ordenar_sem_repeticao([3, 1, 2, 3, 1]), [1, 2, 3])
        self.assertEqual(ExerciciosUltimaAula.ordenar_sem_repeticao([5, 2, 8]), [2, 5, 8])
        self.assertEqual(ExerciciosUltimaAula.ordenar_sem_repeticao([]), [])
        self.assertEqual(ExerciciosUltimaAula.ordenar_sem_repeticao([42]), [42])
        self.assertEqual(ExerciciosUltimaAula.ordenar_sem_repeticao([3.1, 1, 2.5, 3.1]), [1, 2.5, 3.1])

    def test_soma_digitos(self):
        self.assertEqual(ExerciciosUltimaAula.soma_digitos(123), 6)
        self.assertEqual(ExerciciosUltimaAula.soma_digitos(-456), 15)
        self.assertEqual(ExerciciosUltimaAula.soma_digitos(0), 0)
        self.assertEqual(ExerciciosUltimaAula.soma_digitos(9999), 36)
        self.assertEqual(ExerciciosUltimaAula.soma_digitos(5), 5)

    def test_eh_palindromo(self):
        self.assertTrue(ExerciciosUltimaAula.eh_palindromo("radar"))
        self.assertTrue(ExerciciosUltimaAula.eh_palindromo("A man a plan a canal Panama"))
        self.assertFalse(ExerciciosUltimaAula.eh_palindromo("Olá"))
        self.assertTrue(ExerciciosUltimaAula.eh_palindromo(""))
        self.assertTrue(ExerciciosUltimaAula.eh_palindromo("A Santa at NASA"))
        self.assertFalse(ExerciciosUltimaAula.eh_palindromo("Hello, world!"))

    def test_frequencia_palavras(self):
        self.assertEqual(ExerciciosUltimaAula.frequencia_palavras("Olá mundo olá"), {'olá': 2, 'mundo': 1})
        self.assertEqual(ExerciciosUltimaAula.frequencia_palavras("Python é Python"), {'python': 2, 'é': 1})
        self.assertEqual(ExerciciosUltimaAula.frequencia_palavras(""), {})
        self.assertEqual(ExerciciosUltimaAula.frequencia_palavras("teste"), {'teste': 1})
        self.assertEqual(ExerciciosUltimaAula.frequencia_palavras("a a a b b"), {'a': 3, 'b': 2})

    def test_media_lista(self):
        self.assertEqual(ExerciciosUltimaAula.media_lista([1, 2, 3, 4]), 2.5)
        self.assertEqual(ExerciciosUltimaAula.media_lista([5]), 5.0)
        self.assertIsNone(ExerciciosUltimaAula.media_lista([]))
        self.assertEqual(ExerciciosUltimaAula.media_lista([-1, -2, 3]), 0.0)
        self.assertAlmostEqual(ExerciciosUltimaAula.media_lista([1.5, 2.5, 3.0]), 2.3333333333333335, places=5)

if __name__ == '__main__':
    unittest.main()