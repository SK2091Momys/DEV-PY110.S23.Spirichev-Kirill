def task(numbers: list):
    hex_numbers = map(hex, numbers)
    for num, hex_num in zip(numbers, hex_numbers):
        print(f"Число {num:2} -> {hex_num}")


if __name__ == "__main__":
    list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    task(list_numbers)
