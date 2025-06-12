while True:
    try:
        birthDate = int(input("What is your birth year? ").strip())
        while birthDate > 2025:
          print("Please enter a valid year")
          birthDate = int(input("What is your birth year? ").strip())
        else:
          yourAge = 2025 - birthDate
          print(f"Your age in 2025 is {yourAge}")
          break

    except ValueError:
          print("Please enter a valid year")
