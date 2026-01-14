def digit_predictor():
    print("🔢 Simple Digit Predictor")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("Enter a number: ")

        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break

        try:
            num = int(user_input)

            # Digit count
            digits = len(str(abs(num)))
            if digits == 1:
                print("Prediction: Single digit number")
            elif digits == 2:
                print("Prediction: Double digit number")
            else:
                print("Prediction: Multiple digit number")

            # Even or Odd
            if num % 2 == 0:
                print("Prediction: Even number")
            else:
                print("Prediction: Odd number")

            # Positive / Negative
            if num > 0:
                print("Prediction: Positive number")
            elif num < 0:
                print("Prediction: Negative number")
            else:
                print("Prediction: Zero")

            print()

        except ValueError:
            print("Invalid input. Please enter a number.\n")

if __name__ == "__main__":
    digit_predictor()
