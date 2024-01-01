def main():
    time=input('What time is it? ')
    time_check=convert(time)
    if time_check>=7 and time_check<=8:
        print('breakfast time')
    elif time_check >=12 and time_check<=13:
        print('lunch time')
    elif time_check>=18 and time_check<=19:
         print('dinner time')

def convert(time):
    hours, minutes = time.split(":")
    hours=float(hours)
    minutes=float(minutes)
    minutes=minutes/60
    return hours+minutes
    ...

if __name__ == "__main__":
    main()
