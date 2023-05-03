def header_footer(fn):  # TODO написать декоратор
    def wrapper():
        print("========")
        result = fn()
        print("========")
        return result

    return wrapper


@header_footer
def my_func():
    print("Hello World")


if __name__ == "__main__":
    my_func()
