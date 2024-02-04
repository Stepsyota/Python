days_of_week = [
    'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
    'sunday'
]
hour_now = 0
minute_now = 0
hour_add = 0
minute_add = 0
meridiems = ['am', 'pm']
meridiem_now = ''
day_of_week_now = ''

def add_time(time_now, time_add, day_of_week_now=0):

    #Check time
    x = check_and_set_time(time_now, time_add)
    if x == 0:
        print('Error')
        return

    #Check day of week
    if day_of_week_now == 0:
        pass
    else:
        day_of_week_now = format_str(day_of_week_now)
        day_of_week_now = check_day_of_week(day_of_week_now)
        if day_of_week_now == 0:
            print('Error')
            return

    #Conversion to 24-hour format
    hour_24_now = 0
    if meridiem_now == 'am':
        hour_24_now = 0 if hour_now == 12 else hour_now
    if meridiem_now == 'pm':
        hour_24_now = 12 if hour_now == 12 else hour_now + 12

    sum_minute = minute_now + minute_add
    minute_result = sum_minute % 60
    sum_24_hour = hour_24_now + hour_add
    hour_24_result = (sum_24_hour + (sum_minute // 60)) % 24
    days_pass = (sum_24_hour + (sum_minute // 60)) // 24

    #Conversion to 12-hour format
    hour_result = 0
    meridiem_result = ''
    if hour_24_result <= 11:
        meridiem_result = 'am'
        hour_result = 12 if hour_24_result == 0 else hour_24_result
    elif hour_24_result > 11:
        meridiem_result = 'pm'
        hour_result = 12 if hour_24_result == 12 else hour_24_result % 12

    #Calculation of the day of the week
    day_of_week_result = 0
    if day_of_week_now != 0:
        day_of_week_result = days_of_week[(days_of_week.index(day_of_week_now) +days_pass) % 7]

    print_time_result(hour_result, minute_result, meridiem_result, days_pass, day_of_week_result)


def check_and_set_time(time_now, time_add):
    global hour_now, minute_now, hour_add, minute_add

    time_now = format_str(time_now)
    time_add = format_str(time_add)

    index_now = time_now.find(':')
    index_add = time_add.find(':')

    if index_now != -1 and index_add != -1:
        index_meridiem = 0
        for meridiem in meridiems:
            if time_now.find(meridiem) != -1:
                index_meridiem = time_now.find(meridiem)
                break
        if index_meridiem != -1:
            return set_time(time_now, index_now, time_add, index_add, index_meridiem)
        else:
            print('Error')
            return 0
    else:
        print("Error")
        return 0


def set_time(time_now, index_now, time_add, index_add, index_meridiem):
    global hour_now, minute_now, hour_add, minute_add, meridiem_now

    hour_now = time_now[:index_now]
    minute_now = time_now[index_now + 1:index_meridiem]
    meridiem_now = format_str(time_now[index_meridiem:])
    if len(meridiem_now) > 2:
        print('Error')
        return 0

    hour_add = time_add[:index_add]
    minute_add = time_add[index_add + 1:]

    if hour_now.isdigit() and minute_now.isdigit() and hour_add.isdigit() and minute_add.isdigit():
        hour_now = int(hour_now)
        minute_now = int(minute_now)

        hour_add = int(hour_add)
        minute_add = int(minute_add)

        if hour_now > 12 or minute_now >= 60 or minute_add >= 60:
            print("Error")
            return 0
    else:
        print("Error")
        return 0


def format_str(str):
    str = str.replace(' ', '')
    str = str.lower()
    return str


def check_day_of_week(day_check):
    for day in days_of_week:
        if day_check == day:
            day_check = day
            return day_check
    return 0


def print_time_result(hour_result, minute_result, meridiem_result, days_pass,day_of_week_result):
    if hour_result == 0:
        hour_result = '00'
    if minute_result < 10:
        minute_result = f'0{minute_result}'
    meridiem_result = meridiem_result.upper()

    print(f'{hour_result}:{minute_result} {meridiem_result}', end="")

    if day_of_week_result != 0:
        day_of_week_result = day_of_week_result.capitalize()
        print(f', {day_of_week_result}', end="")

    if days_pass != 0:
        if days_pass == 1:
            print(f' (next day)')
        elif days_pass > 1:
            print(f' ({days_pass} days later)')
    print("")