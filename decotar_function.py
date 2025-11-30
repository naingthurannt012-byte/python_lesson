def my_decorator(func):
    def wrapper(*args,**kwargs):
        print('Somthing is happening before the function is called.')
        result = func(*args, **kwargs)
        print('Somethin is happening after the function is called.')
        return result
    return wrapper

@my_decorator
def say_hello(name):
    return f'hello,{name}!'    

print(say_hello('Naing Thura'))

