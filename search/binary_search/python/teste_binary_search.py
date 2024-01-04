import unittest
from binary_search import binary_search

class TesteBinarySearch(unittest.TestCase):
    # Teste para verificar se o indice retornado esta correto.
    def test_search(self):
        data = [1, 2, 3, 5, 6, 8, 9, 11, 14, 16, 17]
        self.assertEqual(binary_search(data, 3), 2)

    # Tete para quando o valor procurado não esta na lista.
    def test_not_value(self):
        data = [5, 7, 8, 12, 15, 16]
        self.assertEqual(binary_search(data, 4), -1)

    # Teste para lista vazia.
    def test_empty_list_test(self):
        data = []
        self.assertEqual(binary_search(data, 5), -1)
        

class TesteBinarySearchRecursion(unittest.TestCase):
    # Teste para verificar se o indice retornado esta correto.
    def test_search(self):
        data = [1, 2, 3, 5, 6, 8, 9, 11, 14, 16, 17]
        self.assertEqual(binary_search(data, 3), 2)
        
    # Tete para quando o valor procurado não esta na lista.
    def test_not_value(self):
        data = [5, 7, 8, 12, 15, 16]
        self.assertEqual(binary_search(data, 4), -1)

    # Teste para lista vazia.
    def test_empty_list_test(self):
        data = []
        self.assertEqual(binary_search(data, 5), -1)

if __name__ == '__main__':
    unittest.main()