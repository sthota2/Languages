def is_year_leap(year):
    if ( year % 400 ) == 0 :
        return True
    elif ( year % 100 ) == 0:
        return False
    elif ( year % 4 ) == 0:
         return True
    else:
         return False
        
def days_in_month(year, month):
    month_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_year_leap(year):
        if month == 2:
            return month_list[month-1]+1
        else:
            return month_list[month-1]

def day_of_year(year, month, day):
    if ( is_year_leap(year) == True):
        if ( month !=1):
          extra_days=1
        else:
          extra_days=0
    else:
        extra_days=0
    days=0
    month_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    for day_count in range(0,month-1):
        days+=month_list[day_count]
    return days + day+ extra_days
        
        
#
# Write your new code here.
#

print(day_of_year(2000, 12, 31))
print(day_of_year(2000, 1, 31))
print(day_of_year(2000, 2, 1))
print(day_of_year(2022, 2, 26))
print(day_of_year(2021, 12, 16))
