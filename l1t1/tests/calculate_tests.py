import unittest
from main import calculate


class TestCase(unittest.TestCase):
    def test_number_of_signes(self):
        result = calculate()
        self.assertTrue(len(result) >= 5 and len(result) <= 50)  # Проверяет, что выдаваемые знаки находятся в кол-ве от 5 до 50

    def test_right_sign(self):
        result = calculate()
        self.assertEqual(result, "!" * len(result))  # Проверяет, что все выдаваемые знаки являются знаком "!"


if __name__ == '__main__':
    unittest.main()
