Work_11_LeapYear.py

yr = int(input("year:"))
if yr % 4 == 0 and yr % 100 != 0:
    print("leap year")
elif yr % 400 == 0:
    print("leap year")
else:
    print("not leap year")

