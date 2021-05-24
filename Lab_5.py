'''
 CS515 - Lab_5
@ author= Zimu Jiao
'''
from functools import *

def sum__list(thelist):
    sum=0
    if(len(thelist)==0):
        return 0

    for num in thelist:
        sum=sum+num
    return sum

def reverse(s):
    if s=='':
        return ''
    '''
    rev_s=''
    for ch in s:
        rev_s=ch+rev_s
    '''
    rev_s=reduce(lambda x,y:y+x,s)
    return rev_s

def remove_dups(thelist):
    if len(thelist)<=1:
        return thelist

    if thelist[0] == thelist[1]:
        del thelist[1]
        return remove_dups(thelist)
    else:
        thelist[1:]=remove_dups(thelist[1:])
        return thelist

def into(n,c):
    count=0
    while(n%c==0):
        n=n//c
        count=count+1
    return count

if __name__ == '__main__':
    print(sum__list([]))
    print(sum__list([1, 2, 3]))

    print(reverse(''))
    print(reverse('abc'))

    print(remove_dups([1, 2, 2, 3, 3, 3, 4, 5, 1, 1, 1]))
    print(remove_dups([1, 2, 2, 3]))

    print(into(3*9*9*7,3))
    print(into(12,3))