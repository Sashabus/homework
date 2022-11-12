import time as t


def delay3_3(func):
    def wrapper(*args, **kwargs):
        t.sleep(3)
        func(*args, **kwargs)
        t.sleep(3)

    return wrapper


def repeat_3(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            func(*args, **kwargs)

    return wrapper


def protection(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except ValueError:
                print("numbers please")

    return wrapper


@repeat_3
@delay3_3
@protection
def suma():
    a = float(input())
    b = float(input())
    print(a + b)


suma()
