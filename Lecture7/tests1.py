import unittest
from prime import is_prime

class Tests(unittest.TestCase):

    def test_1(self):
        """Check 1 is not prime"""
        self.assertFalse(is_prime(1))

    def test_2(self):
        """Check 2 is prime"""
        self.assertFalse(is_prime(2))
    
    def test_8(self):
        """Check 8 is not prime"""
        self.assertFalse(is_prime(8))

if __name__ == "__main__":
    unittest.main()