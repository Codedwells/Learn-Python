# Fibonacci in python


def fibonacci(n):
    fib_arr = [0, 1]
    i = 2
    while i < n:
        fib_arr.append(fib_arr[i - 1] + fib_arr[i - 2])
        i = i + 1
    print(f"{fib_arr}")


fibonacci(7)
