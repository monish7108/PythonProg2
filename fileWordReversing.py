"""This program takes existing filename as input and creates a new file by
     data=open(filename)
s of old file in reverse order [words].
============================================================"""


def file_printing(filename,outputFilename="output.txt"):
    """This function writes from one file to another in reverse order."""
    data=open(filename)
    lines=data.readlines()
    data.close()
    data=open(outputFilename,"w+")
    for line in lines[::-1]:
        wordlist=line.split(" ")
        for words in reversed(wordlist):
            data.write(words+" ")
    data.close

if __name__ == "__main__":
    print(__doc__)
    filename = input("enter the name of the file: ")
    outputFilename=input("enter the name of the file to write the output: ")
    file_printing(filename,outputFilename)
