"""This program takes a path of directory as input and gives list of all the

all the files, sub-folders, files under sub-folders and so on.
==============================================================
"""

import os

file = []
dir = []

def listing(path1, pathlist1):


    for items in pathlist1:

        if os.path.isfile(os.path.join(path1, items)):
            file.append(os.path.join(path1, items))

        else:
            dir.append(os.path.join(path1, items))
            newpath = os.path.join(path1, items)
            newpathlist = os.listdir(newpath)
            listing(newpath, newpathlist)

    printing_the_output(file,dir)


def printing_the_output(file,dir):

    # print(len(dir))
    for d in dir:
        print(d)
    # print(len(file))
    for f in file:
        print(f)


def main(userinput):
    try:
        os.path.isdir(userinput)
        pathlist = os.listdir(userinput)

    except NotADirectoryError as e:
        print("\n", e)

    else:
        listing(userinput, pathlist)


if __name__ == "__main__":

    print(__doc__)
    userinput = input("enter the path you want to walk through: ")
    main(userinput)
    #print(file)