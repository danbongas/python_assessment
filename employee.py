from datetime import datetime,date


class Employee(object):
    empCount = 0

    def __init__(self,first_name,last_name,birthday,date_employment):
       self.first_name = first_name
       self.last_name = last_name
       self.birthday = birthday
       self.date_employment = date_employment        
       Employee.empCount += 1 

    def ShowUser(self):
   	    print("Birthday: ", self.birthday)
   	    print("Employment: ", self.date_employment)

    def Eligibilty(self):
        today = date.today()
        bday = self.birthday
        print( today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day)))
        age = calculate_age(bday)
        print(age)

def main():

    print("Enter an Employee Details :\n")
    fname = input("Enter First Name :")
    lname = input("Enter Last Name :")
    #BIRTHDATE 
    date_entry = input('Enter a date in YYYY-MM-DD format for your brithday')
    year, month, day = map(int, date_entry.split('-'))
    bday = datetime.date(year, month, day)  
    #EMPLOYEMENT
    employment_date = input('Enter a date in YYYY-MM-DD format for your employement date')
    emp_year, emp_month, emp_day = map(int, employment_date.split('-'))
    emp_date = datetime.date(emp_year,emp_month,emp_day)
    emp = Employee(fname,lname,bday,emp_date)
    emps[emp.lname] = emp
    emp.ShowUser()
    print("Total Users Available :\n",len(emps))
    lst.append(Employee(fname,lname,bday,emp_date)) 


emps = {}
lst = []
main()