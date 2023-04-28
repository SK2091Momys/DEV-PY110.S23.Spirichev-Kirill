def task() -> str:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return str(min(list_words, key=len))


if __name__ == "__main__":
    print(task())
