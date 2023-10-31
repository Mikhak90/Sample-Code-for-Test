
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True

    # Check for divisibility by 2 or 3
    if number % 2 == 0 or number % 3 == 0:
        return False

    # Check for divisibility by numbers of the form 6k ± 1
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

# Example usage:
number = 73
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
