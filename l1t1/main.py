import random


def calculate():
    return '!' * random.randint(5, 50)

def printing():
    return "Hello, world!\nAndhiagain!\n" + calculate()

if __name__ == "__main__":
    print(printing())
