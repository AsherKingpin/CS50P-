# in month-day-year order, formatted like 9/8/1636 or September 8, 1636
months = ["January","February","March","April",
"May","June","July","August","September","October","November","December"]

while True:
    date = input("Date:")
    if "/" in date:
        month, day, year = date.split("/")
    elif "," in date:
        date = date.replace(",","")
        month, day, year = date.split(" ")
        if month in months:
            month = months.index(month) + 1
    try:
        month = int(month)
        day = int(day)
        year = int (year)
        if 0 < month > 12 or 0 < day > 31:
            continue
        else:
            break
    except ValueError:
        break

print(f"{year}-{month:02}-{day:02}")

    
