'''
In this problem, you'll create a program that guesses a secret number!
The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

Here is a transcript of an example session:
Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83
'''
###################################################################################
print ("Please think of a number between 0 and 100!")
low = 0
high = 100
guess_number = (low+high)//2                   #interger division
print ("Is your secret number ",guess_number,'?', sep="")      #sep = "" is used to remove space between an interger and a string in the print statement. Similarly end="" can be used 
guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while guess is not 'c':
    if guess == 'l':
        #print ("Guess is too low")
        low = guess_number
        guess_number = (low + high)//2
        print ("Is your secret number ",guess_number,'?', sep="")
        guess = input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    elif guess == 'h':
        #print ("Guess is too high")
        high = guess_number
        guess_number = (high + low)//2
        print ("Is your secret number ",guess_number,'?', sep="")
        guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    else:
        print ("Sorry, I did not understand your input")
        print ("Is your secret number ",guess_number,'?', sep="")
        guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

if guess == 'c':
    print ("Game over. Your secret number was:",guess_number)
