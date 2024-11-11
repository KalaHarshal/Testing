import unittest

def ascending(lst):
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
        return True

class TestIsSortedAscending(unittest.TestCase):

    def test_sorted_list(self):
        # Test case for a list that is already sorted
        self.assertTrue(ascending([1, 2, 3, 4, 5]))

    def test_unsorted_list(self):
        # Test case for a list that is not sorted
        self.assertFalse(ascending([5, 3, 4, 1, 2]))


if __name__ == "__main__":
    unittest.main()
