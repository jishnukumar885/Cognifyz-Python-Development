def generate_fibonacci_sequence(terms):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < terms:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence


try:
    num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()


if num_terms <= 0:
    print("Please enter a positive integer for the number of terms.")
else:
    result = generate_fibonacci_sequence(num_terms)
    print(f"Fibonacci sequence up to {num_terms} terms: {result}")
