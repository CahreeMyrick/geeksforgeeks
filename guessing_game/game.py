
def validate_bounds(interval):
  while True:
    interval_split = interval.split()
    left_bound = interval_split[0]
    right_bound = interval_split[1]

    if len(interval_split) > 2:
        interval = input("Choose valid interval: ")

    try:
        left_bound = int(left_bound)
        right_bound = int(right_bound)

    except ValueError:
        interval = input("Choose valid integer values: ")
    
    else:
       break

    if left_bound > right_bound:
       interval = input("Left bound must be less than right bound: ")
    
    else:
       break

       

  return left_bound, right_bound
    
def validate_feedback(feedback):
    options = {"low", "high", "found", "quit"}
    while True:
        if feedback not in options:
            feedback = input("Give valid feedback (ex: low, high, found): ")
        else:
           break
    return feedback

def main():
  # get interval from user
  interval = input("Choose interval (ex: 1 100, -5 1000): ")

  left, right = validate_bounds(interval)

  guess = (left + right) // 2

  while True:
    print(f"Guess: {guess}")
    feedback = input("Feedback: ")
    feedback = validate_feedback(feedback)

    if feedback == "low":
      left = guess + 1
    elif feedback == "high":
      right = guess - 1
    elif feedback == "quit":
       return
    else:
       print("Great. Thanks for playing.")
       return
    guess = (left + right) // 2

main()