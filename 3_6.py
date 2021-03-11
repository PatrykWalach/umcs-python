
import datetime
import calendar


def weekday(date):
    year, month, day = date
    return calendar.day_name[datetime.datetime(year, month, day).weekday()]


print(weekday((2021, 3, 12)))
