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



#
# Your code from LAB 4.3.1.6.
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
#
# Your code from LAB 4.3.1.7.
#

def day_of_year(year, month, day):
    if month == 1:
        return day
    elif month == 2:
        return day + 31
    elif month == 3:
        if is_year_leap(year):
            return day + 31 + 29
        else:
            return day + 31 + 28
    elif month == 4:
        if is_year_leap(year):
            return day + 31*2 + 29
        else:
            return day + 31*2 + 28
    elif month == 5:
        if is_year_leap(year):
            return day + 31 + 29 + 30
        else:
            return day + 31 + 28 + 30
    elif month == 6:
        if is_year_leap(year):
            return day + 31*3 + 29 + 30
        else:
            return day + 31*3 + 28 + 30
    elif month == 7:
        if is_year_leap(year):
            return day + 31*3 + 29 + 30*2
        else:
            return day + 31*3 + 28 + 30*2
    elif month == 8:
        if is_year_leap(year):
            return day + 31*4 + 29 + 30*2
        else:
            return day + 31*4 + 28 + 30*2
    elif month == 9:
        if is_year_leap(year):
            return day + 31*5 + 29 + 30*2
        else:
            return day + 31*5 + 28 + 30*2
    elif month == 10:
        if is_year_leap(year):
            return day + 31*5 + 29 + 30*3
        else:
            return day + 31*5 + 28 + 30*3
    elif month == 11:
        if is_year_leap(year):
            return day + 31*6 + 29 + 30*3
        else:
            return day + 31*6 + 28 + 30*3
    elif month == 12:
        if is_year_leap(year):
            return day + 31*6 + 29 + 30*4
        else:
            return day + 31*6 + 28 + 30*4
    else:
        return None
#
# Write your new code here.
#

print(day_of_year(2000, 12, 31))
