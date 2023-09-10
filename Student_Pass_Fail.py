# Write a program to find out whether a student is Pass Or Fail,
# It requires total 40% and 33% in each subject to Pass.
# Assume 3 subjects and take marks as an input from the user.

Gujarati = int(input('Enter Gujarati subject marks: '))
Hindi = int(input('Enter Hindi subject marks: '))
English = int(input('Enter English subject marks: '))

if(Gujarati < 33 or Hindi < 33 or English < 33):
    print('Sorry, you are fail...')

elif(Gujarati + Hindi + English)/3 < 40:
    print('Sorry, you are fail...')

else:
    percentages = ((Gujarati + Hindi + English)/3) > 40
    print('Congretulation you are Pass with', percentages, '%')
