import datetime

print("Enter year of birth yyyy")
yy=int(input())

print("Enter month of birth m/mm")
mm=int(input())

print("Enter day of birth d/dd")
dd=int(input())



bday=datetime.date(yy,mm,dd)

wkday=bday.isoweekday()

print("You were born on a ",end='')

if wkday == 1:
    print("Monday")
elif wkday == 2:
    print("Tuesday")
elif wkday == 3:
    print("Wednesday")
elif wkday == 4:
    print("Thursday")
elif wkday == 5:
    print("Friday")
elif wkday == 6:
    print("Saturday")
elif wkday == 7:
    print("Sunday")

