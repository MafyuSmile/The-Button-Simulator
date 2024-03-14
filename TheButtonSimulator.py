import random

def simulate_game():
    current_number = 0
    attempts = 1
    high_score = 0
    total = 0
    
    while attempts < 10000000:
        odds_of_increase = 1 - (current_number / 100)
        if random.random() < odds_of_increase:
            current_number += 1
            if current_number > high_score:
                high_score = current_number
                print(f"New High Score: {high_score} at attempt {attempts}")
        else:
            total += current_number
            current_number = 0
            attempts += 1
    
    average_score = total / attempts
    print(f"\nFinal High Score: {high_score}")
    print(f"Total Attempts: {attempts}")
    print(f"Average Score: {average_score}")
    print(f"Total Score: {total}")

simulate_game()
