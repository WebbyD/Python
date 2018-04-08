# Author:Marcais Jackson
#This program deploys a number guessing game that requires the use of conditional logic and decision making control 
#structures during its construction.

#Global variable to keep count of guesses.
guess_count = 0
#Global variable to keep the success of a player. 
success = 0  

#ClearScreen function, it clears whatever is on the current console.
def ClearScreen(): 
 # Multiplies the new line with 100.
    clear = '\n' * 100  
	#Prints 100 new lines to screen.
    print clear  

#Function
def guess_number(secret_number):
  # Declaring global variables in function to change them.
    global guess_count, success 
	# For every guess count incremented.
    guess_count += 1  
	# Prompts user to guess the number.
    guess_secret_number = input("\nTry to guess the secret number:") 
	# If guess number less than secret number
    if guess_secret_number < secret_number:
	#Print statement for when the guess number less than secret number.
        print("The secret number is higher than " + str(guess_secret_number)) 
		# If guess number greater than secret number.
    elif guess_secret_number > secret_number:  
        print("The secret number is less than " + str(guess_secret_number))  
    else:  #If the guess number equals to the secret number
        success = 1  #Make global variable 1 indicating succeeded.
        print("You got it!!!")  #Print statement in success case.

#Repeat function.
def repeat(secret_number):  
#If guess count less than 5.
    if guess_count != 5:
	# if player succeeded.
        if success == 1:  
            print("\nCongratulations... the secret number was " + str(secret_number) + "\nYOU WIN... GAME OVER")
        else:  # If player did not succeed till now and guesses remain.
		#Calls function.
            guess_number(secret_number) 
			#Calls to same function.
            repeat(secret_number) 
    else:  # If guesses are completed
        if success == 1:  # if player succeeds...
            print("\nCongratulations... the secret number was " + str(secret_number) + "\nYOU WIN... GAME OVER")
        else:  #If player did not succeed and guesses are over
            print(
                "\nSorry... you were not able to guess the secret number\nYOU LOSE... GAME OVER\n\nBTW the secret number was " + str(
                    secret_number) + "... Better luck next time")


#Main function					
def main():  
#Prompts for secret number.
    secret_number = input("Please enter a secret number:")  
    ClearScreen()  # Clears screen function.
    repeat(secret_number)  #Calls to repeat function.


if __name__ == '__main__':
    main()  #Call to main method.
	#End program.
raw_input("Press Any Key To Continue")