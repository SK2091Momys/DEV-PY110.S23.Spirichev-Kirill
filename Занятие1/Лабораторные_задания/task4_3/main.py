from itertools import repeat


def task():
    a = 10
    for num in repeat(a, 4):
        print(num)


if __name__ == "__main__":
    task()
