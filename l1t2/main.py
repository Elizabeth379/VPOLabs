def last_name_input():
    return input("Введите фамилию: ")


def name_input():
    return input("Введите имя: ")


def age_input():
    while True:
        try:
            age = int(input("Введите возраст: "))
            break

        except ValueError:
            print("Вы ввели не целое число")

    return age


def make_person():
    return (last_name_input(), name_input(), age_input())


def make_list_of_people():
    result = []

    while True:
        command = input("Для остановки нажмите s, для продолжения - c")

        match command:
            case "s":
                return result

            case "c":
                person = make_person()
                result.append(person)


def ages_calculation(list_of_people):
    ages = [a[-1] for a in list_of_people]

    min_age = min(ages)
    max_age = max(ages)
    middle_age = sum(ages) / len(ages)

    return (min_age, max_age, middle_age)


def print_result():
    people_list = make_list_of_people()
    ages = ages_calculation(people_list)

    for person in people_list:
        print(f"{person[0]} {person[1]} {person[2]}")

    print(f"{ages[0]} {ages[1]} {ages[2]:.2f}")

    return


if __name__ == "__main__":
    print(print_result())
