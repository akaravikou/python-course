import time


def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def my_time(fn):
    def wrapper(*args):
        st = time.time()
        fn(*args)
        dt = time.time() - st
        print(f"Work time: {dt} sec.")

    return wrapper


test1 = my_time(get_nod)
test1(5, 4)
