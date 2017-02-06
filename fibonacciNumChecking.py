"""This programs check every number from command line
    and tells whether number is in fibbonacci series or not.
    Math:   Instead of producing loop and checking the number there is a mathematical formula.
            If (5*x*x)+4  or (5*x*x)-4   or both are perfect squares,
            then the number is in fibonacci.
======================================================================="""


def isPerfectSquare(x):
    """if the number is not having decimal part then dividing it from int type
     of same num  gives 0"""
    return (x**0.5) % int(x**0.5) == 0


def fibonacciSeries(userinput):
    """This function tells whether number is in fibbonacci series or not."""
    try:
        isinstance(int(userinput), int)
        userinput = int(userinput)
    except ValueError as e:
        print(e)
    else:
        if isPerfectSquare((5*userinput*userinput) - 4) or isPerfectSquare((5*userinput*userinput) + 4):
            return True
        else:
            return False


if __name__ == "__main__":
    print(__doc__)
    userinput = input("Enter the number you want to check: ")
    if fibonacciSeries(userinput):
        print("The numeber is present in fibonacci series.")
    else:
        print("The number is not present in fibonacci series.")
