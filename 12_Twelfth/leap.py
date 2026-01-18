year  = int(input("Enter the year "))

# Leap Year % 4 and not by 100 unless also % by 400

if (year%400 == 0) or (year%4 ==0 and year %100 !=0):
    print("LEAP YEAR")
else:
    print("NOT LEAP YEAR")

val = "Leap Year" if year%400 ==0 or(year%4==0 and year%100!=0) else "Not Leap Year"
print(val)

is_leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
print(is_leap)
val = "Leap Year" if is_leap else "Not Leap Year"
