months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date=input("Date: ")
    try:
        month,day,year=date.split('/')
        if int(day)>=1 and int(day)<=31:
            if int(month)>=1 and int(month)<=12:
                    break
    except:
        try:
            month_day,year=date.split(", ")
            m,day=month_day.split()
            for x in range(12):
                 if m==months[x]:
                      month=x+1
                      break
            if int(day)>=1 and int(day)<=31:
                if int(month)>=1 and int(month)<=12:
                        break
        except:
            print("not vaild")
            pass
print(f"{year}-{month:02}-{day:02}")
