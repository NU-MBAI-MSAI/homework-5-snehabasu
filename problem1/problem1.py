def is_leap_year(year_in):
    if year_in % 4 == 0:
        if year_in % 100 == 0:
            if year_in % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
