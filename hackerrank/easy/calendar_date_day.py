import calendar
week_days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

mon, day, year = list(map(int, input().split()))
weekday = calendar.weekday(year, mon, day) 
print(week_days[weekday])