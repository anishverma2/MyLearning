from datetime import datetime, timezone, timedelta #timedelta gives the difference between 2 times

print(datetime.now())

print(datetime.now(timezone.utc))   #utc is standard time standard, its is the central time, normally matches GMT

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1, hours=4, minutes=30)   #this add 1 day 4 hours and 30 mins to the todays time
print(today)
print(tomorrow)

print(today.strftime('%d-%m-%Y %H:%M:%S'))     #strftime - string format time

user_date = input("Enter the in format YYYY-MM-DD: ")
user_date = datetime.strptime(user_date, '%Y-%m-%d')    #strptime - string parse time

print(user_date)
