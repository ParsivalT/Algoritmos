import unittest
from python.insertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        # Teste para verificar se a lista está ordenada corretamente
        lista = [5, 2, 4, 7, 1, 3, 6]
        insertion_sort(lista)
        self.assertEqual(lista, [1, 2, 3, 4, 5, 6, 7])  # Verifica se a lista está ordenada corretamente

    def test_insertion_sort_empty(self):
        # Teste para lista vazia
        lista = []
        insertion_sort(lista)
        self.assertEqual(lista, [])  # Verifica se a lista vazia permanece vazia

    def test_insertion_sort_single_element(self):
        # Teste para lista com um elemento
        lista = [42]
        insertion_sort(lista)
        self.assertEqual(lista, [42])  # Verifica se a lista com um elemento permanece igual

if __name__ == '__main__':
    unittest.main()
