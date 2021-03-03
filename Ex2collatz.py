def collatz():
	#user input
    number = int(input("Enter a number"))

	#this code checks if the input is divisible by 2 and if thats true then we divide the user input and return the result
    if number %2== 0:
        print(number,"//2")
        even = number/2
        print(even)
        
    else:
        print("3*",number,"+ 1")
        odd = 3*number+1
       	print(odd)

collatz()

    