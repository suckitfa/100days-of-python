def format_name(f_name,l_name):
    return f"{f_name.title()} {l_name.title()}"

print(format_name("alice","Shit"))

def is_leap(year):
    """If year is a leap year,return True or return False
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    """Get the days of a special year and month,
    month:1-12
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    el = month_days[month - 1]
    if month == 2:
        # return is_leap(year=year) el+1:el
        if(is_leap(year=year)):
            return el+1
        else:
            return el
    else:
        return el

year = int(input("Enter a year:"))
month = int(input("Enter a month:"))
days = days_in_month(year,month)
print(days)