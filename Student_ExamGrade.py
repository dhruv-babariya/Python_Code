# Insert your marks and check that how many marks average you got with Grade...

def Average(Marks):
    return sum(Marks) / len(Marks)

Marks = [40, 36, 30, 20, 32]
average = Average(Marks)

print(f'Your average marks is {average}')

if(average >= 80):
    print("So, You deserve A Grade")

elif (average < 80 and average >= 60):
        print("So, You deserve B Grade")

elif (average >= 50 and average <60):
            print("So, You deserve C Grade")

elif(average < 50 and average >= 33):
                print("So, You deserve D Grade")

else:
    print("Sorry, You are fail...")
