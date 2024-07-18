def fibonacci_series(limit):
    fib_series = []
    a, b = 0, 1
    while a <= limit:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

limit = 50
fib_series = fibonacci_series(limit)
print(f"Fibonacci series between 0 and {limit}: {fib_series}")


for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz",end = " ")
    elif i % 3 == 0:
        print("Fizz",end = " ")
    elif i % 5 == 0:
        print("Buzz",end = " ")
    else:
        print(i,end = " ")