import unittest
from utils import palindromeChecker

class PalindromeTests(unittest.TestCase):

    def testSentencePalindrome(self):
        # Test Case 1: A sentence with punctuation, spaces, and capital letters
        # Expected result: True
        testString = "Anne, I vote more cars race Rome-to-Vienna."
        self.assertTrue(palindromeChecker(testString))

    def testNonPalindrome(self):
        # Test Case 2: A sentence that is not a palindrome
        # Expected result: False
        testString = "This is not a palindrome."
        self.assertFalse(palindromeChecker(testString))

    def testWordPalindrome(self):
        # Test Case 3: One word palindrome
        # Expected result: True
        testString = "racecar"
        self.assertTrue(palindromeChecker(testString))

    def testEmptyString(self):
        # Test Case 4: An empty string
        # Expected result: True
        testString = ""
        self.assertTrue(palindromeChecker(testString))


if __name__ == "__main__":
    unittest.main(verbosity=2)
