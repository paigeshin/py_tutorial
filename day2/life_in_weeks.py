age = input("What is your current age?")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365 
weeks_remaining = years_remaining * 52 
months_remaining = years_remaining * 12 

print(f"Days Remaining: {days_remaining}")
print(f"Weeks Remaining: {weeks_remaining}")
print(f"Months Remaining: {months_remaining}")