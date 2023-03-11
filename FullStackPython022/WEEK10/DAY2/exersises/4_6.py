# # ex4
#
# import datetime
#
#
# def display_current_date():
#     now = datetime.datetime.now()
#     print("Current date:", now.strftime("%Y-%m-%d"))
#
#
# display_current_date()
#
#
# # ex 5
# def time_left_until_new_year():
#     now = datetime.datetime.now()
#     new_year = datetime.datetime(now.year + 1, 1, 1)
#     time_left = new_year - now
#     days_left = time_left.days
#     hours_left = time_left.seconds // 3600
#     minutes_left = (time_left.seconds % 3600) // 60
#     seconds_left = time_left.seconds % 60
#     return f"The 1st of January is in {days_left} days and {hours_left}:{minutes_left:02d}:{seconds_left:02d} hours."
#
#
# print(time_left_until_new_year())

# ex 6

from datetime import datetime


def minutes_lived(birthdate):
    birth_datetime = datetime.strptime(birthdate, "%Y-%m-%d %H:%M:%S")
    now_datetime = datetime.now()
    diff = now_datetime - birth_datetime
    get_minutes_lived = int(diff.total_seconds() / 60)
    return get_minutes_lived


birthdate_str = "1998-11-11 15:15:00"
minutes_lived = minutes_lived(birthdate_str)
print(f"You have lived {minutes_lived} minutes so far!")