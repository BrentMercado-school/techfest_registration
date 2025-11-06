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

participants = {}
for i in range(number_participant):
    name = input("Enter participant name: ")
    track = input("Enter chosen track: ")
    participants[name] = track

print("\nRegistered Participants:")
counter = 1
for name, track in participants.items():
    print(f"{counter}. {name} - {track}")
    counter += 1