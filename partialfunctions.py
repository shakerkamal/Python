from functools import partial

def multiply(a : int, b : int) -> int:              # static type checker mypy ----> pip install mypy
    return a * b;

double = partial(multiply, b = 2)

print(double(3))



from functools import partial


def multiply(a, b):
    return a*b


x = 2
f = partial(multiply, x)

result = f(10)  # 20
print(result)

x = 3
result = f(10)  # 20 supposed to be 30
print(result)  # the reason is: Python evaluates the value of x while declaring the partial function not after that





from typing import Union

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y