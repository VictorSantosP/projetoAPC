def f(x):
    if x == 0 or x == 1:
        return 1
    return f(x-1)*x

def func(a):
    if a == 0:
        return 2
    return a + f(a-1)

print(func(6))