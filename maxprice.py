n=int(input("Enter n: "))
days=[]
price=[]
for i in range(n):
    days.append(int(input("Enter days: ")))
    price.append(int(input("Enter price: ")))
print(days)
print(price)
summ=int(0)
while len(days)>2:
    max = int(0)
    index = int(0)
    for j in range(len(days)):
        m=days[j]*price[j]
        if m>max:
            max=m
            index=j
        elif (m==max):
            if ((days[j]-1)*price[j]>(days[index]-1)*price[index]):
                max=days[index]*price[index]
            else:
                max=days[j]*price[j]
                index=j;
    summ=summ+max
    days.pop(index)
    price.pop(index)
    flag=int(0)
    for j in range(len(days)):
        if days[j-flag]!=0:
            days[j-flag]=days[j-flag]-1
    for j in range(len(days)):
        if days[j-flag]== 0:
            days.pop(j-flag)
            price.pop(j-flag)
            flag=flag+1
    print(days)
    print(price)
if len(days)==2:
    if price[0]>price[1]:
        summ=summ+price[0]*days[0]
        days[1] = days[1] - 1
        days.pop(0)
        price.pop(0)
    else:
        summ=summ+price[1]*days[1]
        days[0] = days[0] - 1
        days.pop(1)
        price.pop(1)
if(len(days)==1):
    summ=summ+price[0]*days[0]
print("Summ is: "+str(summ))