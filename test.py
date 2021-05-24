'''
test.py
'''

import random


def partition(b, h, k):
    '''
    :param b: The list to sort
    :param h: The left index
    :param k: The right index
    :return: The pivot index: i
    '''
    i = h;
    j = k + 1;
    x = b[h]
    while i < j - 1:
        if b[i + 1] >= x:
            swap(b, i + 1, j - 1)
            j = j - 1
        else:
            swap(b, i, i + 1)
            i = i + 1
    return i


def swap(b, i, j):
    print(b[i],b[j]," will be changed")
    temp=b[i]
    b[i]=b[j]
    b[j]=temp


def quick_sort(list, left, right):
    if len(list) < 2:
        return list
    # j is the pivot
    pivot = partition(list, left, right)
    return quick_sort(list, left, pivot - 1)+[pivot]+quick_sort(list, pivot + 1, right)


def random_numbers_generator(num=1000, min=9, max=10000):
    '''
    :param num: int
    :param min: int
    :param max: int, bigger than num
    :return: return num of random elements
    '''
    list = []
    for i in range(num):
        list.append(random.randint(min, max))
    return list


if __name__ == '__main__':
    list = random_numbers_generator(10, 0, 50)
    print(list)
    sorted_list=quick_sort(list, 0, 20)
