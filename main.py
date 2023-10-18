from getpass import getpass

# Get user names
user1 = input("User 1, enter your name: ")
user2 = input("User 2, enter your name: ")

# Function to get a valid secret number within the specified range
def get_valid_secret_number(min_range, max_range):
    """
    Get a valid secret number within the specified range.

    Args:
        min_range (int): The minimum range for the secret number.
        max_range (int): The maximum range for the secret number.

    Returns:
        int: A valid secret number within the specified range.
    """
    while True:
        try:
            secret_number = int(getpass(f"Enter the secret number (between {min_range} and {max_range}): "))
            if min_range <= secret_number <= max_range:
                return secret_number
            else:
                print("Please enter a number within the specified range.")
        except ValueError:
            print("Please enter a valid numeric value.")

# Function to get the number of chances
def get_chances():
    """
    Get the number of chances from the user.

    Returns:
        int: The number of chances.
    """
    while True:
        try:
            chances = int(input("Enter the number of chances: "))
            return chances
        except ValueError:
            print("Please enter a valid numeric value for the chances.")

# Get the range for the secret number
min_range = int(input("Enter the minimum range for the secret number: "))
max_range = int(input("Enter the maximum range for the secret number: "))

# Get a valid secret number within the range
secret_number = get_valid_secret_number(min_range, max_range)

# Get the number of chances
chances = get_chances()

n_att = 0
while n_att < chances:
    print("\n")
    print(f"{user2}, you have {chances - n_att} attempts left to guess the number.")
    
    # Get User 2's guess
    try:
        att = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if att == secret_number:
        print(f"{user2}, you've won in {n_att + 1} attempts!")
        break
    elif att < secret_number:
        print("The secret number is higher.")
    else:
        print("The secret number is lower.")
    n_att += 1

if n_att == chances:
    print(f"{user2}, game over! The secret number was {secret_number}.")