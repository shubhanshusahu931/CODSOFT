import random

def computer_choice():
    return random.choice(["Stone", "Paper", "Scissor"])

user_total_score = 0
computer_total_score = 0
draw_matches=0
round_number = 1
def Determine_winnner():
    global user_total_score,computer_total_score,round_number
    print(f"this is {round_number} round ")
    user_score = 0
    computer_score = 0

    user_choice = input("Enter your choice (Stone/Paper/Scissor): ").capitalize()
    comp_choice = computer_choice()
    print(f"Computer chose: {comp_choice}")

    if user_choice not in ["Stone", "Paper", "Scissor"]:
        print(" Enter a valid input!")
    else:
        if user_choice == comp_choice:
            print(" It's a Draw!")
            draw_matches += 1
        elif user_choice == "Stone":
            if comp_choice == "Paper":
                computer_score += 1
                print(" Computer wins this round!")
            elif comp_choice == "Scissor":
                user_score += 1
                print(" You win this round!")
        elif user_choice == "Paper":
            if comp_choice == "Scissor":
                computer_score += 1
                print(" Computer wins this round!")
            elif comp_choice == "Stone":
                user_score += 1
                print(" You win this round!")
        elif user_choice == "Scissor":
            if comp_choice == "Stone":
                computer_score += 1
                print(" Computer wins this round!")
            elif comp_choice == "Paper":
                user_score += 1
                print(" You win this round!")

        user_total_score += user_score
        computer_total_score += computer_score
        print(f"Score This Round => You: {user_score} | Computer: {computer_score}")
        print(f" Total Score => You: {user_total_score} | Computer: {computer_total_score}")
        round_number += 1

def round():
    Determine_winnner()

round()

while True:
    print("Do you want to play another round? (yes/no)")
    play_again = input("Enter your choice: ").lower()
    if play_again == "yes":
        round()
    else:
        print("🎮 Game Over!")
        print(f"total number of rounds is {round_number}")
        print(f"total number of draw rounds is {draw_matches}")
        break

        
