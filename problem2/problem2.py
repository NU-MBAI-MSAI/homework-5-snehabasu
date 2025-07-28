def date_format(date_in):
    month, day, year = date_in.split('/')
    formatted_month = "{:02d}".format(int(month))
    formatted_day = "{:02d}".format(int(day))
    return "{}-{}-{}".format(year, formatted_month, formatted_day)