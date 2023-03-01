def collatz(number):
    if number % 2 == 0: # number is even
        number = number // 2
        return number
    elif number % 2 == 1: # number is odd
        number = 3 * number + 1
        return number

print('COLLATZ SEQUENCE:')
print('Enter any positive integer.')
while True:
    try:
        user_input = input()
        number = int(user_input) # converts input into an integer

        while number != 1: # continues to check until == 1
            number = collatz(number) 
            print(number)
        else:
            break
    except ValueError: # does not accept string inputs
        print("Invalid input! Enter a positive integer.")

print('Great! Your number has been collatzed!')