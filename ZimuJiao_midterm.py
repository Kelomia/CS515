'''
 CS515 - Midterm
@ author: Zimu Jiao
'''

from functools import *

def followers(wordlist,starter):
    '''
    :param wordlist: A listof nonempty strings......
    :param starter:  a nonempty string with no spaces
    :return: a list of all words follow starter in wordlist.
    '''
    result=[]       # Set the result as list
    for i in range(len(wordlist)-1):    # Loop: the range is smaller the length by 1 because the last one doesn't work
        if wordlist[i]==starter:        # if a 'starter' found, the next one appended to result
            result.append(wordlist[i+1])
    return result

def filter_negative(alist):
    '''
    :param alist: a (possibly empty) list of numbers
    :return:  a copy of alist(in order) without negative numbers
    '''
    copy=alist          # Make a copy
    length=len(copy)    # Get the length of it
    i=0                 # Set the counting(i)
    while(i<length):    # Start the loop
        if copy[i]<0:           # if the number is negative
            del copy[i]         # del it and length-1
            length=length-1
            i=i-1               # then counting(i)-1
        i=i+1           # Else counting(i)+1
    return copy         # Return the value

if __name__ == '__main__':
    '''
    s=["x","x","dog","x","car","x"]
    print(followers(s,'x'))

    temp=[1,-1,-2,3,0,-11,2,-3,1,-2,1,-2,1]
    print(filter_negative(temp))
    '''