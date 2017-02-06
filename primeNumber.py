"""This program takes a number and tells if it is prime and

if the given number is prime it also tells the next prime number
=================================================================="""


def is_prime(userinput):
    """Return True if *number* is prime."""
    if userinput == 0:
        return False
    elif userinput == 1:
        return False
    else:
        for i in range(2, userinput):
            if userinput % i == 0:
                return False
    return True


def next_prime(userinput):
    """Print the closest prime number larger than *number*."""
    nextPrimeNum = userinput
    while True:
        nextPrimeNum += 1
        if is_prime(nextPrimeNum):
            break
    return nextPrimeNum

if __name__ == "__main__":
    print(__doc__)
    userinput = int(input("Enter the number: "))
    print(is_prime(userinput))
    output=next_prime(userinput)
    print("Next Prime Number is "+ str(output))
