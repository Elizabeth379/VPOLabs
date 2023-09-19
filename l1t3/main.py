import sys


def params_input():
    while True:
        try:

            length = float(input("Введите длину"))
            width = float(input("Введите ширину"))

            if length <= 0 or width <= 0:
                raise ValueError("Вы ввели не положительное число")

            break

        except ValueError:
            print("Вы ввели не положительное число")

    return length, width



def calculate_rectangle_area(params):
        area = params[0] * params[1]
        return area


def result_print():
    print(calculate_rectangle_area(params_input()))



if __name__ == "__main__":
    result_print()