def task() -> list:
    num_list = [
        "12",
        "14",
        3.1415926,
        5,
        0xFF,  # шестнадцатеричное представление
        0b1010101010  # бинарное представление представление
    ]

    return list(map(int, num_list))


if __name__ == "__main__":
    print(task())
