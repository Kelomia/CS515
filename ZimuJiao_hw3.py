'''
Homework-3-CS515
author: Zimu Jiao
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

from sys import getsizeof   # used to check how large the algorithm could solve
'''
By testing with giving String(Penguin, Smile and Five), which ratios are about 1.484, 1.328 and 1.016
And tested with myString, it's clear that there are more adjacent same 0/1 , the smaller ratio is.

About the largest number used to encode, I think it's the result of String="10"*32, because each 1/0 need 5 bit to
encode, it's 5+64*5=325.(Since it begin with 1, 5 0' are need at beginning.

'''

def ten2two(num):
    '''
    turn num from int to binary and fill it to length=Compressed_block_size;
    :param num: the number to transfer to binary number, which is not greater than 31.
    :return: a binary number with length=5
    '''
    binary=bin(num)
    S=""
    S=str(binary[2:]).zfill(COMPRESSED_BLOCK_SIZE)
    return S

def D_S(S,length):
    '''
    Divide String by length, could use to check string easy
    :param S: String to divide
    :param length: the length each divided part will be.
    :return: A divide string with parts' length
    '''
    newS=[]
    newS.append(S[0:length])
    A=S[length:]
    if len(A)>length:
        newS+=D_S(A,length)
    elif len(A)==0:
        return newS
    else:
        newS.append(A)
    return newS

def compress(S):
    '''
    :param S: A string to compress.
    :return:  The compressed string.
    '''
    record=[]
    current = 1
    count = 1

    if S[0]=="0":
        temp="0"
    else:
        record.append(["0",0])
        temp="1"
    while current < len(S):
        if S[current] == temp:  # When current is same as last one, count+1, move to next
            count += 1
            current += 1
        else:  # Else add Last-count to record-List. Reset count as 1, reset temp.
            record.append(["1" if temp == "1" else "0", count])
            count = 1
            current = current + 1
            temp = "1" if temp == "0" else "0"
        if count == MAX_RUN_LENGTH:
            record.append(["1" if temp == "1" else "0", MAX_RUN_LENGTH])    # When reach the max, record part.
            record.append(["1" if temp == "0" else "0", 0])                 # Record a part that 0 of 0/1
            count -= MAX_RUN_LENGTH
    record.append(["1" if temp == "1" else "0", count])
    str=""
    for item in record:
        str=str+ten2two(item[1])
    return str

def uncompress(C):
    '''
    :param C: The compressed String to uncompress. 
    :return: thr content.
    '''
    if((len(C)%5)!=0):
        print("ERROR")
        return False
    content=D_S(C,COMPRESSED_BLOCK_SIZE)        # length=COMPRESSED_BLOCK_SIZE+1
    result=""
    num="0"
    for element in content:
        temp=num*int(element[1:],2)
        result+=temp

        num="1" if num == "0" else "0"
    return result


def compression(S):
    '''
    Return the ratio of the compressed size to the original size for image/string S.
    :param S: the image/string to compress
    :return:  the ratio
    '''
    ratio=len(compress(S))/len(S)
    return ratio

if __name__ == '__main__':
    S1 = "00011000" + "00111100" * 3 + "01111110" + "11111111" + "00111100" + "00100100"
    S2 = "0" * 8 + "01100110" * 2 + "0" * 8 + "00001000" + "01000010" + "01111110" + "0" * 8
    S3 = "1" * 9 + "0" * 7 + "10000000" * 2 + "1" * 7 + "0" + "00000001" * 2 + "1" * 7 + "0"

    CS1=compress(S1)
    CS2=compress(S2)
    CS3=compress(S3)

    print("Penguin:")
    print(S1)
    print(uncompress(CS1))
    print(compress(S1))
    print("Separated by5\n",D_S(compress(S1),COMPRESSED_BLOCK_SIZE))

    print("Smile:")
    print(S2)
    print(uncompress(CS2))
    print(compress(S2))
    print("Separated by5\n",D_S(compress(S2), COMPRESSED_BLOCK_SIZE))

    print("Five:")
    print(S3)
    print(uncompress(CS3))
    print(compress(S3))
    print("Separated by5\n",D_S(compress(S3),COMPRESSED_BLOCK_SIZE))

    print("S1's ratio:", compression(S1), "\nS2's ratio:", compression(S2), "\nS3's ratio:", compression(S3))


    myS1="1"*64
    myS2="10"*32
    myS3="11111111"*2+"00010001"*2+"00000000"*2+"10000001"*2
    myS4="10000001"*4
    myS5="10010010"*4

    print(compress(myS1))
    print(compress(myS2))
    print(compress(myS3))

    print("myS1's ratio:", compression(myS1), "\nmyS2's ratio:", compression(myS2), "\nmyS3's ratio:", compression(myS3))
    print("myS4's ratio:", compression(myS4), "\nmyS5's ratio:", compression(myS5))