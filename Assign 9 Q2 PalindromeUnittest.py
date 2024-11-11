import unittest

def is_palindrome(s):
    # Normalize the string by converting it to lowercase and removing spaces
    s = s.lower().replace(" ", "")
    return s == s[::-1]  # Check if string equals its reverse

class TestIsPalindrome(unittest.TestCase):

    def test_palindrome_word(self):
        # Test case for a simple palindrome word
        self.assertTrue(is_palindrome("madam"))

    def test_non_palindrome_word(self):
        # Test case for a non-palindrome word
        self.assertFalse(is_palindrome("hello"))

 

    def test_mixed_case_palindrome(self):
        # Test case for a mixed case palindrome
        self.assertTrue(is_palindrome("RaceCar"))


if __name__ == "__main__":
    unittest.main()
