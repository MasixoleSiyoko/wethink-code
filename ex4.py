name= str(input('Enter Your name '))
greeting = ('Hello ') +  name  + (" Lets play Hangman ")
print(greeting)
word = 'Play '
missingLetter = 'l'
missingWord = word.replace(missingLetter ,'_')
userGuess= input(' Guess the missing Letter in ' + missingWord)
if missingLetter == userGuess:
    print('correct')

else:
     print('incorect')

