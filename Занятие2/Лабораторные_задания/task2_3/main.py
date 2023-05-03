def pow_gen(base: int):
    n = 0
    while True: # TODO записать функцию-генератор
        num = base ** n
        n += 1
        yield num


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
