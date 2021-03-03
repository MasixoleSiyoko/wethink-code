def thinking():
    print('Iam Thinking of a number between 1 and 20.')
    print('Take a Guess.')
thinking()
guesses= 0
while True:
    

    guessnumber = int(input('Enter number '))
    if guessnumber < 16:
        print('Your guess is too low')
        print('Take a Guess')
        guesses +=1
    if guessnumber > 16:
        print('Number is too high')
        print('Take a guess')
        guesses +=1
    if guessnumber == 16:
        print('correct')
        print('You did it in '+ str(guesses) + ' guesses')
        break
    



