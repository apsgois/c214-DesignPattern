import unittest
from q1 import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort, SortContext


class Testes_Q1(unittest.TestCase):
    print("*******Inicio dos testes******* \n")


    def test_01_bubble_sort(self):
        base = [7, 2, 5, 1, 8, 3]
        result = SortContext(bubble_sort)
        result.sort(base)
        self.assertEqual(base, [1, 2, 3, 5, 7, 8])
        print("Teste 01 - Bubble Sort OK \n")


    def test_02_insertion_sort(self):
        base = [7, 2, 5, 1, 8, 3]
        result = SortContext(insertion_sort)
        result.sort(base)
        self.assertEqual(base, [1, 2, 3, 5, 7, 8])
        print("Teste 02 - Insertion Sort OK \n ")


    def test_03_selection_sort(self):
        base = [7, 2, 5, 1, 8, 3]
        result = SortContext(selection_sort)
        result.sort(base)
        self.assertEqual(base, [1, 2, 3, 5, 7, 8])
        print("Teste 03 - Selection Sort OK \n")


    def test_04_merge_sort(self):
        base = [7, 2, 5, 1, 8, 3]
        result = SortContext(merge_sort)
        result.sort(base)
        self.assertEqual(base, [1, 2, 3, 5, 7, 8])
        print("Teste 04 - Merge Sort OK")


if __name__ == '__main__':
    unittest.main()
