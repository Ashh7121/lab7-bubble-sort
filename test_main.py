import unittest
from main import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_sorted_already(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random_order(self):
        self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])

    def test_with_duplicates(self):
        self.assertEqual(bubble_sort([3, 1, 2, 1, 3]), [1, 1, 2, 3, 3])

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_single_element(self):
        self.assertEqual(bubble_sort([42]), [42])


if __name__ == '__main__':
    unittest.main()
