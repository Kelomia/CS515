'''
 CS515 - Lab_6
@ author: Zimu Jiao
'''

from functools import *

def remove_dups(L):
    '''
    :param L: The list to modify
    :return: A COPY of L with adjacent duplicates removed.
    Example: L=[1,2,2,3,3,3,4,5,1,1,1]
        result=[1,2,3,4,5,1]
    '''
    temp = L[0]             # Set temp mark as L[0]
    i = 1                   # Begin loop at L[1]
    while i < len(L):
        if L[i] == temp:    # If current is duplicate to before one, del it
            del L[i]        # As the index -1 when the element del, i doesn't +1
        else:
            temp = L[i]     # Else, set temp mark as different element
            i = i + 1       # Then i +1
    return L                # Return L

def clamp(L,min,max):
    '''
    Any Number in list less than min is replaced with min.
    Any Number in list greater than max is replaced with max.
    Number between min and max will not change.
    :param L: List of integers/floats to modify
    :param min: The min set(int/float)
    :param max: The max set(int/float)
    :return:  The list after all change.
    Example: L=[-1,1,3,5], clamp(L,0,4), L=[0,1,3,4]
    '''
    i = 0                   # Begin loop at L[0]
    while i < len(L):
        if L[i] < min:      # When current element < min, replace it
            L[i] = min
        elif L[i] > max:    # When current element > max, replace it
            L[i] = max
        # When min < current < max, not change
        i=i+1               # i++
    return L                # Return L

def into(n,c):
    '''
    :param n: the number to analyse, n>=1 is an int.
    :param c: the number to divide by, c>1 is an int.
    :return: the number of times that c divides n
    Example: into(5,3) return 0 because 3 does not divide 5
             into(3*3*3*3*7,3)=4
    '''
    num_times=0                 # Assign num_times and set it as 0
    while(n%c==0):              # When c can divide n
        num_times=num_times+1   # num_times +1
        n=n/c                   # Renew n as n/c
    return num_times            # return num_times

"""
                    Def two function to help calculate x^n and n!
def factorial(n):
    '''
    :param n: an int, not minus.
    :return: the factorial of n, n!
    '''
    if(n>1):
        return n*factorial(n-1)
    else:
        return 1

def power(x,n):
    '''
    :param x: the base
    :param n: the power
    :return: x^n
    '''
    if(n>1):
        return x*power(x,n-1)
"""

def exp(x):
    '''
    :param x:  the exponential value, x>=1 is an int
    :return:  return approximation of sum, which is the sum of x^n/n! from 0 to n, stop when meet error value.
    e^x=sum(1+x++x^2/2...+x^n/n!
    Example: None
    '''
    sum=1.0       # Assign sum, as 0
    n=1.0         # Set the n, begin at 1
    term=1.0      # Set the turn number as 1, because x^n/n!=1 when n=0:x^0/0!==1/1==1
    '''
    term,sum,n=1,1,1
    float(x)
    while n<=100:
        term=term*x/n   {new term=term*x/n}
        sum=sum+term
        n=n+1
        (condition):break
    '''
    while True:
        '''
        Loop
        e_x =int(power(x,n))/int(factorial(n))
        e^x==x^n/n!==x/1*x/2*x/3*...*x/n
        '''

        flag=term           # Set last term as flag
        term=term*(x/n)     # Calculate the next term.
        sum = sum + term    # Add term to sum
        n=n+1               # n++"
        if(abs(term)<1e-10):       # Check how great the term is, if it's smaller than 1e-10, stop the loop.
            break                  # Break loop
    return sum


if __name__ == '__main__':
    '''
    L=[1,2,2,3,3,3,4,5,1,1,1]
    S=[-4.,3.,1.,-10.,22.,15.,3.,1.]
    print("now the L is\n\t",L)
    print(remove_dups(L))
    print("now the S is\n\t",S)
    print(clamp(S,0,5))
    
    print(into(3*3*3*3*7,3))
    
    n=3
    print('e^',n," is",exp(n))
    '''