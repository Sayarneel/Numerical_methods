def f(x):
    return x**2-10
def g(x):
    return 2*x
x=0.0000001
for i in range(100):
    x1=x-f(x)/g(x)
    x=x1
print(x)
