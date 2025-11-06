print("Welcome to SMIT TechFest!\nOrganized by Brent Mercado of APPDAET BTCS1\n")

#gathering of number of participants
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

#collecting participant's information
participants = []
for i in range(number_participant):
    name = input("Enter participant name: ")
    track = input("Enter chosen track: ")
    participants.append({"name": name, "track": track})

print("\nRegistered Participants:")
for i, participant in enumerate(participants):
    print(f"{i+1}. {participant['name']} - {participant['track']}")

#tracking of unique track
track_count = {}
for participant in participants:
    track = participant['track']
    track_count[track] = track_count.get(track, 0) + 1

unique_tracks = {track for track, count in track_count.items()}
print("\nTracks offered in this event:")
for track in unique_tracks:
    print(track)

#tracking of duplicated name
name_count = {}
for participant in participants:
    name = participant['name']
    name_count[name] = name_count.get(name, 0) + 1

duplicated_names = {name for name, count in name_count.items() if count > 1}
print("\nDuplicated names found:")
for name in duplicated_names:
    print(name)

#tracking of number of participants per track
# print("\nParticipants per track:")
# for track, count in track_count.items():
#     print(f"{track}: {count}")

