'''
 CS515 - Lab_8
@ author: Zimu Jiao
'''

# Q2:
class Address:
    def __init__(self,street,num):
        self.street_name=street
        self.number=num

class CampusAddress(Address):
    city_name = "Hoboken"

    def __init__(self,office_number):
        self.office_number=office_number

# Q3:
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length* self.width

'''
class Square:
    def __init__(self,length):
        self.length = length

    def area(self):
        return self.length*self.length
'''

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)

# Q4:
class Cube(Square):
    def volume(self):
        return self.length * super(Cube,self).area()


if __name__ == '__main__':
    # Q1: In *.pdf
    '''
    The results:
        s1 False
        s2 True
    '''
    # Q2:
    Sarina_addr=CampusAddress("111")
    print(Sarina_addr.office_number)
    print(Sarina_addr.city_name)

    # Q3:
    square = Square(4)
    print(square.area())

    # Q4:
    cube = Cube(3)
    print(cube.volume())