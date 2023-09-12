# Write a program which will return factorial number

num = int(input('Enter a number: '))
f = 1

for i in range(1, num + 1):
    f = f * i

print('The factorial of ', num, 'is', f)
