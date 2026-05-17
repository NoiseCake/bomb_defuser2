from hint import give_hint
from number_generator import number

#Replica of code i found online, for practice use only

def main():
    print ("You walk into a room and there's a bomb on the table!")
    print ("You have 6 attempts to defuse!")
    attempts = 6
    print("Enter the correct number to defuse the bomb, press h for help, press q to try to escape")

    while True:
        if attempts == 0:
            print ("You have ran out of chances!")
            print ("You failed")
            break
        action = input()
        if action.lower() == "q":
            print ("you tripped and fell and banged your head on the table and died and so did everyone else and you wife cheated on you AND THIS IS ALL YOUR FAULT")
            break

        if action.lower() == "h":
            attempts = attempts - 1
            give_hint()
            print (f"You have {attempts} attempts left")

        elif action == str(number):
            print("Correct! you win! Congratulations")
            break
        elif action > str(number):
            attempts = attempts - 1
            print(f"You have a feeling that the number is lower than {action}")
            print(f"You have {attempts} attempts left")
        elif action < str(number):
            attempts = attempts - 1
            print(f"You have a feeling that the number is higher than {action}")
            print(f"You have {attempts} attempts left")


main()