'''
 CS515 - hw4
@ author: Zimu Jiao
'''

class Date:
    # Q1: __init__(self,month,day,year):
    def __init__(self,month,day,year):
        '''
        :param month: Month
        :param day: Day
        :param year: Year
        '''
        self.month=month
        self.day=day
        self.year=year
        '''
        If check the input, can use the dictionaries in tomorrow():
        if day>n_month[month] or l_month[month]:
            self.day=n_month[month] or l_month[month]
        '''

    # __str(self):
    def __str__(self):
        '''
        :return: Month/Day/Year
        '''
        return "%d/%d/%d"%(self.month,self.day,self.year)

    # Q3: method isLeapYear(self):
    def isLeapYear(self):
        '''
        :return: if the Year is leap.
        '''
        if self.year%100 == 0 and self.year%400 != 0:
            return False
        if self.year%4 == 0:
            return True
        return False

    # Q3: method tomorrow(self):
    def tomorrow(self):
        '''
        :return: The next day of Month/Day/Year
        '''

        # Using dictionary to find the next day's value:
        n_Month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        l_Month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        self.day=self.day+1
        if self.isLeapYear():
            # If it's leap year, check day with lear year dictionary:
            if self.day > l_Month[self.month]:
                self.day=1
                self.month=self.month+1
        else:
            # Else, check day with non-leap year dictionary:
            if self.day > n_Month[self.month]:
                self.day=1
                self.month=self.month+1
        if self.month>12:
            self.month=1
            self.year=self.year+1

    # Q4: method isBefore(self,d2):
    def isBefore(self,d2):
        '''
        :param d2: An object of Date
        :return: if self is before d2.
        '''
        if self.year<d2.year:
            # If smaller year:
            return True
        elif self.year==d2.year:
            # Else, if smaller month:
            if self.month<d2.month:
                return True
            elif self.month==d2.month:
                # Else, if smaller day:
                if self.day<d2.day:
                    return True
        # Else, return False.
        return False


# Test:
if __name__ == '__main__':
    d=Date(3,14,2012)
    d2=Date(3,15,2012)
    d3=Date(1,2,1900)
    print("d1:",str(d),"d2:",str(d2),"d3:",str(d3))
    print("d1 Leap-year:",d.isLeapYear())
    print("d2 Leap-year:",d2.isLeapYear())
    print("d3 Leap-year:",d3.isLeapYear())

    print("d1:",str(d),"d2:",str(d2))
    print(d.isBefore(d2))

    d.tomorrow()
    print("d1:", str(d), "d2:", str(d2))
    print(d.isBefore(d2))