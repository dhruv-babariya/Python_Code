# Write a program to find whether a given number is Prime or not...

a = int(input("Write a number in order to check whether "
              "it is Prime number or not: "))

if(a%2) == 0:
    prime = False
else:
    prime = True

if(prime):
    print("the number is prime number")
else:
    print("the number is not a prime number")
