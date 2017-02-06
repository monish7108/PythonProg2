"""This program contains a series of function designed to work
as per RegEx rules"""
import re


def isvalidIP(ipAdd):

    ip = re.compile(
        "(^[2][0-5][0-5]|^[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})$")

    if ip.match(ipAdd):
        print("valid")
        return True
    else:
        print("Invalid Ip Address")
        return False


def isvalidEmail(email):

    em = re.compile(r"(^[a-zA-Z0-9_.+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z.]{2,5}$)")

    if em.match(email):
        print("valid")
        return True
    else:
        print("invalid email id")
        return False


def isvalidPhoneNum(phnum):

    phone = re.compile("(^[0-9]{3}-[0-9]{3}-[0-9]{4}$)")

    if phone.match(phnum):
        print("valid")
        return True
    else:
        print("invalid Phone Number")
        return False


def containsOnlyNumbers(num):

    numbers = re.compile("(^[0-9]+$)")

    if numbers.match(num):
        print("valid")
        return True
    else:
        print("invalid Number")
        return False


def containsOnlyCharacters(char):

    characters = re.compile("(^[ a-zA-Z]+$)")

    if characters.match(char):
        print("valid")
        return True
    else:
        print("should only be characters")
        return False


def containsSpecifiedSpecialCharacters(special):

    spechar = re.compile("(^[&\-\)\(]+$)")

    if spechar.match(special):
        print("valid")
        return True
    else:
        print("only above listed special characters are allowed")
        return False

if __name__ == "__main__":
    print(__doc__)
    print("====================================================================")
    ipAdd = input("Enter the ip address: ")
    isvalidIP(ipAdd)
    print("====================================================================")
    email = input("Enter email address: ")
    isvalidEmail(email)
    print("====================================================================")
    print("\nPhone number should be in the formate XXX[citycode]-XXX-XXXX")
    phnum = input("Enter Phone Number: ")
    isvalidPhoneNum(phnum)
    print("====================================================================")
    num = input("Enter Only Numbers: ")
    containsOnlyNumbers(num)
    print("====================================================================")
    char = input("Enter Only characters \nNote:spaces are allowed: ")
    containsOnlyCharacters(char)
    print("====================================================================")
    special = input("Enter only special Characters(&, -, (, ),): ")
    containsSpecifiedSpecialCharacters(special)
    print("====================================================================")
