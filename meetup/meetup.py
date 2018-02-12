from datetime import date, timedelta
from calendar import monthrange, day_name, weekday


def meetup_day(year, month, day_of_the_week, which):
    day_offset = {
        '1st': 1,
        '2nd': 8,
        '3rd': 15,
        '4th': 22,
        '5th': 29,
        'teenth': 13,
        'last': monthrange(year, month)[1]-6,
    }
    weekdays = dict(zip(day_name, range(7)))
    day_diff = (weekdays[day_of_the_week] - weekday(year, month, day_offset[which])) % 7
    return date(year, month, day_offset[which]) + timedelta(day_diff)

