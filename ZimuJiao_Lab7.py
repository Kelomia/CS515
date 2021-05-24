'''
 CS515 - Lab_7
@ author: Zimu Jiao
'''

def divide(a,b):
    '''
    Example: divide(4,2), return 2
             divide(4.2,2), return None
             divide(4,0), return None
    :param a: an Int
    :param b: an Int
    :return:  a/b
    '''

    try:
        if not (isinstance(a,int) or isinstance(b,int)):
            return None
        return a/b
    except:
        #print("invalid input")
        return None


class Date(object):
    month=1
    year=2021
    day=1
    month_d={1:'January', 2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',
             10:'October',11:'November',12:'December'}

    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year

    def __str__(self):
        return "Date in form:%d/%d/%d %s %d"%(self.month,self.day,self.year,self.month_d[self.month],self.day)
    def getyear(self):
        return self.year
    def getmonth(self):
        return self.month
    def getday(self):
        return self.day

    def setyear(self,year):
        self.year=year
    def setmonth(self,month):
        self.month=month
    def setday(self,day):
        self.day=day


if __name__ == '__main__':
    print(divide(5,3))
    print(divide(4.5,3.0))
    print(divide(4,0))

    Date1 = Date(1, 1, 3000)
    Date1.getmonth()
    Date1.getyear()
    Date1.getday()

    Date1.setmonth(4)
    Date1.getmonth()

    Date1.setyear(2021)
    Date1.getyear()

    Date1.setday(6)
    Date1.getday()

    print(Date1)
