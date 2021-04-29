class UnknownScaleError(Exception):
    pass


def result_to(scale):
    if scale == 'celcjusz':
        def convert(k): return k - 273.15
    elif scale == 'fahrenheit':
        def convert(k): return k*1.8 - 459.67
    else:
        raise UnknownScaleError

    def decorator(fn):
        def decorated(*args):
            return convert(fn(*args))
        return decorated
    return decorator


@result_to('celcjusz')
def get_temp():
    return 301

@result_to('fahrenheit')
def get_other_temp():
    return 295

print(get_temp())
print(get_other_temp())