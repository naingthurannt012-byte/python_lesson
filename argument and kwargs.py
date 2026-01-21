def greet(name,age):
    print(f'Hello,my name is {name} and I am {age} years old.')
greet(name='Naing Thura',age=30)

def greet(name,age=30):
    print(f'Hello,my name is {name} and I am {age} years old.')
greet(name='Naing Thura')
greet(name='Aung Aung',age=25)


def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
result = add_numbers(1,2,3,4,5)
print('The sum is:',result)

def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
display_info(name='Naing Thura',age=30,city='Yangon')

def example_function(a,b=2,*args,x=10,y=20,**kwargs):
    print(f'a:{a}','b:{b}')
    print(f'args:{args}')
    print(f'kwargs:{kwargs}')
    print(f'x:{x}','y:{y}')
example_function(1,3,4,5,6,x=15,z=30,city='Yangon')