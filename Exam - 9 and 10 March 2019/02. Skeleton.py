#Read User Input
control_minutes = int(input()) * 60
control_seconds = int(input())
distance_track = float(input())
seconds_per_meter = int(input())

#Logic

overall_control_time = control_minutes + control_seconds
delay = (distance_track / 120) * 2.5
marin_time = (distance_track / 100) * seconds_per_meter - delay

#Print Output

if marin_time <= overall_control_time:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {marin_time:.3f}.")
else:
    difference = marin_time - overall_control_time
    print(f"No, Marin failed! He was {difference:.3f} second slower.")