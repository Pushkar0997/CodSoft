import random

def rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Choose one: rock, paper, or scissors")
    
    choices = ["rock", "paper", "scissors"]
    
    user_choice = input("Your choice: ")
    
    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return rock_paper_scissors()
    
    computer_choice = random.choice(choices)
    print(f"Computer's choice: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors"):
                print("You win!")
    elif(user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    elif(user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
         
    else:
        print("You lose!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        rock_paper_scissors()
    else:
        print("Thanks for playing! Goodbye!")

rock_paper_scissors()
