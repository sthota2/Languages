hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
converted_hour = int((mins / 60 + dura / 60) % 24)
total_hour = hour + converted_hour

if total_hour > 23:
    total_hour = hour + converted_hour - 24

converted_min = hour * 60
total_min = (converted_min + mins + dura) % 60
print(str(total_hour) + ':' + str(total_min))
