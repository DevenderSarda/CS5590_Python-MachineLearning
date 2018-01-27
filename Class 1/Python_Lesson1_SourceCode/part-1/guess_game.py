import random
print("Welcome to Guess Game. Please select a lucky number between 0-9 and the program tells you if the number is above or below or right on target. Good Luck. Happy Guessing!")
while 0==0:
 "The below statement generates a random number between 0-9"
 n= random.randint(0,9)
 n1=input("Enter the lucky number between 0-9:")
 "The below statement converts random number to integer"
 guess=int(n1)
 "Check if random number matches with the user entered number, If yes break the loop and show a message"
 if guess == n:
     print("Yipeee! Number guessed by you is right on target. ")
     break
 elif guess > n:
        print("Hard Luck! The Number guessed is above the random number")
 else:
        print("Try Harder! The  Number guessed is below the random number")
