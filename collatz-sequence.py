def collatz(number):
    number = int(user_input) # converts input into an integer

    while number != 1: # continues to check until the result is 1
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
        if int(user_input) < 0: # does not allow negative integers
            print('Negative integers not allowed. Try again.')
            continue
        else:
            print(collatz(user_input))
    
    except ValueError: # does not allow string input
        print("Invalid input! Enter a positive integer.")

    collatz_again = input('Would you like to collatz another number? yes/no: ')
    if collatz_again.lower() == 'yes' or collatz_again.lower() == 'y':    
        print('Enter any positive integer.')
        continue
    else:
        print('Have a nice day!')
        break