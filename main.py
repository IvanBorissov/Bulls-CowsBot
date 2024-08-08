from bulls_and_cows_solver import BullsAndCowsSolver

bulls: int = 0
cows: int = 0
game = BullsAndCowsSolver()

game.first_guess()
print("Guess:")

while True:
    print(game.guess_number())
    user_input = input("Enter bulls and cows (e.g., '2 1') or 'exit' to quit: ")

    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break

    try:
        bulls, cows = map(int, user_input.split())
    except ValueError:
        print("Invalid input. Please enter the number of bulls and cows separated by a space.")
        continue

    if bulls == 4:
        break

    if not (0 <= bulls <= 4) or not (0 <= cows <= 4) or (bulls + cows) > 4:
        print("Invalid input. Please enter valid numbers for bulls and cows.")
        continue

    game.add_input((bulls, cows))
    game.reduce_possible_guesses()
    game.general_guess()
    print(f"You provided feedback: Bulls = {bulls}, Cows = {cows}")

print("Found the number with")
print(game.print_guesses())

#8631
# 1. 1695 - 638 possible numbers left
# 2. 1236 - 26 possible numbers left
# 3. 1329 - 5 possible numbers left
# 4. 3265 - 3 possible numbers left {4631, 7631, 8631}
# 5. 4631 - 2 possible numbers left
# 6. 7631 - 1 possible number left
# 7. 8631 - the answer

#8631
# 1. 8126 - 204 possible numbers left
# 2. 1236 - 20 possible numbers left
# 3. 1328 - 4 possible numbers left
# 4. 3816 - 1 possible number left
# 5. 8631 - the answer

