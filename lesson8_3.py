from functools import wraps


def val_checker(data):
    def wrapped_func(func):

        @wraps(func)
        def wrapper(a, b, c):
            for value in [a, b, c]:
                if data(value):
                    func(value)
                    print(wrapper.__name__)
                else:
                    raise ValueError("Нельзя вводить отрицательное число")
        return wrapper
    return wrapped_func


def type_logger(function):
    cache = {}

    @wraps(function)
    def logger(a, b, c):
        nonlocal cache
        for value in [a, b, c]:
            print(logger.__name__, f'({value}: {type(value)})', end=', ')
            if type(value) not in cache:
                cache[type(value)] = function(value)
        return cache

    return logger


@val_checker(lambda x: x > 0)
# @type_logger
def calc_cube(x):
    return print(x ** 3)


a = calc_cube(a=5, b=4, c=-3)
