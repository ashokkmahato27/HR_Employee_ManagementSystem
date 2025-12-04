# HR Employee Management System

A simple Python program demonstrating **Classes, Inheritance, and Polymorphism**.

About

Manages 3 employee types with different salary and bonus calculations:
- **Full-Time** - Fixed salary with rating-based bonus
- **Part-Time** - Hourly pay with hours-based bonus
- **Intern** - Fixed stipend with completion bonus

# Create employees
emp1 = FullTime("Rahul", "Engineering", 80000, 5)

emp2 = PartTime("Sonam", "Support", 25, 120)

emp3 = Intern("Ashok", "IT", 2000)

# Sample Output


<img width="702" height="823" alt="image" src="https://github.com/user-attachments/assets/4d39b983-2f7e-4378-8a74-e10e3f57f413" />
<img width="851" height="585" alt="image" src="https://github.com/user-attachments/assets/840bc79e-9692-4462-9279-e4cd75b3bc43" />



# Calculate salary (Polymorphism)
emp1.calculate_salary()  # 80000

emp2.calculate_salary()  # 3000

emp3.calculate_salary()  # 2000

# Apply bonus
emp1.apply_bonus()  # 16000 (20% of salary)

# Get details as dictionary
emp1.get_details()
# {'name': 'Rahul', 'department': 'Engineering', 'salary': 80000, 'bonus': 16000}

# OOP Concepts
Concept	Example
Class	Employee, FullTime, PartTime, Intern
Inheritance	FullTime(Employee)
Polymorphism	calculate_salary() works differently for each type
Dictionary	get_details() returns data as dict
