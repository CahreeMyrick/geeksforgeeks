
def main():
    guess_range = input("Choose Range: ")

    range_split = guess_range.split()
    left = int(range_split[0])
    right = int(range_split[1])

    guess = (left + right) // 2

    while (True):
        if guess_range == "quit":
            return False
        
        print(f"guess: {guess}")
        feedback = input("is this is? ")
        
        if feedback == "low":
            left = guess + 1
            guess = (left + right ) // 2
        
        elif feedback == "high":
            right = guess - 1
            guess = (left + right) // 2
        
        elif feedback == "found":
            print("Great! Thanks for playing.")
            return False
    
        elif feedback == "quit" :
            return False
        
        else:
            print("Enter somthing valid: (ex: low, high, found)")

main()

        
