def arithmetic_arranger(*args):
    global rs
    problems = args[0]
    firsts = ""
    seconds = ""
    lines = ""
    results = ""
    arranged_problems = ""
    counts = 0
    non_nums = 0
    ops = []
    for prob in problems:
        x = prob.split()
        ops = ops + [x[1]]
        tot_len = 2 + max(len(x[0]), len(x[2]))
        a = " " * (tot_len - len(x[0])) + x[0]
        b = x[1] + " " * (tot_len - (len(x[1]) + len(x[2]))) + x[2]
        c = "-" * tot_len
        try:
            if x[1] == "-":
                rs = int(x[0]) - int(x[2])
            elif x[1] == "+":
                rs = int(x[0]) + int(x[2])
            d = " " * int(tot_len - len(str(rs))) + str(rs)
        except ValueError:
            non_nums += 1
            continue
        firsts = firsts + a + "    "
        seconds = seconds + b + "    "
        lines = lines + c + "    "
        results = results + d + "    "
    if len(args) > 1:
        if args[1] is True:
            arranged_problems = f"{firsts}\n{seconds}\n{lines}\n{results}"
    else:
        arranged_problems = f"{firsts}\n{seconds}\n{lines}"
    frs = firsts.split()
    snd = seconds.split()
    alls = frs + snd
    count_ops = 0
    for el in ops:
        if el not in ["-", "+"]:
            count_ops += 1
    for el in alls:
        if len(el) > 4:
            counts += 1
    if len(problems) > 4:
        return "Error: Too many problems."
    elif non_nums != 0:
        return "Error: Numbers must only contain digits."
    elif count_ops != 0:
        return "Error: Operator must be '+' or '-'."
    elif counts != 0:
        return "Error: Numbers cannot be more than four digits."
    else:
        return arranged_problems


print(arithmetic_arranger(["323 + 229", "311 + 2122", "312 + 10", "31s2 + 10"], True))

# Error: Numbers cannot be more than four digits....Checked + None
# Error: Numbers must only contain digits... Checked + None
# Error: Operator must be '+' or '-'."...Checked +   None
# Error: Too many problems...Checked but appears with other error.





