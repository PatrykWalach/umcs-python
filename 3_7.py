
import datetime
import calendar


def _weekday(date):
    year, month, day = date
    return calendar.day_name[datetime.datetime(year, month, day).weekday()]


def weekday(*dates, **namedDates):
    return {
        date: _weekday(date) for date in list(dates) + list(namedDates.values())
    }


print(weekday((2020, 3, 10), (2021, 3, 11),
              data1=(2023, 3, 10), data2=(2024, 3, 11)))
