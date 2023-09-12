# Write a program about calculation of use input number until 0 
# (means, if user input 4 then it will sum 4 + 3 + 2 + 1 = 10)

num = int(input("Enter a number: "))
sum = 0
for i in range(0, num+1):
    sum = sum + i

print(f"The sum of {num} until 0 is {sum}...")
