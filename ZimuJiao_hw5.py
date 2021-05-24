'''
 CS515 - hw5
@ author: Zimu Jiao
'''
import random
import time

def random_numbers_generator(num=1000,min=9,max=10000):
    '''
    :param num: int
    :param min: int
    :param max: int, bigger than num
    :return: return num of random elements
    '''
    list=[]
    for i in range(num):
        list.append(random.randint(min,max))
    return list

def insertion_sort(random_list):
    '''
    :param random_list: list of elements
    :return: random_list and sorted_list
    '''
    sorted_list=random_list[:]
    for i in range(0,len(sorted_list)):
        j=i-1
        current=sorted_list[i]
        while j>=0 and sorted_list[j]>current :
            sorted_list[j+1]=sorted_list[j]
            j-=1
        sorted_list[j+1]=current

    return random_list, sorted_list


def partition(b,h,k):
    '''
    :param b: The list to sort
    :param h: The left index
    :param k: The right index
    :return: The pivot index: i
    '''
    i=h;
    j=k+1;
    x=b[h]
    while i<j-1:
        if b[i+1]>=x:
            swap(b,i+1,j-1)
            j=j-1
        else:
            swap(b,i,i+1)
            i=i+1
    return i

def swap(b,i,j):
    b[i],b[j]=b[j],b[i]
    return b

'''
def quick_sort(b,h,k):
    if len(b)<2:
        return b
    # j is the pivot
    j=partition(b,h,k)
    quick_sort(b,h,j-1)
    quick_sort(b,j+1,k)
'''

# The first_quick_sort:

def partition_random(list,left,right):
    pivot=random.randint(left,right)
    j = right + 1;
    x = list[pivot]
    while pivot < j - 1:
        if list[pivot + 1] >= x:
            swap(list, pivot + 1, j - 1)
            j = j - 1
        else:
            swap(list, pivot, pivot + 1)
            pivot = pivot + 1
    return pivot

def Quick_sort_first(random_list):
    length=len(random_list)
    if length<2:
        return random_list

    pivot=partition(random_list,0,length)
    Quick_sort_first(random_list[0:pivot-1])
    Quick_sort_first(random_list[pivot+1,length])

def Quick_sort_random(random_list):
    length=len(random_list)
    if length<2:
        return random_list

    pivot=partition_random(random_list,0,length)
    Quick_sort_random(random_list[0:pivot-1])
    Quick_sort_random(random_list[pivot+1,length])
'''
def Quick_sort_first(random_list):
    # Previous version:
    
    list=random_list[:]
    length=len(list)

    if length<=1:
        return list

    pivot = list[0]
    Smaller = []
    Bigger = []
    for i in range(1,length):
        if list[i] < pivot:
            Smaller.append(list[i])
        else:
            Bigger.append(list[i])
    return Quick_sort_first(Smaller) + [pivot] + Quick_sort_first(Bigger)

def Quick_sort_random(random_list):
    # Previous version:
    
    list=random_list[:]
    length = len(list)

    if length < 2:
        return list

    index=random.randint(0,length)
    pivot = list[index]
    Smaller = []
    Bigger = []
    for i in range(0, length):
        if i == index:
            continue
        if list[i] < pivot:
            Smaller.append(list[i])
        else:
            Bigger.append(list[i])

    return Quick_sort_first(Smaller) + [pivot] + Quick_sort_first(Bigger)
'''
# Test:
if __name__ == '__main__':
    Start = time.time()
    Random_list = random_numbers_generator(num=1000, max=100000 * 10)
    print("Generating random list, time:{}".format(time.time() - Start))

    Start = time.time()
    sorted_list = Quick_sort_first(Random_list)
    print("Sort random list by Quick sort using the first as pivot, time:{}".format(time.time() - Start))

    Start = time.time()
    sorted_list = Quick_sort_random(Random_list)
    print("Sort random list by Quick sort using a random as pivot, time:{}".format(time.time() - Start))

'''
    Start = time.time()
    sorted_list = insertion_sort(Random_list)
    print("Sort random list by Insertion sort, time:{}".format(time.time() - Start))
'''