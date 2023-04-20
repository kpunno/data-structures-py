import unittest
from minheap_NOswaps import MinHeap


class MinHeapTestCase(unittest.TestCase):
    # These are the test cases for functions of MinHeap class

    def test_init(self):
        the_heap = MinHeap()
        self.assertEqual(the_heap.get_min(), None)
        self.assertEqual(the_heap.extract_min(), None)

        the_heap = MinHeap([1, 2, 3, 4, 5])
        self.assertEqual(len(the_heap), 5)
        self.assertEqual(the_heap.get_min(), 1)
        self.assertEqual(len(the_heap), 5)
        self.assertEqual(the_heap.extract_min(), 1)
        self.assertEqual(len(the_heap), 4)
        self.assertEqual(the_heap.get_min(), 2)
        self.assertEqual(the_heap.extract_min(), 2)
        self.assertEqual(the_heap.get_min(), 3)
        self.assertEqual(the_heap.extract_min(), 3)
        self.assertEqual(the_heap.get_min(), 4)
        self.assertEqual(the_heap.extract_min(), 4)
        self.assertEqual(the_heap.get_min(), 5)
        self.assertEqual(the_heap.extract_min(), 5)
        self.assertEqual(len(the_heap), 0)
        self.assertEqual(the_heap.get_min(), None)
        self.assertEqual(the_heap.extract_min(), None)

if __name__ == '__main__':
    unittest.main()