from datetime import date, timedelta


def get_closest_wednesday_date():
    return get_closest_wednesday_from_date(date.today())


def get_closest_wednesday_from_date(a_date):
    wednesday_weekday = 2
    previous_wednesday_offset = (a_date.weekday() - wednesday_weekday) % 7
    next_wednesday_offset = (wednesday_weekday - a_date.weekday()) % 7
    if previous_wednesday_offset < next_wednesday_offset:
        return a_date - timedelta(days=previous_wednesday_offset)
    else:
        return a_date + timedelta(days=next_wednesday_offset)
