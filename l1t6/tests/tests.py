import unittest
from unittest.mock import patch, Mock
from io import StringIO
import requests
import os
import sys
from main import download_and_save, start_downloading

class TestDownloadAndSave(unittest.TestCase):
    @patch('builtins.print')
    @patch('requests.get')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_download_and_save_success(self, mock_open, mock_requests_get, mock_print):
        # Устанавливаем ожидаемые значения
        url = "https://test.com/document.pdf"
        save_directory = "/save/directory"
        file_name = "document.pdf"
        file_path = os.path.join(save_directory, file_name)
        expected_content = b"Mocked content"

        # Имитируем успешный запрос и запись в файл
        mock_requests_get.return_value.content = expected_content
        mock_requests_get.return_value.raise_for_status.side_effect = None
        mock_open.return_value.__enter__.return_value.write.side_effect = None

        # Вызываем функцию download_and_save
        download_and_save(url, save_directory)

        # Проверяем, что запрос был отправлен с указанным URL
        mock_requests_get.assert_called_once_with(url)

        # Проверяем, что файл был создан и записан в него ожидаемый контент
        mock_open.assert_called_once_with(file_path, 'wb')
        mock_open.return_value.__enter__.return_value.write.assert_called_once_with(expected_content)

        # Проверяем, что было выведено сообщение о успешном сохранении
        mock_print.assert_called_once_with(f"Содержимое URL '{url}' успешно сохранено в '{file_path}'")

    @patch('builtins.print')
    @patch('requests.get')
    def test_download_and_save_request_error(self, mock_requests_get, mock_print):
        # Устанавливаем ожидаемые значения
        url = "https://test.com/document.pdf"
        save_directory = "/save/directory"
        error_message = "Request error message"

        # Имитируем ошибку при запросе
        mock_requests_get.side_effect = requests.exceptions.RequestException(error_message)

        # Вызываем функцию download_and_save
        download_and_save(url, save_directory)

        # Проверяем, что запрос был отправлен с указанным URL
        mock_requests_get.assert_called_once_with(url)

        # Проверяем, что было выведено сообщение об ошибке запроса
        mock_print.assert_called_once_with(f"Ошибка при получении данных из URL: {error_message}")

    @patch('builtins.print')
    @patch('requests.get')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_download_and_save_output(self, mock_open, mock_requests_get, mock_print):
        # Устанавливаем ожидаемые значения
        url = "https://test.com/document.pdf"
        save_directory = "/save/directory"
        file_name = "document.pdf"
        file_path = os.path.join(save_directory, file_name)
        expected_content = b"Mocked content"

        # Имитируем успешный запрос и запись в файл
        mock_requests_get.return_value.content = expected_content
        mock_requests_get.return_value.raise_for_status.side_effect = None
        mock_open.return_value.__enter__.return_value.write.side_effect = None

        # Вызываем функцию download_and_save
        download_and_save(url, save_directory)

        # Проверяем, что было выведено сообщение о успешном сохранении
        mock_print.assert_called_once_with(f"Содержимое URL '{url}' успешно сохранено в '{file_path}'")


class TestStartDownloading(unittest.TestCase):
    @patch('main.download_and_save')
    def test_start_downloading(self, mock_download_and_save):
        # Устанавливаем ожидаемые значения
        url = "https://i.pinimg.com/564x/db/22/b0/db22b02f2f9d740d35fad1e922e9f748.jpg"
        save_directory = "C:/projects/vpo/l1t6"

        # Вызываем функцию start_downloading()
        start_downloading()

        # Проверяем, что функция download_and_save была вызвана с правильными аргументами
        mock_download_and_save.assert_called_once_with(url, save_directory)


if __name__ == '__main__':
    unittest.main()

