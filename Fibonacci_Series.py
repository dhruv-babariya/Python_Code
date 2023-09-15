"""# FS = (n-1) + (n-2)
n = 10
num1 = 0
num2 = 1

def f(n1, n2):
    f= (n1-1) + (n2-2)
    return f

a = f(10, 15)
print(a)"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

# Change 'n' to the number of Fibonacci numbers you want to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci(n)
    print("Fibonacci series:")
    print(result)
