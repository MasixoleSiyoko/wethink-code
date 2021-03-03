num1 = int(input('enter a number'))
num2 = int(input('enter a second number'))
calculation= (num1 + num2)
# print(calculation)
# numbers= [0-9]

if num1 >= 0 and num1 <=9:
    print('calculation is {}'.format(calculation))
elif num2 >=0 and num2 <=9:
    print('calculation is {}'.format(calculation))
    
else: 
    print('Error terminate')
    