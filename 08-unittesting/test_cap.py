import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = "python"
        result = cap.cap_text(text)
        print("Test case 1 ")
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = "multi python"
        print("Test case 2")
        result = cap.cap_text(text)
        self.assertEqual(result, 'Multi Python')


if __name__ == "__main__":
    print("Ran test cases script manually")
    unittest.main()