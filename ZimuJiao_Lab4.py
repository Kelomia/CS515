'''
Lab4-homework-cs515
@ author: Zimu Jiao
'''

import introcs

def convert_time(alist):
    sum=alist[-1]
    if len(alist)>1:
        sum=sum+alist[-2]*60
        if len(alist)>2:
            sum=sum+alist[-3]*3600
            if len(alist)>3:
                sum=sum+alist[-4]*3600*24
    return sum

def last_name_first(n):

    end_first=n.find(' ')
    start_last=n[::-1].find(' ')    # Using reverse String to locate the start of last name.
    first=n[:end_first]
    last=n[len(n)-start_last::]     # Get the last name part with "start_last"

    name=first+' '+last
    introcs.assert_equals(n,name)

    return last+', '+first

if __name__ == "__main__":
    print(last_name_first("Jason Albert"))
    print(last_name_first("Jason Big Cat"))

'''
def sortnum(alist):
    length=len(alist)
    for i in range(length):
        for j in range(i+1,length):
            if alist[i]>=alist[j]:
                temp=alist[i]
                alist[i]=alist[j]
                alist[j]=temp
    return alist
    #Since the len of alist is three, the loop can be simplified as compare 0/-1(0/2) and 1/-1(1/2)
'''

def sortnum(alist):
    if alist[0]>alist[-1]:
        temp = alist[0]
        alist[0] = alist[-1]
        alist[-1] = temp
    if alist[1]>alist[-1]:
        temp = alist[1]
        alist[1] = alist[-1]
        alist[-1] = temp
    return alist

# ----------------------------Challenge Part
'''
------------------------------------------------------------------
--------------------- The above is my version of anglicize(n)-----
------------------------------------------------------------------

def turnNtoA(number):
    if number==1:
        str='one '
    elif number==2:
        str='two '
    elif number==3:
        str='three '
    elif number==4:
        str='four '
    elif number==5:
        str='five '
    elif number==6:
        str='six '
    elif number==7:
        str='seven '
    elif number==8:
        str='eight '
    elif number==9:
        str='nine '
    return str

def turnNtoA10(number):
    if number==2:
        str='twenty '
    elif number==3:
        str='thirty '
    elif number==4:
        str='forty '
    elif number==5:
        str='fifty '
    elif number==6:
        str='sixty '
    elif number==7:
        str='seventy '
    elif number==8:
        str='eighty '
    elif number==9:
        str='ninety '
    return str

def anglicize(n):
    str1=str2=str3=''
    num1=n%10
    num2=n%100//10
    num3=n//100

    str3 = turnNtoA(num3)

    if num2==1:
        if num1 == 1:
            str1 = 'eleven'
        elif num1 == 2:
            str1 = 'twelve'
        elif num1 == 3:
            str1 = 'thirteen'
        elif num1 == 4:
            str1 = 'fourteen'
        elif num1 == 5:
            str1 = 'fifteen'
        elif num1 == 6:
            str1 = 'sixteen'
        elif num1 == 7:
            str1 = 'seventeen'
        elif num1 == 8:
            str1 = 'eighteen'
        elif num1 == 9:
            str1 = 'nineteen'
    else:
        str2 = turnNtoA10(num2)
        str1 = turnNtoA(num1)
    return str3+"hundred "+str2+str1

#---------------------------------------------------------
#--------------Above is my version of anglicize(n) -------
#---------------------------------------------------------
'''

def anglicize(n):
    """
       Examples:
           3:      "three"
           45:     "forty five"
           100:    "one hundred"
           127:    "one hunded twenty seven"
       Returns: English equiv of n.

       Parameter: the integer to anglicize
       Precondition: n in 1..999
       """
    #####Your code#####
    if n>0 and n<20:
        return anglicize1to19(n)
    elif n<100:
        return anglicize20to99(n)
    elif n<999:
        return anglicize100to999(n)


def anglicize1to19(n):
    """
    Returns: English equivalent of n.

    Parameter: the integer to anglicize
    Precondition: n in 1..19
    """
    if n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'
    elif n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelve'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'

    # n = 19
    return 'nineteen'


def anglicize20to99(n):
    """
    Returns: English equiv of n.

    Parameter: the integer to anglicize
    Precondition: n in 20..99
    """
    ten=tens(n//10)
    unit=anglicize1to19(n%10)

    return ten + unit
    #####Your code#####


def anglicize100to999(n):
    """
    Returns: English equiv of n.

    Parameter: the integer to anglicize
    Precondition: n in 100..999
    """
    # Anglicize the first three digits

    hundreds = n % 100
    suffix = anglicize(hundreds)

    #####Your code#####
    if hundreds == 1:
        str = 'one '
    elif hundreds == 2:
        str = 'two '
    elif hundreds == 3:
        str = 'three '
    elif hundreds == 4:
        str = 'four '
    elif hundreds == 5:
        str = 'five '
    elif hundreds == 6:
        str = 'six '
    elif hundreds == 7:
        str = 'seven '
    elif hundreds == 8:
        str = 'eight '
    elif hundreds == 9:
        str = 'nine '

    return anglicize1to19(n // 100) + ' hundred ' + suffix

def tens(n):
    """
    Returns: tens-word for n

    Parameter: the integer to anglicize
    Precondition: n in 2..9
    """
#####Your code refer to anglicize1to19(n) #####
    if n == 2:
        str = 'twenty '
    elif n == 3:
        str = 'thirty '
    elif n == 4:
        str = 'forty '
    elif n == 5:
        str = 'fifty '
    elif n == 6:
        str = 'sixty '
    elif n == 7:
        str = 'seventy '
    elif n == 8:
        str = 'eighty '
    elif n == 9:
        str = 'ninety '
    return str


