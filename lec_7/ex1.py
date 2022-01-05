x=float(input())
def f(x):
    return x**2-10
    print (f(x))
def g(x):
    return 2*x
    print (g(x))

for i in range(100):
    x=x-f(x)/g(x)
print(x)

