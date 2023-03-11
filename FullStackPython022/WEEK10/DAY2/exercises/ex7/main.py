# ex 7

from datetime import datetime, timedelta


def upcoming_holiday():
    today = datetime.today()
    holiday = datetime(today.year, 12, 25)
    if holiday < today:
        holiday = datetime(today.year + 1, 12, 25)
    time_until_holiday = holiday - today
    print("Today is:", today.strftime("%Y-%m-%d %H:%M:%S"))
    print("The next holiday is Christmas on December 25th.")
    print("It is in:", time_until_holiday.days, "days and", time_until_holiday.seconds // 3600, "hours.")


upcoming_holiday()
