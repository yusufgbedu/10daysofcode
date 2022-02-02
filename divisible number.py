# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
restart= True
while restart:
    x = abs(int(input('input number')))
    z=abs(int(input('input your desired divisor')))
    y= x
    while x and z > 0:
        y -= 1
        if y % z == 0:
            print('', y, 'is the first number less than',x,'that is divisible by ',z)
            break
    option= input('would you like to perform another operation\tY/N')
    if option in ('N','n','No','NO'):
        restart=False
        print('Thanks for using my program')
        satisfied= input('hope you enjoyed testing my program\tY/N')
        break    
            
            