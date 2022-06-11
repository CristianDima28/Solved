def add_time(*args):
    start = args[0]
    duration = args[1]
    if len(args) > 2:
        week_day = args[2]
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start_pieces = start.split()
    am_pm = start_pieces[1]
    am_pm2 = start_pieces[1]
    hour_parts = start_pieces[0].split(":")
    hours = hour_parts[0]
    hours = int(hours)
    mins = hour_parts[1]
    dur_pieces = duration.split(":")
    dur_pieces[0] = int(dur_pieces[0])
    hrz = int(hours) + int(dur_pieces[0])
    hrz1 = hrz
    mnz = int(mins) + int(dur_pieces[1])
    mnz2 = int(mins) + int(dur_pieces[1])

    if int(mnz) > 60:
        h = int(mnz) / 60
        mnz = mnz % 60
        hrz = hrz + h
        if mnz < 10:
            mnz = str("0") + str(mnz)
        h = int(h)
    elif int(mnz) == 60:
        h = mnz / 60
        mnz = "00"
        h = int(h)
        hrz = hrz + h

    elif int(mnz) < 60:
        if int(mnz) < 10:
            mnz = str("0") + str(mnz)
        elif mnz == 0:
            mnz = "00"
            hrz = hrz
        else:
            h = 0
            mnz = mnz + h
            hrz = hrz + h

    dif = int(dur_pieces[0]) - int(hours)
    days = dur_pieces[0] / 24
    days = int(days)
    dif2 = int(dur_pieces[0]) % 24
    dif4 = int(dur_pieces[0]) % 12

    dif33 = hrz / 12
    dif33 = int(dif33)
    dif33 = dif33 * 12
    dif3 = hrz / 12
    dif3 = int(dif3)
    dif3 = dif3 / 2
    dif3_parts = str(dif3).split(".")
    x = int(dif3_parts[1])

    if hrz > 12:
        if (hrz % 12) == 0:
            hrz = 12
        elif hrz == 0:
            hrz = 12
        else:
            hrz = hrz % 12
    else:
        hrz = hrz

    ore = []
    for i in range(dur_pieces[0]+1):
        i = i + hours
        ore.append(i)

    o = []
    for ora in ore:
        if (ora % 12) != 0:
            ora = 0
        elif (ora % 12) == 0:
            ora = 1
        o.append(ora)
    o[0] = am_pm
    o2 = []
    for el in o:
        el = str(el)
    t = o
    i = 1
    for i in range(len(o)):
        if t[i] == 0:
            t[i] = t[i-1]
        else:
            if t[i-1] == "AM":
                t[i] = "PM"
            elif t[i-1] == "PM":
                t[i] = "AM"
        o2.append(t[i])
        i += 1
    am_pm = o2[-1]
    r = o2.count("AM")
    r1 = int(r / 12)
    r2 = r % 12
    if r1 >= 1:
        if r2 > 0:
            r3 = r1 + 1
        else:
            r3 = r1
    elif r1 < 1:
        if r2 > 0:
            r3 = r1 + 1
        else:
            r3 = 0
    if len(args) <= 2:
        if r3 == 0:
            print(str(hrz) + ":" + str(mnz), am_pm)
        elif r3 == 1:
            print(str(hrz) + ":" + str(mnz), am_pm, "(next day)")
        elif r3 > 1:
            print(str(hrz) + ":" + str(mnz), am_pm, "(" + str(r3) + " days later)")

    elif len(args) > 2:
        z = day_names[day_names.index(week_day):]
        cnt = 1
        l = day_names.index(week_day)
        if week_day in day_names:
            if r3 > len(z)-1:
                if r3 < 7:
                    cnt = cnt + 1
                else:
                    cnt = r3 / 7
                day_names = day_names * int(cnt)
        else:
            print("Day not existing!")
        week_day = day_names[day_names.index(week_day) + r3]

        if r3 == 0:
            print(str(hrz) + ":" + str(mnz), am_pm, week_day)
        elif r3 == 1:
            print(str(hrz) + ":" + str(mnz), am_pm, "(next day)", week_day)
        elif r3 > 1:
            print(str(hrz) + ":" + str(mnz), am_pm, "(" + str(r3) + " days later)", week_day)


add_time("1:00 PM", "35:00")












