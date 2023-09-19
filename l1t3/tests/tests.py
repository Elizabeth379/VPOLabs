import unittest
from unittest.mock import patch, Mock
import sys
import io
from main import params_input, calculate_rectangle_area, result_print


class TestParamsInput(unittest.TestCase):
    @patch('builtins.input', side_effect=['10', '5'])
    def test_valid_input(self, mock_input):
        # Проверяем, что функция возвращает корректные значения
        length, width = params_input()
        self.assertEqual(length, 10)
        self.assertEqual(width, 5)

    @patch('builtins.input', side_effect=['0', '0', '10', '5'])
    def test_zirrow_input(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            # Запускаем функцию params_input()
            length, width = params_input()
            expected_output = "Вы ввели не положительное число\n"

        # Проверяем, что значения были скорректированы на правильные
        self.assertEqual(length, 10)
        self.assertEqual(width, 5)

        # Проверяем, что выводится сообщение об ошибке
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['-1', '5', '10', 'abc', '5', '7'])
    def test_invalid_input(self, mock_input):
        # Подготавливаем вывод для имитации ввода

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            # Запускаем функцию params_input()
            length, width = params_input()
            expected_output = "Вы ввели не положительное число\nВы ввели не положительное число\n"


        # Проверяем, что значения были скорректированы на правильные
        self.assertEqual(length, 5)
        self.assertEqual(width, 7)

        # Проверяем, что выводится сообщение об ошибке
        self.assertEqual(mock_stdout.getvalue(), expected_output)


class TestCalculateRectangleArea(unittest.TestCase):
    def test_valid_params(self):
        # Проверяем, что функция корректно вычисляет площадь для правильных параметров
        params = (10, 5)
        result = calculate_rectangle_area(params)
        self.assertEqual(result, 50.0)


class TestResultPrint(unittest.TestCase):
    @patch('builtins.input', side_effect=['10', '5'])
    def test_print_result_output(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            result = result_print()
            expected_output = "50.0\n"

        # Проверяем, что результат соответствует ожидаемому выводу
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['0', '0', '10', '5'])
    def test_print_result_zirrow(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            result = result_print()
            expected_output = "Вы ввели не положительное число\n50.0\n"

        # Проверяем, что результат соответствует ожидаемому выводу
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['-1', '-1', '10', '5'])
    def test_print_result_invalid(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            result = result_print()
            expected_output = "Вы ввели не положительное число\n50.0\n"

        # Проверяем, что результат соответствует ожидаемому выводу
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
