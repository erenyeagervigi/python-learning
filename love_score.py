def calculate_love_score(name, name1):
    total = 0
    total2 = 0
    to_check = "true"
    to_check2 = "love"
    #true
    for check in to_check:
        for char in name:
            if check == char:
                total += 1
    for check in to_check:
        for char in name1:
            if check == char:
                total += 1
    #love
    for check in to_check2:
        for char in name:
            if check == char:
                total2 += 1
    for check in to_check2:
        for char in name1:
            if check == char:
                total2 += 1

    str_total = str(total)
    str_total2 = str(total2)

    print(str_total + str_total2)

calculate_love_score("Kanye West", "Kim Kardashian")

