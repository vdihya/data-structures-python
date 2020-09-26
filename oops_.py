import math
class circle:
    radius = 0.0 #declare as __radius if private member
    def a(self,r):
        self.radius = r
        area = math.pi*self.radius*self.radius
        cir = math.pi*2*self.radius
        print("area= ",area) #print("area = %.3f" %area)
        print("circumference=",cir)

c = circle()
c.a(12) 

class student: 
    # __rollno = 0
    #__name = ""
    # __marks = ""
    __num = 0
    def __init__ (self): # use init only to pass and instantiate variables directly as user input: self.radius = radius 
        self.__rollno = input("Enter the students' roll number= ")
        self.__name = input("Enter the students' name= ")
        student.__num +=1
        #self.__marks = input("Enter the students' marks= ")
   
    def printdetails(self):
        print("Name: ",self.__name)
        print("Roll no: ",self.__rollno)
        print("number of students = ",student.__num)
        print("studentdoc= ",student.__doc__)        #print("Marks: ",self.__marks)
        print("studentdict= ",student.__dict__)
        print("studentname= ",student.__name__)
        print("studentmod= ",student.__module__)
        print("studentbase= ",student.__bases__)
 
    """def float calcavg():
        self.m1 = input("Enter marks for subject 1= ")
        self.m2 = input("Enter marks for subject 2= ")
        float(self.avg) = (float(self.m1) + float(self.m2)/2.0
        return self.avg """   

stu = student()
stu.printdetails()
#print(stu.calcavg()) 
"""BUILT IN CLASS ATTRIBUTES:
    __dict__ : dictionary containing the class' namespace
    __doc__  : class documentation string or none
    __name__ : class name
    __module__ :module name in which the class is defined
    __bases__ :A possibly empty tuple containing base classes, in the order of occurence in the base class list """

""" __del__() is a destructor that prints to name of the class of an instance that is about to be destroyed"""
class complex:
    def __init__(self,r=0,i=0):
        self.r = r
        self.i = i

    def __del__(self):
        class_name = self.__class__.__name__ #??? 
        print(class_name," destroyed")

num = complex()

""" DATA HIDING """
class counter:
     __secretcounter = 0
     def count(self):
         self.__secretcounter += 1
         print(self.__secretcounter)

c = counter()
c.count()
#print(c.__secretcounter)
print(c._counter__secretcounter)

""" formal and informal representation str(variable) = 'variable' repr(variable) = " """ 

""" INHERITANCE """
class parent:
    parentattribute = 100
    def __init__(self):
        print("calling parent constructor")
    def parentmethod(self):
        print("calling the parent method")
    def setattr(self,attr):
        parent.parentattribute = attr 
    def getattr(self):
        print("parent attribute:",parent.parentattribute)

class child(parent):
    def __init__(self):
        print("calling child constructor")
    #super(child,self).__init__()
    def childmethod(self):
        print("calling child method")
# class childchild(child,parent)


""" when base and child class have same function signatures, the child class overwrites it and has superiority """
c = child()
c.childmethod()
c.parentmethod()
c.setattr(100)
c.getattr()

""" aggregation: making an object available in another object 
    if the life time of an object is aligned with a parent object then it's called composition"""

""" method overloading/POLYMORPHISM """
""" raise NotImplementedError """
