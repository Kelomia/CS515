'''
Homework-1-CS515
author Zimu Jiao

'''

from cs515 import *

'''
def factorial(number):
    # check the input is positive or not.
    if(number>0):
        if(number==1):
            return 1
        else:
            return number*factorial(number-1)
    else:
        #if the input is not positive integer
        print("Illegal input, please input positive integer.")
'''

def factorial(number):
    if number>1:
        return number*factorial(number-1)
    elif number==1:
        return 1
    else:
        return 'Please input positive integer'

'''
def mean(list):
    sum=0
    count=0
    for number in list:
        sum=sum+number
        count=count+1
    return sum/count
'''
def Sum(list):
    return reduce(lambda x,sum: x+sum,list)

def mean(list):
    return reduce(lambda number,sum: number+sum,list)/len(list)

def divides(n,k):
    return n%k==0
    # while k is in range(2,n)

'''
def prime(number):
    for k in range(2,number):
        if (number%k==0):
            return False
    return True
'''

def prime(number):
    if number==1:
        return False
    if(filter(lambda k:number%k==0,range(2,number))==[]):
        return True
    else:
        return False