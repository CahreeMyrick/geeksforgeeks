def main():
  
    guess_range = input("Choose range (ex: 1 100, -3 2000): ")

    range_split = guess_range.split()
    left = range_split[0]
    right = range_split[1]

    try:
    # must be a valid integer
        left = int(left)
        right = int(right)

    except ValueError:
        print("Input not an integer.")


    if left > right:
        print("Left must be less than right")

    while left <= right:
        guess = (left + right) // 2
        print(f"Guess: {guess}")

        feedback = input("Too high, too low, or found: ").lower().strip()

        if feedback == "low":
            left = guess + 1
        
        elif feedback == "high":
            right = guess - 1

        elif feedback == "found":
            print("Great. Thanks for playing!")
            return

        elif feedback == "quit":
            return
        
        else:
            print("Enter a valid option (ex: low, high, found, quit).")

    
main()
        
