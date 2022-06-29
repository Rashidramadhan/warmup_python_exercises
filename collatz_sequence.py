def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result
try:
    user_guez = int(input('Enter number: '))
    while user_guez != 1:
        user_guez = collatz(user_guez)
except ValueError:
    print('please enter a valid number')
