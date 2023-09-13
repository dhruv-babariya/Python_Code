# Using with "def" write a program which find a greatest number


def maximum(num1, num2, num3):
    if(num1 > num2):
        if(num1 > num3):
            return (num1)
        else:
            return (num3)

    else:
        if(num2 > num3):
            return (num2)
        else:
            return (num3)

n = maximum(200, 30000, 40)
print(n)