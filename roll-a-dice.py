import random

def roll_dice():
    # Ask the user if they want to roll the dice
    response = input("Do you want to roll the dice? (y/n): ").lower()

    # While loop to run until the user enters 'n'
    while response == 'y':
        # Generate a random number between 1 and 6
        dice_result = random.randint(1, 6)

        # Display the dice representation based on the random number
        if dice_result == 1:
            print("---------")
            print("|       |")
            print("|   *   |")
            print("|       |")
            print("---------")
        elif dice_result == 2:
            print("---------")
            print("| *     |")
            print("|       |")
            print("|     * |")
            print("---------")
        elif dice_result == 3:
            print("---------")
            print("| *     |")
            print("|   *   |")
            print("|     * |")
            print("---------")
        elif dice_result == 4:
            print("---------")
            print("| *   * |")
            print("|       |")
            print("| *   * |")
            print("---------")
        elif dice_result == 5:
            print("---------")
            print("| *   * |")
            print("|   *   |")
            print("| *   * |")
            print("---------")
        else:  # dice_result == 6
            print("---------")
            print("| *   * |")
            print("| *   * |")
            print("| *   * |")
            print("---------")

        # Prompt the user to roll again
        response = input("Roll again? (y/n): ").lower()

    print("Goodbye!")

# Run the roll_dice function
if __name__ == "__main__":
    roll_dice()
