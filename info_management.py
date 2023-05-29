class Employee:
    def __init__(self, emp_id, name, department, position):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.position = position

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, department, position):
        employee = Employee(emp_id, name, department, position)
        self.employees.append(employee)

    def get_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                return employee
        
    def display_all_employees(self):
        if not self.employees:
            print("No employees in the database.")
        else:
            print("Employee Database:")
            for employee in self.employees:
                print(f"ID: {employee.emp_id}, Name: {employee.name}, Department: {employee.department}, Position: {employee.position}")    

database=EmployeeDatabase()

database.add_employee('science',1,'John','HR')
database.add_employee('management',2,'Jim','PR')
database.add_employee('customs',3,'tim','analytics')

database.display_all_employees()

        