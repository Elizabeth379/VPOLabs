import unittest
from main import printing

class TestCase(unittest.TestCase):
    def test_first_string(self):
        hello = printing()[0:14]
        self.assertEqual("Hello, world!\n", hello)  # Проверяет, выводится ли верно Hello world в консоль и есть ли
                                                    # переход на следующую строку

    def test_second_string(self):
        andhiagain = printing()[14:26]
        self.assertEqual("Andhiagain!\n", andhiagain)   # Проверяет, выводится ли верно Andhiagain в консоль и есть ли
                                                        # переход на следующую строку

if __name__ == '__main__':
    unittest.main()
