while True:
    num = eval(input('Enter a Number >= 2: '))

    if num < 2:
        print("Invalid input, Enter a number greater than 2"); print()
        break

    else:
        for num2 in range(1, 10):
            num2 = num % num2
        print('Smallest Factor other than 1 for', num, 'is', num2); print()
