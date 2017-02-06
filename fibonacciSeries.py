"""This program takes a number from command line

and tells whether the number is present in fibonacci or not.

Works only for one input.
============================================"""

def nextNum(x,y):
    return x+y

def fibonacciSeries(userinput=2):
    f1,f2=0,1
    fibseries=[f1,f2]
    # userinput=int(input("enter the range for the fibonacci series"))
    for i in range(2,userinput,1):
        fibseries.append(nextNum(fibseries[i-1],fibseries[i-2]))
    return fibseries

if __name__=="__main__":
    print(__doc__)
    userinput=int(input("enter the range for the fibonacci series: "))
    outputlist=fibonacciSeries(userinput)
    print(outputlist)