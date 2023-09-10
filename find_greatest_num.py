#Write a program to find Greatest of 4 numbers entered by the user.

A = int(input('Enter the first number: '))
B = int(input('Enter the second number: '))
C = int(input('Enter the third number: '))
D = int(input('Enter the forth number: '))

if(A>B):
    f1 = A
else:
    f1 = B

if(C>D):
    f2 = C
else:
    f2 = D

if(f1>f2):
    print(f1, " is greatest")
else:
    print(f2, " is greatest")
