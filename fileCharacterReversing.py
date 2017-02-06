"""This program takes existing filename as input and creates a new file by

printing the contents of old file in reverse order [Characters].
==============================================================="""


def file_printing(filename,outputFilename):
    """This function writes characters from one file to another in reverse order."""
    data = open(filename)
    words = data.read()
    data.close()
    data = open(outputFilename, "w+")
    for i in words[::-1]:
        data.write(i)
    data.close()

if __name__ == "__main__":
    print(__doc__)
    filename = input("enter the name of the file: ")
    outputFilename=input("enter the name of the file to write the output: ")
    file_printing(filename,outputFilename)
