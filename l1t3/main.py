import sys


def calculate_rectangle_area(length, width):
    try:
        length = float(length)
        width = float(width)

        if length <= 0 or width <= 0:
            raise ValueError("Длина и ширина прямоугольника должны быть положительными числами.")

        area = length * width
        return area

    except ValueError as e:
        print(f"Ошибка: {e}")
        return None


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python calculate_rectangle_area.py <1> <2>")
    else:
        length = sys.argv[1]
        width = sys.argv[2]

        area = calculate_rectangle_area(length, width)

        if area is not None:
            print(f"Площадь прямоугольника с длиной {length} и шириной {width} равна {area}")
