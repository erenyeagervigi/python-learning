while True:
    principle = float(input("enter the principle "))
    if principle < 0:
        print("principle cant be negative")
    else:


        while True:
            rate = float(input("enter the rate "))
            if rate < 0:
                print("rate cant be negative")
            else:

                while True:
                    time = float(input("enter the time "))
                    if time < 0:
                        print("rate cant be negative")
                    else:

                        Total = principle * (1 + rate / 100)
                        print(f"the total is {Total} ")

                        break
                break
        break