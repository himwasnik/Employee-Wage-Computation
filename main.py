print("Welcome to Employee Wage Computation Program")

import random

print("Welcome to Employee Wage Computation Program")

# UC1: Check Employee Attendance
attendance = random.choice([0, 1])
if attendance == 1:
    print("Employee is Present")
else:
    print("Employee is Absent")


# UC2: Daily Employee Wage
wage_per_hour = 20
full_day_hour = 8
daily_wage = wage_per_hour * full_day_hour
print(f"Daily Employee Wage: {daily_wage}")



# UC3: Part-Time Employee Wage
part_time_hour = 4
part_time_wage = wage_per_hour * part_time_hour
print(f"Part-time Employee Wage: {part_time_wage}")


# UC4: Solve using Switch Case
def employee_wage(employee_type):
    switcher = {
        1: full_day_hour * wage_per_hour,  # Full-time employee
        2: part_time_hour * wage_per_hour  # Part-time employee
    }
    return switcher.get(employee_type, 0)  # Default for absent

employee_type = random.choice([0, 1, 2])  # 0: Absent, 1: Full-time, 2: Part-time
print(f"Employee Wage (Switch Case): {employee_wage(employee_type)}")


# UC5: Calculate Wages for a Month
working_days_per_month = 20
monthly_wage = working_days_per_month * daily_wage
print(f"Monthly Employee Wage: {monthly_wage}")


# UC6: Calculate Wages Till Condition
max_hours_per_month = 100
total_working_days = 0
total_working_hours = 0

while total_working_days < 20 and total_working_hours < max_hours_per_month:
    hours_worked = random.choice([0, 4, 8])  # 0: Absent, 4: Part-time, 8: Full-time
    total_working_hours += hours_worked
    total_working_days += 1

total_wage = total_working_hours * wage_per_hour
print(f"Total Employee Wage for the Month: {total_wage}")

