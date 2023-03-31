def collatz(number):
    number = int(user_input) # converts input into an integer

    while number != 1: # continues to check until == 1
        if number % 2 == 0: # number is even
            number = number // 2
            print(number)
        elif number % 2 == 1: # number is odd
            number = 3 * number + 1
            print(number)
    return 'Great! Your number has been collatzed!'

print('COLLATZ SEQUENCE:')
print('Enter any positive integer.')
while True:
    try:
        user_input = input()
        if int(user_input) < 0: 
            print('Negative integers not allowed. Try again.')
            continue
        else:
            print(collatz(user_input))
            break
            
    except ValueError: # does not accept string inputs
        print("Invalid input! Enter a positive integer.")