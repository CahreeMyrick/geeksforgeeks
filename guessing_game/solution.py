def validate_bounds(interval):
    while True:
        interval_split = interval.split()

        if len(interval_split) != 2:
            interval = input("Choose valid interval with two numbers: ")
            continue

        try:
            left_bound = int(interval_split[0])
            right_bound = int(interval_split[1])
        except ValueError:
            interval = input("Choose valid integer values: ")
            continue

        if left_bound > right_bound:
            interval = input("Left bound must be less than right bound: ")
            continue

        return left_bound, right_bound


def validate_feedback(feedback):
    options = {"low", "high", "found", "quit"}

    while feedback not in options:
        feedback = input("Give valid feedback: low, high, found, or quit: ")

    return feedback


def main():
    interval = input("Choose interval (ex: 1 100, -5 1000): ")
    left, right = validate_bounds(interval)

    while left <= right:
        guess = (left + right) // 2
        print(f"Guess: {guess}")

        feedback = input("Feedback: ")
        feedback = validate_feedback(feedback)

        if feedback == "low":
            left = guess + 1
        elif feedback == "high":
            right = guess - 1
        elif feedback == "quit":
            return
        elif feedback == "found":
            print("Great. Thanks for playing.")
            return

    print("Your feedback was inconsistent. No valid guesses remain.")


main()