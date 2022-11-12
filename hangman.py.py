import random

print("H A N G M A N", "\n")

win_count = 0
lost_count = 0
input_list = []

def gameplay():
    global win_count
    global lost_count
    global input_list

    words = ['python', 'java', 'swift', 'javascript']
    game_choice = list(random.choice(words))
    word = ("-" * len(game_choice))
    print(word)
    listed_word = list(word)
    attempt = 0

    while attempt < 8:
        print("Input a letter: ")
        user_input = input()

        input_list.append(user_input)

        if len(user_input) != 1:
            print("Please, input a single letter.")
            print("".join(listed_word))

        elif user_input.islower() is False or user_input.isnumeric() is True:
            print("Please, enter a lowercase letter from the English alphabet.")
            print("".join(listed_word))

        elif user_input in game_choice and user_input not in listed_word:
            for i in range(len(word)):
                if game_choice[i] == user_input:
                    listed_word[i] = user_input

            print("".join(listed_word))
            if "-" not in listed_word:
                print("You guessed the word", ("".join(listed_word))+"!")
                print("You survived!")
                win_count += 1
                break

        elif user_input not in game_choice:
            if input_list.count(user_input) > 1:
                print("You've already guessed this letter.")
                print("".join(listed_word))
            else:
                print("That letter doesn't appear in the word.")
                print("".join(listed_word))
                attempt += 1

        elif (user_input in game_choice) and input_list.count(user_input) > 1:
            print("You've already guessed this letter.")
            print("".join(listed_word))

    if "-" in listed_word:
        print("You lost!")
        lost_count += 1

while True:
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    decision = input()
    if decision == "play":
        print(gameplay())
    elif decision == "results":
        print("You won: ", win_count, "times.")
        print("You lost: ", lost_count, "times.")
    elif decision == "exit":
        break
