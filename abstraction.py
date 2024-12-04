class employee:
    count=0
    def __init__ (self):
        employee.count=employee.count+1
    def display(self):
        print("the number of employees",employee.count)
emp=employee()
emp2=employee()
try:
    print(emp.count)
finally:
    emp.display()                
