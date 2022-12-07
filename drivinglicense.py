months = [31,28,31,30,31,30,31,31,30,31,30,31]
category = ["A","B","C","D","CE"]
category_value = [31,39,48,48,10]
registration_day = input("Enter day of registration: ")
enterCategory = input("Enter a category:" )
sunday = 2
sundayFlag = int(0)
#endOfstudy=""
regDayArray = []
n = len(registration_day)
flag = int(0)
value = int(0)
flagForCategory = int(0)
for i in range(n):
    if registration_day[i] == ".":
        value = int(registration_day[flag:i])
        regDayArray.append(value)
        flag = i+1
    else:
        continue
regDayArray.append(int(registration_day[flag:n]))
day = regDayArray[0]
month = regDayArray[1]
year = regDayArray[2]
for i in range(len(category)):
    if category[i] == enterCategory:
        flagForCategory = category_value[i]
day = day+flagForCategory-15
if day > months[regDayArray[1]-1]:
    day -= months[regDayArray[1]-1]
    month += 1
elif day < 0:
    day = months[regDayArray[1]-2]+day
    month -= 1
if month > 12:
    month = 1
    year += 1
elif month == 0:
    month = 12
    year -= 1
#print(str(day),".",str(month),".",year,sep="")
sum = int(0)
if regDayArray[2] == year:
    for i in range(month-1):
        sum += months[i]
    sum += day-1
    sundayFlag = sum%7
elif regDayArray[2] == year+1:
    sundayFlag = sum % 7
    sum = day - months[11]-2-1
elif regDayArray[2] == year-1:
    sum = 365 + day-1
    sundayFlag = sum % 7
if sundayFlag == sunday:
    day += 1
print(str(day),".",str(month),".",year,sep="")
#print(sundayFlag)