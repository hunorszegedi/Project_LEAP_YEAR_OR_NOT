year = (int)(input("Year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Year {year} is a LEAP YEAR!\n")
        else:
            print(f"Year {year} is NOT a LEAP YEAR!\n")
    else:
        print(f"Year {year} is a LEAP YEAR!\n")
else:
    print(f"Year {year} is NOT a LEAP YEAR!\n")