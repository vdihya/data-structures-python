

from datetime import date
import datetime
import re


class Student:
    def __init__(self, marks=None):
        self.marks = marks if marks != None else []

    def add_marks(self, lst):
        self.marks.extend(lst)


s1 = Student(marks=[45, 32, 37])
s2 = Student(marks=[28, 34, 42])

s1.add_marks([33, 27, 31])

print(s1.marks)
print(s2.marks)


class Person:

    def __init__(self, usn='', name='', dob=None, gender=''):
        if self.validate_usn(usn) and self.validate_dob(dob):
            self.usn = usn
            self.dob = datetime.datetime.strptime(dob, '%d/%m/%Y').date()
        else:
            raise Exception(
                "Objection Creation failed due to invalid USN/DoB.")

        self.name = name
        self.gender = gender
        self.age = self.calculate_age()

    def __str__(self):
        return f"{self.usn} {self.name} {self.dob} {self.gender[0]} \n"

    def validate_usn(self, usn):
        res = re.findall(
            '1CR1[0-9](CS|IS|CV|ME|TE|EC|EE)[0-9][0-9][0-9]$', usn)
        #print("usn val " ,res)
        if res:
            return True
        else:
            return False

    def validate_dob(self, dob):
        res = re.findall("([0-9]{1,2}[/]){2}[0-9]{4}", dob)
        if res:
            # self.dob=datetime.datetime.str
            return True
        else:
            return False

    def calculate_age(self):
        # calculate and extract from timedelta object or by calculating difference between years
        now = date.today()
        # datetime.datetime.strptime(self.dob,'%d/%m/%Y').date()
        birth = self.dob
        return (now-birth).days//365

    def get_age(self):
        """ return age """
        return self.age

    def time_to_bday(self):

        today = date.today()
        if today.month <= self.dob.month:
            #print("This year")
            no_of_days_to_bday = self.dob.replace(year=today.year)-today

        else:
            #print("Next year")
            no_of_days_to_bday = self.dob.replace(year=today.year+1)-today

        return no_of_days_to_bday.days


class Student(Person):
    def __init__(self, usn, name, dob, gender, branch, year, ma):
         #""" call superclass init and pass usn, name dob, gender """
         #""" assign branch year and MA"""
        super().__init__(usn, name, dob, gender)
        self.year = year
        self.branch = branch
        self.ma = ma if type(ma) is MA else print(
            "ma object is of incompatible type.")

    def __str__(self):
        return super().__str__() + self.ma.__str__()


class MA:
    max_marks = 80  # for each subject
    max_classes = 62  # for each class

    def __init__(self, subject_list, marks_list, att_list):

        if len(subject_list) == len(marks_list) == len(att_list):
            self.marks_dict = dict(zip(subject_list, marks_list))
            self.att_dict = dict(zip(subject_list, att_list))
            self.marks = self.calculate_avg_marks()
            self.att = self.calculate_avg_att()
        else:
            raise Exception("Incompatible list shapes in MA.")

    def __str__(self):
        res = ''
        for snm, m, a in zip(self.marks_dict.keys(), self.marks_dict.values(), self.att_dict.values()):
            res += f'{snm} : marks - {m}%, attendance - {a}%\n'
        return res

    def calculate_avg_marks(self):
        res = sum(self.marks_dict.values())/len(self.marks_dict.values())
        return res

    def calculate_avg_att(self):
        res = sum(self.att_dict.values())/len(self.att_dict.values())
        return res


# Driver Code
subject_lst = ['PYTHON', 'CD', 'CNS', 'CG']
marks_lst = [65, 60, 55, 50]
att_lst = [42, 50, 60, 58]

ma = MA(subject_lst, marks_lst, att_lst)
s = Student('1CR17CS001', 'Vidhya', '18/08/1999', 'F', 'CSE', 4, ma)

print(s)
print("Age", s.get_age())
print("Time to next birthday", s.time_to_bday())
