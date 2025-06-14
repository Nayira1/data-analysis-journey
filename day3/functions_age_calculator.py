def year_was_born():
  year = int(input("What year you were born in ?").strip())
  return year

def calc_age(year,current_year):
  age = current_year - int(year)
  return age

def display(age):
  print (f"Your age this year should be {age}")
  
try:
    current_year = int(input("What year is it now ?").strip())
    display(calc_age(year_was_born(), current_year))
except ValueError:
    print("Please enter a valid year")

