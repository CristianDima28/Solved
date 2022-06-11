def add_time(*args):
    start = args[0]
    duration = args[1]
    if len(args) > 2:
        week_day = args[2]

    start_pieces = start.split()
    am_pm = start_pieces[1]
    hour_parts = start_pieces[0].split(":")
    hours = hour_parts[0]
    mins = hour_parts[1]
    dur_pieces = duration.split(":")
    #if dur_pieces[1] > 12
    hrz = int(hours) + int(dur_pieces[0])
    mnz = int(mins) + int(dur_pieces[1])
    mnz2 = int(mins) + int(dur_pieces[1])

    if int(mnz) > 60:
        h = mnz / 60
        mnz = mnz % 60
        h = int(h)
        hrz = int(hrz) + int(h)
    elif int(mnz) == 60:
        h = mnz / 60
        mnz = "00"
        h = int(h)
        hrz = int(hrz) + int(h)
    elif int(mnz) < 60:
        if int(mnz) < 10:
            mnz = str("0") + str(mnz)
        elif mnz == 0:
            mnz = "00"

    if len(args) < 3:
        if am_pm == "AM":
            if int(hours) < 12:
                if hrz > 12:
                    am_pm = "PM"
                    print(hrz)

                    if len(str(int(hrz))) < 2:
                        hrz = str("0") + str(int(hrz)-12)
                        print(str(hrz) + ":" + str(mnz) + " " + str(am_pm))

                    elif len(str(int(hrz))) >= 2:
                        hrz = hrz % 12
                        count = 0
                        print(hrz)
                        zile = int(dur_pieces[0]) / 24
                        h_to_add = int(dur_pieces[0]) % 24
                        h_to_add = int(h_to_add)
                        print(str(h_to_add) + " ore de adaugat")
                        print(str(int(zile))+" zile")

                        hrz = int(hrz) + int(h_to_add)
                        if int(zile) == 1:
                            print(str(hrz) + ":" + str(mnz) + " " + am_pm + " (next day)")
                        if int(zile) > 1:
                            print(str(hrz) + ":" + str(mnz) + " " + am_pm, "(" + str(int(zile)) + " days later)")
                        # else:
                        #     print(str(hrz) + ":" + str(mnz) + " " + am_pm)


add_time("09:30 AM", "12:00")




# daca este 11:59 am se transforma in 12 pm
# daca este 11:59 pm se transforma in 12 am
