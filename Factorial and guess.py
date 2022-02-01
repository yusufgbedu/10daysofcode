6# -*- coding: utf-8 -*-
"""
Created on Tue Feb 1 08:00:22 2022

@author: GBEDU
factorial a number
then a guess game using a while loop until answer is correct
"""
# factorial of a number and a guessing game anwser must be 20
#usinf a function
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# using a FOR loop statement

factorial= 1
number = int(input('input number to get factorial'))
if number < 0:
        print('input positive number')
elif number== 0:
        print('factorial is 1')
else:
        for i in range(1, number + 1):
            factorial = factorial * i
print('factorial is:', factorial)



#guess


x= 0
num= 20
while x != num:
    x = int(input('\nwelcome a guessing game\ninput number to guess answer'))
    if x > 0:
        if x < num:
            print('to small')
        elif x > num:
            print ('to big')
    else:
        print('you gave up')
else:
    print ('congrats you got it')
