import random


class BullsAndCowsSolver:
    def __init__(self):
        self.positions: list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 25, 30]
        self.invalid_guesses: set = set()
        self.valid_guesses: set = self._find_valid_numbers()
        self.guessed_nums: set = set()
        self.bot_guesses: list = []
        self.valid_answers: set = set()
        self.player_answers: list = []

    def _find_valid_numbers(self) -> set:
        return {num for num in range(1234, 9877) if self._has_distinct_digits(num)}

    def _has_distinct_digits(self, num: int) -> bool:
        str_digit: str = str(num)
        return len(set(str_digit)) == 4

    def add_input(self, info):
        self.player_answers.append(info)

    def guess_number(self) -> int:
        print("ALL of the bot guesses thus far")
        for i in self.bot_guesses:
            print(i)
        print("/----------------------")

        guesses_size = len(self.bot_guesses) - 1
        return self.bot_guesses[guesses_size]

    def first_guess(self):
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        guess = int(''.join(map(str, numbers[:4])))
        self.guessed_nums.add(guess)
        self.bot_guesses.append(guess)

    def general_guess(self):
        max_set_size = 10000
        new_guess: int = next(iter(self.valid_guesses))

        if len(self.valid_guesses) > 1:
            for i in range(1234, 9877):

                if i in self.valid_guesses and i not in self.guessed_nums:
                    current_max_set_size = self._calculate_sets(i)

                    if max_set_size > current_max_set_size:
                        max_set_size = current_max_set_size
                        new_guess = i

        self.guessed_nums.add(new_guess)
        self.bot_guesses.append(new_guess)

    def _calculate_sets(self, number) -> int:
        partition: dict = {}

        for valid_answer in self.valid_answers:
            set_value = self._function(number, valid_answer)
            partition[set_value] = partition.get(set_value, 0) + 1

        max_set = max(partition.values(), default=0)
        return max_set

    def _function(self, number_to_ask_with, possible_answer) -> int:
        guess_str = str(number_to_ask_with)
        possible_str = str(possible_answer)

        bulls = sum(g == p for g, p in zip(guess_str, possible_str))
        cows = sum((g in possible_str) for g in guess_str) - bulls

        return self._bulls_and_cows_to_digit((bulls, cows))

    def _bulls_and_cows_to_digit(self, info) -> int:
        return 10 + (info[0] * 5) + info[1]

    def reduce_possible_guesses(self):
        last_guess_pos = len(self.bot_guesses) - 1
        last_player_answer = len(self.player_answers) - 1

        current_guess: int = self.bot_guesses[last_guess_pos]
        target_number: int = self._bulls_and_cows_to_digit(self.player_answers[last_player_answer])

        new_set = set()
        for i in self.valid_guesses:
            if i not in self.invalid_guesses and self._function(current_guess, i) == target_number:
                new_set.add(i)
            else:
                self.invalid_guesses.add(i)

        self.valid_guesses = new_set
        if len(self.valid_guesses) == 0:
            raise Exception("Invalid input somewhere")
        else:
            print("Len of valid guesses " + str(len(new_set)))
            print("Set of valid guesses")
            for i in new_set:
                print(i)

            print("/------------------------------")

    def print_guesses(self):
        print("Found the number with:")
        for i in self.bot_guesses:
            print(i)

