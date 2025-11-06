print("Welcome to SMIT TechFest!\nOrganized by Brent Mercado of APPDAET BTCS1\n")

while True:
    try:
        number_participant = int(input("How many participants will register? "))
        if number_participant < 1:
            print("Invalid number of participants.")
            exit()
        break
    except ValueError:
        print("Please enter a valid number.\n")
        continue
