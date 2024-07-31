def day_converter(num):
    if num == 1:
        print("Sunday")
    if num == 2:
        print("Monday")
    if num == 3:
        print("Tuesday")
    if num == 4:
        print("Wednesday")
    if num == 5:
        print("Thursday")
    if num == 6:
        print("Friday")
    if num == 0:
        print("Saturday")

def day_of_week(string):
    year = int(string[string.index(",") + 2:])
    century = year // 100
    last_two = year % 100
    last = 0
    century_doomsday = 0
    year_doomsday = 0
    day = int(string[string.index(" ") + 1:string.index(",")])
    day_of_week = 0
    if century % 4 == 0:
        century_doomsday = 3
    elif century % 4 == 3:
        century_doomsday = 4
    elif century % 4 == 2:
        century_doomsday = 6
    elif century % 4 == 1:
        century_doomsday = 1
    last = last_two + (last_two // 4)
    year_doomsday = (century_doomsday + last) % 7
    if last_two // 4 != last_two / 4 or (string[0:string.index(" ")] != "January" and string[0:string.index(" ")] != "February"):
        if string[0:string.index(" ")] == "January":
            day_of_week = (((day - 10) % 7) + year_doomsday) % 7
        if string[0:string.index(" ")] == "February":
            day_of_week = (((day - 14) % 7) + year_doomsday) % 7
        if string[0:string.index(" ")] == "March":
            day_of_week = (((day - 14) % 7) + year_doomsday) % 7
        if string[0:string.index(" ")] == "April":
            day_of_week = (((day - 4) % 7) + year_doomsday) % 7
        if string[0:string.index(" ")] == "May":
            day_of_week = (((day - 9) % 7) + year_doomsday) % 7
        if string[0:string.index(" ")] == "June":
            day_of_week = (((day - 6) % 7) + year_doomsday) % 7
        if string[0:string.index(" ")] == "July":
            day_of_week = (((day - 11) % 7) + year_doomsday) % 7
        if string[0:string.index(" ")] == "August":
            day_of_week = (((day - 8) % 7) + year_doomsday) % 7
        if string[0:string.index(" ")] == "September":
            day_of_week = (((day - 5) % 7) + year_doomsday) % 7
        if string[0:string.index(" ")] == "October":
            day_of_week = (((day - 10) % 7) + year_doomsday) % 7
        if string[0:string.index(" ")] == "November":
            day_of_week = (((day - 7) % 7) + year_doomsday) % 7
        if string[0:string.index(" ")] == "December":
            day_of_week = (((day - 12) % 7) + year_doomsday) % 7
        day_converter(day_of_week)
    else:
        last = last - 1
        year_doomsday = (century_doomsday + last) % 7
        if string[0:string.index(" ")] == "January":
            day_of_week = (((day - 10) % 7) + year_doomsday) % 7
        if string[0:string.index(" ")] == "February":
            day_of_week = (((day - 14) % 7) + year_doomsday) % 7
        day_converter(day_of_week)



day_of_week(input("Date: "))