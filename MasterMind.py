#This is a program that I made which is similar to Wordle, but using numbers. 
#The program is called MasterMind. 
import random
import math

#Defining the generated number 
def splitNum(num):
    unitsgen = num%10
    tensgen = (math.floor(num/10))%10
    hundgen = (math.floor(num/100))%10
    thousgen = (math.floor(num/1000))%10
    numSet = {thousgen, hundgen, tensgen, unitsgen}

    #checks for making sure the number generated does not have any repeating digits 
    isDupeExist = len(numSet) < 4
    numList = [isDupeExist, unitsgen, tensgen, hundgen, thousgen]
    return numList

shouldContinue = "y"
while shouldContinue == "y":

    i = random.randrange(1000, 9999)
    genList = splitNum(i) 

    while genList[0]:
        i = random.randrange(1000, 9999)
        genList = splitNum(i) 
    
    #Bulls mean that the digit is correct and in the right spot of the generated number 
    bulls = 0

    #Cows mean that the digit is correct, but in the wrong spot of the generated number
    cows = 0
    print("Hey! Let's play this game of cows and bulls!")
    print("I am thinking of a 4 digit number")

    while bulls != 4:
        bulls = 0
        cows = 0

        validGuess = True
        try: 
            guess = int(input("Can you guess what it is? "))
            guessList = splitNum(guess)
        except:
            validGuess = False
        #Many constraints to follow for the the guess to be a valid 
        while guessList[0] or guessList[4] == 0 or guess < 1000 or guess > 9999 or validGuess == False:
            print("Invalid entry, please enter a 4 digit number with no digits repeating. ")
            validGuess = True
            try: 
                guess = int(input("Can you guess what it is? "))
            except:
                validGuess = False
                continue

            guessList = splitNum(guess)

        
        #if generated number has same digits as number guessed 
        if genList[4] == guessList[4]:
            bulls = bulls + 1
        elif guessList[4] in genList:
            cows = cows + 1

        if genList[3] == guessList[3]:
            bulls = bulls + 1
        elif guessList[3] in genList:
            cows = cows + 1

        if genList[2] == guessList[2]:
            bulls = bulls + 1
        elif guessList[2] in genList:
            cows = cows + 1

        if genList[1] == guessList[1]:
            bulls = bulls + 1
        elif guessList[1] in genList:
            cows = cows + 1

        print(str(bulls), "bulls")
        print(str(cows), "cows")

    
    print("You win! Good job!")

    shouldContinue = input("Do you want to continue playing, (y or n)? ") 

print("Alright, have a great day!!")




    
    









    