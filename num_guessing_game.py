import random


class NumberGuessingGame:

    def __init__(self):
        self.LOWER = 1
        self.HIGHER = 10
        self.MAX_CHANCES = 5
        self.OUT_OF_CHANCES = False

    def get_random_number(self):
        return random.randint(self.LOWER, self.HIGHER)

    def start(self):

        random_number = self.get_random_number()

        print(
            f"Guess the random number from {self.LOWER} to {self.HIGHER}")

        chances = 0
        while True and not (self.OUT_OF_CHANCES):
            if chances < self.MAX_CHANCES:
                user_number = int(input("Please guess the number: "))
                chances += 1
            else:
                self.OUT_OF_CHANCES = True

            if self.OUT_OF_CHANCES:
                print("-> Sorry! you are Out of chances")

            if user_number == random_number:
                print(
                    f"-> You have attempted{chances + 1} tries{'s' if chances > 1 else ''}!")
                break
            elif user_number < random_number:
                print("-> Your number is lower than the random number")
            else:
                print("-> Your number is larger than the random number")
numberGuessingGame = NumberGuessingGame()
numberGuessingGame.start()



