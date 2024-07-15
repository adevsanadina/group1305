def result_as_dict(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return {'result': result}
    return wrapper


#examples

@result_as_dict
def add(a, b):
    return a + b


@result_as_dict
def greet(name):
    return f"Hello, {name}!"


print(add(6, 75))
print(greet("Ashlye"))

