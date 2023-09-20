import unittest
import os
import sys
import io
from unittest.mock import patch
from bs4 import BeautifulSoup
from main import generate_html_table, table_creation


class TestGenerateHtmlTable(unittest.TestCase):
    def setUp(self):
        self.output_file = "test_table.html"

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_generate_html_table(self):
        # Проверяем, что функция генерирует HTML-файл с корректной структурой
        num_rows = 5  # Количество строк в таблице
        generate_html_table(num_rows, self.output_file)

        self.assertTrue(os.path.exists(self.output_file))  # Проверяем, что файл был создан

        # Анализируем HTML-код
        with open(self.output_file, 'r') as file:
            html_content = file.read()
            soup = BeautifulSoup(html_content, 'html.parser')

            # Проверяем наличие начала и конца таблицы
            self.assertIsNotNone(soup.find("table"))
            self.assertIsNotNone(soup.find("table"))

            # Проверяем количество строк
            rows = soup.find_all("tr")
            self.assertEqual(len(rows), num_rows)

            # Проверяем корректность фона строк
            for i, row in enumerate(rows):
                brightness = i / num_rows
                color = int(255 - 255 * brightness)
                background_color = f"rgb({color}, {color}, {color})"
                self.assertEqual(row["style"], f"background-color: {background_color};")


class TestTableCreation(unittest.TestCase):
    def setUp(self):
        self.output_file = "table.html"

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_table_creation(self):
        # Проверяем, что функция создает HTML-файл
        table_creation()
        self.assertTrue(os.path.exists(self.output_file))  # Проверяем, что файл был создан

        # Проверяем, что файл содержит ожидаемую таблицу
        with open(self.output_file, 'r') as file:
            html_content = file.read()
            # Проверяем наличие начала и конца таблицы в HTML-коде
            self.assertIn("<table", html_content)
            self.assertIn("</table>", html_content)

    def test_table_creation_output(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            result = table_creation()
            expected_output = "HTML-файл с таблицей создан: table.html\n"

        # Проверяем, что результат соответствует ожидаемому выводу
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
