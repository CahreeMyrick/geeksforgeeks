def main():
    guess_range = input("Choose range, example: 1 100: ")

    if guess_range == "quit":
        return

    range_split = guess_range.split()

    if len(range_split) != 2:
        print("Please enter exactly two numbers.")
        return

    try:
        left = int(range_split[0])
        right = int(range_split[1])
    except ValueError:
        print("Both values must be valid integers.")
        return

    if left > right:
        print("Left number must be less than or equal to right number.")
        return

    while left <= right:
        guess = (left + right) // 2
        print(f"Guess: {guess}")

        feedback = input("Too low, too high, found, or quit? ").lower().strip()

        if feedback == "low":
            left = guess + 1
        elif feedback == "high":
            right = guess - 1
        elif feedback == "found":
            print("Great! Thanks for playing.")
            return
        elif feedback == "quit":
            return
        else:
            print("Enter something valid: low, high, found, or quit.")

    print("Your feedback was inconsistent. No valid number remains.")


main()