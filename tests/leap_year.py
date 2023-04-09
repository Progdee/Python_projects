def is_year_leap(year):
    if year % 100:
        if year % 4 == 0:
            return True
        else:
            return False
    else:
        if year & 4 == 0:
            return True
        else:
            return False
#
# Write your code here.
#
is_year_leap(1900)
is_year_leap(2000)
is_year_leap(2016)
is_year_leap(1987)
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")


