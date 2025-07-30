import calendar

def print_month_names():
    print("Names of all months:")
    for month in calendar.month_name:
        if month:  
            print(month)

print_month_names()