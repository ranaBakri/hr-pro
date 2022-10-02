# Rana Bakri
# Assessment 3 2/10/2022
class Employee:
    def __init__(self, name,age,salary,employment_years):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_years = employment_years

    def __str__ (self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.employment_years}"

    def get_annual_salary(self):
        return int(self.salary)*12

    

# super().__init__(name, attitude, behaviour, face)
class Manager(Employee):
    def __init__(self,name, age, salary,employment_years,bonus_percentage):
     super().__init__(name, age, salary,employment_years)
     self.bonus_percentage = bonus_percentage

    def __str__ (self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.employment_years}, Bonus:{self.bonus_percentage}"
     

    def get_bonus(self):
        return int(self.bonus_percentage)*int(Employee.salary)

# Show Employees
# 	2. Show Managers
# 	3. Add An Employee
# 	4. Add A Manager
# 	5. Exit
#Create a list of Employee objects for non-managerial employees, and a list of Manager objects for managers.
emp1 = Employee("rana",37,400,2103)
emp2 = Employee("Nasser",40,450,2020)
emp3 = Employee("Ahmad",22,350,2021)
emp4 = Employee("Jassem",29,300,2019)

Employee_object=[emp1,emp2,emp3,emp4]

manager1 = Manager("layla", 25, 700,2020,20)
manager2 = Manager("Hamad", 37, 1000,2020,20)
manager3 = Manager("Mohammad", 40, 1400,2020,20)
manager4 = Manager("Khaled ", 45, 1800,2020,20)

Manager_objects=[manager1,manager2,manager3,manager4]



Employee_show =["Show Employee","Show Managers","Add An Employee","Add A Manager","Exit"]

def show_Employee(Employee_show):
    print()
    print("Options")

    for idx, emp in enumerate(Employee_show, start=1):
        print(f"{idx}. {emp}")


print("Welcome to HR Pro")
show_Employee(Employee_show)
input1=int(input("What would you like to do?   "))
print("-----------------------------------------")
 
def add_employee(Employee_object):
    name = input("enter name:  ")
    print(name)
    age = int(input ("enter age:  "))
    salary = int(input("enter salary:  "))
    years = int(input ("enter years:  "))
    emp5 = Employee(name,age,salary,years)
    Employee_object.append(emp5)
    return  emp5


def add_manager(Manager_objects):
    name = input("enter name:  ")
    print(name)
    age = int(input ("enter age:  "))
    salary = int(input("enter salary:  "))
    years = int(input ("enter years:  "))
    Bounas = int(input("enter bounas"))
    manager5 = Manager(name,age,salary,years,Bounas)
    Manager_objects.append(manager5)
    return  manager5



if input1 == 1:
                for emp in Employee_object:
                    print (emp)
elif input1 == 2:
                for manager in Manager_objects:
                    print (manager)
elif input1 == 3:
                print("Employee added succesfully")
                print(add_employee(Employee_object))
elif input1 == 4:
                print("Manager added succesfully")
                print(add_manager(Manager_objects))
else:
                
                exit()




        
def main():
	# main code here

 if __name__ == '__main__':
  main()
