def is_leap_year(year):
    if year %4 == 0:
        if year %100 == 0:
            if year %400 == 0:
                return f"{year} is a leap year"
            else:
                return f"{year} not a leap year"
        else:
            return f"{year} is a leap year"
    else:
        return f"{year} not a leap year"

input_year = int(input("Enter the year you wanna check:"))
print(is_leap_year(input_year))
