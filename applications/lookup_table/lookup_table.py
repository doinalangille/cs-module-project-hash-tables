import math
import random


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

cache = {}
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    v = math.pow(x,y)
    # if there is already in cache
    if v in cache:
        v = cache[v]
    else:
        cache[v] = math.factorial(v)
        cache[v] //= (x+y)
        cache[v] %= 982451653
        v = cache[v]
    return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
