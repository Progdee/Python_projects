def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#

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
is_year_leap(1900)
is_year_leap(2000)
is_year_leap(2016)
is_year_leap(1987)
#
# Write your code here.
#

def days_in_month(year, month):
    thirty_one = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]
    twenty_8 = [2]
    if month in thirty_one:
        return 31
    elif month in thirty:
        return 30
    elif month in twenty_8:
        if is_year_leap(year):
            return 29
        else:
            return 28
    else:
        return None
#
# Write your new code here.
#
days_in_month(1900, 2)
days_in_month(2000, 2)
days_in_month(2016, 1)
days_in_month(1987, 11)
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
