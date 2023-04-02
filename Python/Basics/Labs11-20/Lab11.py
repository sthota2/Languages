hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
total_hours = int((hour + (mins / 60) + (dura / 60)) % 24)
total_mins = (hour * 60 + mins + dura) % 60
print(total_hours, ":", total_mins, sep="")
