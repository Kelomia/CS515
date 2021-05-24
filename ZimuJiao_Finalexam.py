'''
CS-515
Final Exam
@author: Zimu Jiao
'''

#------------------------------------------------Question 2--------------------------
def sum_matrix(matrix1, matrix2):
    """
    Returns: new matrix that is sum of matrix1 and matrix2.
    Precondition: matrix1 and matrix2 are matrices with the same dimension
    """
    # Get each list
    line1m1 = matrix1[0]
    line2m1 = matrix1[1]

    line1m2 = matrix2[0]
    line2m2 = matrix2[1]

    # Sum one by one and combine as a 2D_list, result:
    result=[[line1m1[0]+line1m2[0],line1m1[1]+line1m2[1]],[line2m1[0]+line2m2[0],line2m1[1]+line2m2[1]]]
    return result

#------------------------------------------------Question 3--------------------------

class Product(object):
    """
    An instance represents an item that can be sold.
    """
    SALES_TAX_RATE = 0.06

    def __init__(self, name, price, quantity, tax_exempt):
        """A new product item called "name" with 4 attributes:
        name: a non-empty  str, e.g., 'Milk'
        price: a float > 0.0
        quantity: a non-negative (but possibly 0) int
           indicating how many of these items are in stock
        tax_exempt: a bool indicating whether sales tax is added to the
           purchase price of this item
        """
        assert(name!="" and price>0.0 and quantity>=0 and isinstance(tax_exempt,bool))
        self.name = name
        self.price = price
        self.quantity=quantity
        self.tax_exempt = tax_exempt

    def __str__(self):
        """
        Returns: a [str] representation of the Product
          including all 4 attributes separated by commas, in a string form.
        The price should have a dollar sign.
        Don't worry about extending the price to exactly 2 decimal places.
        Example: "Milk, $3.0, 10, True"
        """
        return "%s, $%.1f, %d, %s"%(self.name,self.price,self.quantity,str(self.tax_exempt))

    def __eq__(self, other):
        """
        Returns: True if other is a Product, and both self and other have the same
        name, price, tax-exempt status, false otherwise.
        """
        if isinstance(other,Product):
            if self.price == other.price and self.name == other.name and self.tax_exempt == other.tax_exempt:
                return True
            else:
                return False

#------------------------------------------------Question 5--------------------------
class Person(object):
    """ A class representing a person in a 1-parent world.
    """

    def __init__(self, first, last, parent):
        """
        Creates a new Person with 3 instance attributes.
        first: non-empty str of letters
        last: non-empty str of letters
        parent: a Person or None
        """
        self.first = first
        self.last = last
        self.parent = parent
"""
Define the subclass Student below which has all three attributes above and 1 extra attribute UID

UID is a string that is created at initialization by concatenating 3 things:

(1) the lower-case first letter of the first name
(2) the lower-case first letter of the last name
(3) a unique number across all students representing when the Student was created in the university

UID should be initialized within __init__(). 
"""
class Student(Person):
    count=0

    def __init__(self,first,last,parent):
        Person.__init__(self,first,last,parent)
        Student.count += 1
        self.UID=self.first[0].lower()+self.last[0].lower()+str(self.count)





if __name__ == '__main__':
    '''
    Q2:
    m1=[[1.0,2.0],[3.0,-4.0]]
    m2=[[1.5,0.0],[0.0,1.5]]
    print(sum_matrix(m1,m2))
    
    Q3:
    p1=Product("Milk",3.0,20,True)
    p2=Product("Milk",3.0,20,False)
    print(str(p1),str(p2))
    print(p2.__eq__(p1))
    
    Q5:
    s1=Student("Jason","Mike","a")
    s2=Student("Mike","Mia","b")
    s3=Student("Peter","Sombra","a")

    print(s3.UID)
    '''