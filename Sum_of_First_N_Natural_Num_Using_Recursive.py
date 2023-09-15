# Write a recursive function to calculate the sum of first N natural numbers...

n = int(input("enter n: "))

def sum_natural(n):
    if n==0 or n==1:
        return 1
    else:
        return n + sum_natural(n-1)

s = sum_natural(n)
print(s)
