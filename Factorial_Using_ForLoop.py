# Write a program which find a factorial number provided by user
# (Means, if user enter 4 then it will work like 4 * 3 * 2 * 1 = 24)

num = int(input("Enter a number: "))

factorial = 1
for i in range(1, num+1):
    factorial = factorial * i

print(f"The factorial of {num} is {factorial}....")
