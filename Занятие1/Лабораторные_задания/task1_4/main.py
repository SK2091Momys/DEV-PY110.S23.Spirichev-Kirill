def list_comprehension(words: list) -> list:
    return [str.capitalize(i) for i in words]


def list_map(words: list) -> list:
    return list(map(str.capitalize, words))


def task():
    list_words = [
        "goldenROD",
        "puRPle",
        "sAlMoN",
        "TURQUOISE",
        "cYAN"
    ]

    print(list_comprehension(list_words))
    print(list_map(list_words))


if __name__ == "__main__":
    task()
