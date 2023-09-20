def generate_html_table(rows, output_file):
    # Открываем файл для записи HTML
    with open(output_file, 'w') as file:
        # Записываем начало HTML-файла и начало таблицы
        file.write("<html><head></head><body><table style='border-spacing: 0; width: 80vw; heigth: 10vw'>")

        # Генерируем строки таблицы с изменяющимся фоном
        for i in range(rows):
            # Вычисляем цвет фона в формате RGB
            brightness = i / rows  # Меняем яркость от 0 до 1
            color = int(255 - 255 * brightness)  # Вычисляем значение цвета от 255 до 0
            background_color = f"rgb({color}, {color}, {color})"

            # Записываем строку с ячейкой и фоном
            file.write(f"<tr style='background-color: {background_color};'><td>  </td></tr>")

        # Записываем конец таблицы и HTML-файла
        file.write("</table></body></html>")

def table_creation():
    num_rows = 500  # Количество строк в таблице
    output_filename = "table.html"  # Имя выходного HTML-файла

    # Генерируем HTML-файл с таблицей
    generate_html_table(num_rows, output_filename)

    print(f"HTML-файл с таблицей создан: {output_filename}")


if __name__ == "__main__":
    table_creation()
    