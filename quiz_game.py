# quiz_game.py

import random
from vocabulary import vocabulary  # Import the vocabulary dictionary from vocabulary.py

def play_game():
    score = 0
    words = list(vocabulary.keys())
    random.shuffle(words)

    for word in words:
        correct_answer = word
        definition = vocabulary[word]
        
        options = random.sample(words, 3)
        if correct_answer not in options:
            options[0] = correct_answer
        
        random.shuffle(options)
        
        print(f"\nDefinition: {definition}")
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        
        user_answer = input("Choose the correct word (1-3): ")
        
        if options[int(user_answer) - 1] == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct word was: {correct_answer}")
    
    print(f"\nGame Over! Your final score is {score}/{len(vocabulary)}")

if __name__ == "__main__":
    play_game()
