'''
Homework-2-CS515
author Zimu Jiao
'''

'''
Q1: dot(L,K):   Return the sim of dot product of to list, if the length of two list are different, the result is option-
                -al,
                Assume the length are equal. And the output should be 0.0 when two list are empty
                Example: dot([5,3],[6,4])=> 5*6+3*4=12
Q2: explore(S): Take a string S and return a list of characters in string.
                Example: explore("spam")=> ['s','p','a','m']       explore("")=> []
Q3: ind(e,L):   Take an element e and a sequence L(List or Sting), return the index of first e in L. Begin at 0.
                If e is not in L, return the length of L.
                Example: ind(42,[55,77,42,12,42,100])=> 2
                         ind(42, range(0,100))=> 42
                         ind('hi',['hello',42,True]=> 3
                         ind(' ','outer exploration')=> 5
Q4: deepReverse(L):
                List as input, return the reverse.
                Example: deepReverse([1,2,3])=> [3,2,1]
                         deepReverse([1,[2,3],4])=>[4,[3,2],1]
                         deepReverse([1,[2,[3,4],[5,[6,7],8]]])=> [[[8,[7,6],5],[4,3],2],1]
                
                if isinstance(x,list):
                    # if True
                else:
                    # if False
'''
import types
def dot(L,K):
    '''
    :param L: list of integer;
    :param K: list of integer;
    L and K should have same length.
    :return: the dot product of L and K, if the length of them are not equal, the result will be depend on the shorter
    one.
    '''
    if(L==[] or K==[]):     # When K or L is empty, set sum = 0.0 and return sum.
        sum=0.0
        return sum
    if(L[1:]==[] or K[1:]==[]):             # When K or L will end up next turn, the sum end at this turn;
        sum=L[0]*K[0]
    else:
        sum=L[0]*K[0]+dot(L[1:],K[1:])      # Or the sum will calculate the next turn.
    return sum

def explore(s):
    '''
    :param s: String s
    :return: A list of each element in s
    '''
    result=[]
    if(s!=""):      # When String is not empty:
        result.append(s[0])     # Add the first char to result, the return_list
        if(s[1:]!=""):          # If String s is more than 2 char, do the recursion by shorten it 1.
            return result+explore(s[1:])
        else:
            return result       # Or end up.

def ind(e,L):
    '''
    :param e: An element, can be integer, char, string
    :param L: A list
    :return: If e in L, return its index; else return the length of L.
    Notice: Since the type of range()'s return is not a list, if e is out of L from range(), the result will be error
    '''
    count=0
    if(e==L[0]):    # When the e is found in L, return the count
        return count
    else:           # When e is not found yet, count +1
        count=count+1
        if(L[1:]==[]):  # When e is not in L, return the count, which now equal to L-list's length.
            return count
        else:           # When e is not found count, recurse- in L[1:] to find e.
            count=count+ind(e,L[1:])
            return count


def deepReverse(L):
    '''
    :param L: A list
    :return:  A list of reversed L, if elements in L are list, that list will be reversed.
    '''
    newL=[]
    for item in L[::-1]:            # Check list from the end to head.
        if isinstance(item,list):   # Check if item is list:
            item=deepReverse(item)  # Yes: Set it as reversed.
        newL.append(item)           # Add it to the new List.
    return newL


if __name__ == '__main__':
    A=[]
    A1=[2,3]
    B=[2,4]
    print(dot(A,B))
    print(dot(A1,B))
    s="Hello world!"
    print(explore(s))
    print(ind(3,range(0,9)))
    L1=[1,2,3]
    L2=[1,[2,3],4]
    L3=[1,[2,[3,4],[5,[6,7],8]]]
    print(deepReverse(L1))
    print(deepReverse(L2))
    print(deepReverse((L3)))
