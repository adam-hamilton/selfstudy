#!/usr/bin/python

def fact(num):
    """
    Args:
        factoral input number
    Returns:
        computed factoral
    """

    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def main():
    """
    Args:
        None - requires user input of factoral values
    Returns:
        Factoral result
    """

    while True:
        number = input("Enter a number: ")
        try:
            val = int(number)
            if val < 0:  # if not a positive int print message and ask for input again
                print("Sorry, input must be a positive integer, try again")
                continue
            break
        except ValueError:
            print("That's not an int!")

    result = fact(number)
    print(result)

if __name__ == '__main__':
    main()
