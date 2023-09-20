import requests
import os
import sys

def download_and_save(url, save_directory):
    try:
        # Отправка запроса по данному URL
        response = requests.get(url)

        # Проверка успешности запроса
        response.raise_for_status()

        # Имя файла - последняя часть URL
        file_name = url.split("/")[-1]

        # Создание пути к файлу в указанной директории
        file_path = os.path.join(save_directory, file_name)

        # Открыть файл для записи и записать туда данные
        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"Содержимое URL '{url}' успешно сохранено в '{file_path}'")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных из URL: {e}")

def start_dowloading():
    # Задайте URL и директорию здесь
    url = "https://i.pinimg.com/564x/db/22/b0/db22b02f2f9d740d35fad1e922e9f748.jpg"
    save_directory = "C:/projects/vpo/l1t6"

    download_and_save(url, save_directory)

if __name__ == "__main__":
    start_dowloading()

