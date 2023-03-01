import datetime
day1 = int(input("Enter date of birth1: "))
day2 = int(input("Enter date of birth2: "))
month1 = int(input("Enter month of birth1: "))
month2 = int(input("Enter month of birth2: "))
year1 = int(input("Enter year of birt1: "))
year2 = int(input("Enter year of birt2: "))
HB1 = datetime.date(year1, month1, day1)
print(HB1)
HB2 = datetime.date(year2, month2, day2)
print(HB2)
today = datetime.datetime.today()
if HB1<HB2:
    print("HB1 older than HB2")
elif HB1==HB2:
    print("Peers")
else:
    print("HB1 younger than HB2")
