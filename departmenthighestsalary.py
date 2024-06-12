employees = [
    {"name": "John", "department": "HR", "salary": 50000},
    {"name": "Jane", "department": "IT", "salary": 75000},
    {"name": "Doe", "department": "HR", "salary": 60000},
    {"name": "Alice", "department": "Finance", "salary": 80000},
    {"name": "Bob", "department": "IT", "salary": 70000},
    {"name": "Charlie", "department": "Finance", "salary": 85000}
]

def find_highest_salary_per_department(employees):
   
    highest_salaries = {}

    for employee in employees:
        department = employee["department"]
        salary = employee["salary"]

        if department not in highest_salaries or salary > highest_salaries[department]:
            highest_salaries[department] = salary

    return highest_salaries

highest_salaries = find_highest_salary_per_department(employees)
print(highest_salaries)