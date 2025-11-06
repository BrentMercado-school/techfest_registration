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

track_count = {}
for track in participants.values():
    track_count[track] = track_count.get(track,0) + 1

unique_tracks = {track for track, count in track_count.items()}
print("\nTracks offered in this event:")
counter = 1
for track in unique_tracks:
    print(f"{counter}. {track}")
    counter += 1


# duplicate_names = {}

print("\nParticipants per track:")
for track, count in track_count.items():
    print(f"{track}: {count}")
