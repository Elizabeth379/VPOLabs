import unittest
from unittest.mock import patch
import sys
import io
from main import name_input, age_input, last_name_input, make_person, make_list_of_people, ages_calculation,print_result


class InputTypeTestCase(unittest.TestCase):
    @patch('builtins.input', side_effect=['Ivanov'])
    def test_last_name_input(self, mock_input):
        result = last_name_input()
        self.assertIsInstance(result, str)  # Проверяет, что вводимая фамилия на самом деле строка

    @patch('builtins.input', side_effect=['Ivan'])
    def test_name_input(self, mock_input):
        result = name_input()
        self.assertIsInstance(result, str)  # Проверяет, что вводимое имя на самом деле строка

    @patch('builtins.input', side_effect=['67'])
    def test_age_input(self, mock_input):
        result = age_input()
        self.assertIsInstance(result, int)  # Проверяет, что вводимый возраст на самом деле целое число

    @patch('builtins.input', side_effect=['Ivanov', 'Ivan', '47'])
    def test_make_person(self, mock_input):
        result = make_person()
        self.assertIsInstance(result, tuple)  # Проверяет, что информация о человеке является кортежем

    @patch('builtins.input', side_effect=['c', 'Ivanov', 'Ivan', '47', 'c', 'Sinicyn', 'Mark', '13', 's'])
    def test_make_list_of_people(self, mock_input):
        result = make_list_of_people()
        self.assertIsInstance(result, list)  # Проверяет, что список людей создается списком


class TestAgeInput(unittest.TestCase):
    @patch('builtins.input', side_effect=['25'])
    def test_valid_input(self, mock_input):
        self.assertEqual(age_input(), 25)     # Проверяем, что функция возвращает корректное целое число


    @patch('builtins.input', side_effect=['-5'])
    def test_negative_input(self, mock_input):
        # Проверяем, что функция корректно обрабатывает отрицательное число
        self.assertEqual(age_input(), -5)

    @patch('builtins.input', side_effect=['  42  '])
    def test_whitespace_input(self, mock_input):
        # Проверяем, что функция корректно обрабатывает ввод с пробельными символами
        self.assertEqual(age_input(), 42)


class TestMakeListOfPeople(unittest.TestCase):
    @patch('builtins.input', side_effect=['c', 's'])
    @patch('main.make_person', side_effect=[('Ivanov', 'Ivan', 25)])
    def test_make_list_with_commands(self, mock_input, mock_make_person):
        result = make_list_of_people()

        # Проверяем, что список содержит ожидаемый элемент
        self.assertEqual(result, [('Ivanov', 'Ivan', 25)])


    @patch('builtins.input', side_effect=['s'])
    def test_make_list_without_commands(self, mock_input):
        result = make_list_of_people()

        # Проверяем, что результат является пустым списком
        self.assertEqual(result, [])


class TestAgesCalculation(unittest.TestCase):
    def test_ages_calculation(self):
        # Создаем список людей с разными возрастами
        people_list = [('Ivanov', 'Ivan', 25), ('Petrov', 'Petr', 35), ('Sidorov', 'Sidor', 45)]

        # Вычисляем ожидаемые значения
        expected_min_age = 25
        expected_max_age = 45
        expected_middle_age = (25 + 35 + 45) / 3

        result = ages_calculation(people_list)

        # Проверяем, что результат соответствует ожидаемым значениям
        self.assertEqual(result, (expected_min_age, expected_max_age, expected_middle_age))


class TestPrintResult(unittest.TestCase):
    @patch('builtins.input', side_effect=['c', 'Ivanov', 'Ivan', '25', 's'])
    def test_print_result_output(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            result = print_result()
            expected_output = "Ivanov Ivan 25\n25 25 25.00\n"

        # Проверяем, что результат соответствует ожидаемому выводу
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
