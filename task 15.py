# employees with there current salary and ratings
employees = {
    "ravi": {"salary": 40000, "rating": 5},
    "avinash": {"salary": 35000, "rating": 3},
    "mujahed": {"salary": 80000, "rating": 4},
    "gupta": {"salary": 50000, "rating": 2},
}
# percentage incrementation based on the ratings
increment_percentage = {
    5: 20,  # 20% rating=5
    4: 15,  # 15% rating= 4
    3: 10,  # 10% rating= 3
    2: 5,   # 5% rating=2
    1: 0    # 0% rating= 1
}
                                # printing the updated salaries
print("Updated Salaries:")
for employee, details in employees.items():
    salary = details["salary"]
    rating = details["rating"]
    increment = (salary * increment_percentage.get(rating, 0)) / 100
    new_salary = salary + increment
    print(f"{employee}: rs{new_salary:.2f}")
