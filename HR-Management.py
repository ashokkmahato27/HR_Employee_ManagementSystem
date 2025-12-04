#...HR Employee Management System
# Base Class
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.bonus = 0
    
    def calculate_salary(self):
        return 0
    
    def apply_bonus(self):
        return 0
    
    def get_details(self):
        return {
            "name": self.name,
            "department": self.department,
            "salary": self.calculate_salary(),
            "bonus": self.bonus
        }


# Full-Time Employee
class FullTime(Employee):
    def __init__(self, name, department, salary, rating):
        super().__init__(name, department)
        self.salary = salary
        self.rating = rating  # 1 to 5
    
    def calculate_salary(self):
        return self.salary
    
    def apply_bonus(self):      # Rating 5: 20%, Rating 4: 10%, else: 0%
        
        if self.rating == 5:
            self.bonus = self.salary * 0.20
        elif self.rating == 4:
            self.bonus = self.salary * 0.10
        else:
            self.bonus = 0
        return self.bonus


#...... Part-Time Employee
class PartTime(Employee):
    def __init__(self, name, department, hourly_rate, hours):
        super().__init__(name, department)
        self.hourly_rate = hourly_rate
        self.hours = hours
    
    def calculate_salary(self):
        return self.hourly_rate * self.hours
    
    def apply_bonus(self):           # More than 100 hours: 5% bonus
        if self.hours > 100:
            self.bonus = self.calculate_salary() * 0.05
        else:
            self.bonus = 0
        return self.bonus


# Intern 
class Intern(Employee):
    def __init__(self, name, department, stipend):
        super().__init__(name, department)
        self.stipend = stipend
        self.completed = False
    
    def calculate_salary(self):
        return self.stipend
    
    def complete(self):
        self.completed = True
    
    def apply_bonus(self):
        # $500 bonus if completed
        if self.completed:
            self.bonus = 500
        else:
            self.bonus = 0
        return self.bonus


# Create employees
employees = [
    FullTime("RAhul", "Engineering", 80000, 5),
    FullTime("Neha", "Marketing", 60000, 4),
    PartTime("Sonam", "Support", 25, 120),
    PartTime("Ranjan", "Sales", 30, 80),
    Intern("Ashok", "IT", 2000),
    Intern("Abhishek", "HR", 1500)
]

# Complete one intern
employees[4].complete()

# Apply bonuses and display
print("=" * 50)
print("EMPLOYEE DETAILS")
print("=" * 50)

total_salary = 0
total_bonus = 0

for emp in employees:
    emp.apply_bonus()
    details = emp.get_details()
    
    print(f"\nType: {emp.__class__.__name__}")
    print(f"Name: {details['name']}")
    print(f"Department: {details['department']}")
    print(f"Salary: ${details['salary']:,.2f}")
    print(f"Bonus: ${details['bonus']:,.2f}")
    
    total_salary += details['salary']
    total_bonus += details['bonus']

print("\n" + "=" * 50)
print("TOTAL PAYROLL")
print("=" * 50)
print(f"Total Salary: Rs. {total_salary:,.2f}")
print(f"Total Bonus: Rs. {total_bonus:,.2f}")
print(f"Grand Total: Rs. {total_salary + total_bonus:,.2f}")

#......... Polymorphism ............
print("\n" + "=" * 50)
print("POLYMORPHISM - Same method, different output")
print("=" * 50)
for emp in employees:
    print(f"{emp.__class__.__name__:10} - {emp.name:8} - Rs. {emp.calculate_salary():,.2f}")