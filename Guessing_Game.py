import random

def computerGuess(lowval, highval, randnum, count=0):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        # If guess is in the middle, it is found!
        if guess == randnum:
            return count
        # If "guess" is greater than the number,
        # it must be found in the lower half of the set of numbers
        # between the lower calue and the guess
        elif guess > randnum:
            count = count + 1
            return computerGuess(lowval, guess-1, randnum, count)
         # The number must be in the upper set of numbers
         # between the guess and the upper value
        else:
            count = count + 1
            return computerGuess(guess + 1, highval, randnum, count)
    else:
        # Number not found
        return -1

#generate a random number between 1 and 100
randnum = random.randint(1,101)

count = 0
guess = -99

while (guess != randnum):
    # Get the user's guess
    guess1 = input("Enter your guess between 1 and 100:")
    guess = int(guess1)
    if guess < randnum:
        print("higher")
    elif guess > randnum:
        print("lower")
    else:
        print("you guessed it!")
        break
    count = count+1
#end of while loop

print("You took " , count , "steps to guess the number")
print("Computer took " , computerGuess(0,100,randnum) , " steps!")
if(count > computerGuess(0, 100, randnum)):
   print("You lose!")
elif(count <= computerGuess(0, 100, randnum)):
   print("You won!")
   
