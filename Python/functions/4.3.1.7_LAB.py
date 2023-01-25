def is_year_leap(year):
    if ( year % 400 ) == 0 :
        return True
    elif ( year % 100 ) == 0:
        return False
    elif ( year % 4 ) == 0:
         return True
    else:
         return False
        
#
# Your code from LAB 4.3.1.6.
#

def days_in_month(year, month):
    month_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_year_leap(year):
        if month == 2:
            return month_list[month-1]+1
        else:
            return month_list[month-1]
    else:
        return month_list[month-1]
        
    
#
# Write your new code here.
#

test_years = [1900, 2000, 2016, 1987,1999,2022]
test_months = [2, 2, 1, 11,12,2]
test_results = [28, 29, 31, 30,31,28]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
