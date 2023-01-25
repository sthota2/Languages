def is_year_leap(year):
    if ( year % 400 ) == 0 :
        print("Leap Year")
        return True
    elif ( year % 100 ) == 0:
        print ("Not Leap Year")
        return False
    elif ( year % 4 ) == 0:
        print("Leap Year")
        return True
    else:
        print ("Not Leap Year")
        return False

# put your code here
#

test_data = [1900, 2000, 2016, 1987,2020]
test_results = [False, True, True, False, True]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
