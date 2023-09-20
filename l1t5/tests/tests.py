import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import os
import glob
from main import search_files_with_extension, searching_time

class TestFindFilesWithExtension(unittest.TestCase):
    def test_search_files_with_extension(self):
        # Устанавливаем ожидаемый путь к текущей директории
        expected_current_dir = "C:/projects/vpo/l1t5"

        # Устанавливаем ожидаемое расширение файла
        expected_extension = "html"

        # Устанавливаем ожидаемый паттерн для поиска файлов
        expected_search_pattern = os.path.join(expected_current_dir, f"**/*.{expected_extension}")

        # Устанавливаем ожидаемый список файлов, которые должны быть найдены
        expected_files = ["C:/projects/vpo/l1t5/fortest.html", "C:/projects/vpo/l1t5/subfolder/fortest2.html"]

        # Имитируем glob.glob и возвращаем ожидаемый список файлов
        with patch('glob.glob', return_value=expected_files) as mock_glob:
            found_files = search_files_with_extension(expected_extension)

            # Проверяем, что функция glob.glob была вызвана с ожидаемым паттерном
            mock_glob.assert_called_once_with(expected_search_pattern, recursive=True)

            # Проверяем, что список найденных файлов совпадает с ожидаемым списком
            self.assertEqual(found_files, expected_files)


class TestSearchingTime(unittest.TestCase):
    @patch('builtins.print')
    @patch('main.search_files_with_extension', return_value=["file1.py", "file2.py"])
    def test_searching_time_with_files_found(self, mock_search_files, mock_print):
        # Вызываем функцию searching_time()
        searching_time()

        # Проверяем, что функция search_files_with_extension была вызвана
        mock_search_files.assert_called_once_with("py")

        # Проверяем, что было выведено сообщение о найденных файлах
        mock_print.assert_any_call("List of found files:\n")
        mock_print.assert_any_call("file1.py")
        mock_print.assert_any_call("file2.py")

    @patch('builtins.print')
    @patch('main.search_files_with_extension', return_value=[])
    def test_searching_time_with_files_not_found(self, mock_search_files, mock_print):
        # Вызываем функцию searching_time()
        searching_time()

        # Проверяем, что функция search_files_with_extension была вызвана
        mock_search_files.assert_called_once_with("py")

        # Проверяем, что было выведено сообщение о том, что файлы не найдены
        mock_print.assert_called_once_with("Files with extension .py not found.")



if __name__ == '__main__':
    unittest.main()
