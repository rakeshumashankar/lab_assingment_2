#lab_assingment_2
class Employee:
    def _init_(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

    def _repr_(self):
        return f"{self.employee_id} {self.name} {self.age} {self.salary}"

def sort_employees(employees, sort_by):
    if sort_by == 1:
        employees.sort(key=lambda x: x.age)
    elif sort_by == 2:
        employees.sort(key=lambda x: x.name)
    elif sort_by == 3:
        employees.sort(key=lambda x: x.salary, reverse=True)
    else:
        raise ValueError("Invalid sorting parameter")

# Example usage
employees = [
    Employee("161E90", "Ramu", 35, 59000),
    Employee("171E22", "Tejas", 30, 82100),
    Employee("171G55", "Abhi", 25, 100000),
    Employee("152K46", "Jaya", 32, 85000),
]

print("Choose the sorting parameter:")
print("1. Age")
print("2. Name")
print("3. Salary")

sort_by = int(input("Enter the sorting parameter (1/2/3): "))

sort_employees(employees, sort_by)
print("\nSorted employees:")
for employee in employees:
    print(employee)