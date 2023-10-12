import datetime

def getInput():
    year = input("Check year for friday the 13th Dates: ")
    while year.isdigit() is False or int(year) < 0:
        year = input("Error, Check year for friday the 13th Dates: ")
    year = int(year)   
    return year

def get_list_of_fri13th(year):
    result_list = []
    for month in range(1,13):
        date = datetime.datetime(year, month, 13)
        day_of_week = date.strftime("%A")
        #print(day_of_week)
        if day_of_week == "Friday":
            month_word = date.strftime("%B")
            result_list.append(f"13 {month_word} {year}")
    return result_list

year = getInput()
result_list = get_list_of_fri13th(year)
print(f"\nThe list of Friday the 13th for the year of {year} are:")
for res in result_list:
    print(res)
