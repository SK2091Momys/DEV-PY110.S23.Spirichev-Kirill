def count(start_number: float = 1, step: float = 1):
    num = start_number # TODO написать функцию-генератор возвращающую целые числа
    yield num
    for _ in count(start_number, step):
        num += step
        yield num

if __name__ == "__main__":
    my_count = count(10, 0.5)
    for _ in range(10):
        print(next(my_count))
