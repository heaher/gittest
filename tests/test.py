import unittest
import main

class TestSample(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(1, 2), 3)

if __name__ == "__main__":
    unittest.main()