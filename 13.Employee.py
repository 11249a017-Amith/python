.class Employee:
    def __init__(self, emp_id, name, dept, salary):
        self.id = emp_id
        self.name = name
        self.dept = dept
        self.salary = salary
    def update_salary(self, new_salary):
        self.salary = new_salary
emp = Employee(1, "Jithu", "AI&DS", 1000)
emp.update_salary(2000)
print(emp.id, emp.name, emp.dept, emp.salary)
