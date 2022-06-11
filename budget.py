import gc

class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount: float, description: str):
        self.ledger.append({"amount": amount, "description": description})

    def check_funds(self, amount):
        total = 0
        for dicts in self.ledger:
            for key in dicts:
                if key == "amount":
                    total += dicts[key]
        if amount > total:
            return False
        else:
            return True

    def withdraw(self, amount: float, description: str):
        assert amount >= 0
        if self.check_funds(amount):
            self.ledger.append({"amount": -1 * amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        total = 0
        for dicts in self.ledger:
            for key in dicts:
                if key == "amount":
                    total += dicts[key]
        return total

    def __repr__(self):
        return f'{self.name}'

    def transfer(self, amount, other):
        new_ob = Category(f"{other}")
        if self.check_funds(amount):
            self.ledger.append({"amount": -1 * amount, "Transfer to: ": f"{other}"})
            new_ob.ledger.append({"amount": amount, "Transfer from: ": self.name})
            return True
        else:
            return False

    def budget(self):
        lis = []
        names = []
        amounts = []
        new_item = ""
        for i in self.ledger:
            for key, value in i.items():
                if str(key).startswith("Tran"):
                    i[key] = str(key[:-2]) + " " + value


        total = 0
        for i in self.ledger:
            for el in i.values():
                if isinstance(el, str):
                    names.append(el)
                else:
                    amounts.append(el)
                    total = total + el
        lis = list(zip(names, amounts))
        nl = []
        x = 1
        nln = []
        for el in lis:
            k, v = el
            nl.append([k, v])
        for el in nl:
            item = str(el[0]) + x * " " + str(el[1])

            nln.append(str(item))
        maxm = 0
        for el in nln:
           if len(el) > maxm:
               maxm = len(el)
           continue

        nr_stars = round((maxm - len(self.name)) / 2)
        first = str(str("*" * nr_stars) + self.name + str("*" * nr_stars))

        for el in lis:
            k, v = el
            nl.append([k, v])
        nln2 = ""
        nl2 = []
        for el in nl:
            if el not in nl2:
                nl2.append(el)
            continue
        n_first = first + "\n"
        for el in nl2:
            spaces = len(first) - len(el[0]) - len(str(el[1]))
            item = str(el[0]) + spaces * " " + str(el[1])
            n_first = n_first + str(item) + "\n"

        n_sec = n_first + "Total: " + str(total)
        print(n_sec)


def create_spent_chart(some_class):
    instances = []
    instances2 = []
    chart = [["100", "|"], [" 90", "|"], [" 80", "|"], [" 70", "|"], [" 60", "|"], [" 50", "|"], [" 40", "|"], [" 30", "|"], [" 20", "|"], [" 10", "|"], ["  0", "|"]]
    for obj in gc.get_objects():
        if isinstance(obj, some_class):
            instances.append(obj)
            instances2.append(str(obj))

    expences = []
    for obj in instances:
        for key, value, in obj.ledger[0].items():
            if isinstance(value, int):
                first_dep = value
                total_expence = int(round(100 - ((obj.get_balance() * 100) / first_dep), -1))
                expences.append(total_expence)

    for el in list(reversed(chart)):
        for ex in expences:
        # Am identificat eroarea : daca in fata zeroului care se doreste adaugat este un spatiu liber, zeroul acesta se pune la categoria precedenta si nu la actuala
            if ex >= int(el[0]):
                if len(el) <= 2:
                    el.append(" 0")
                elif len(el[0]) >= 2:
                    el.append("  0")
            elif ex < int(el[0]):
                if len(el) <= 2:
                    el.append("  ")
                elif len(el[0]) >= 2:
                    el.append("   ")


    biggest = 0
    the_big = ""
    text = ""
    for el in chart:
        if len(el) > biggest:
            the_big = el
    for el in the_big:
        text = text + str(el)
    chart.append(4 * " " + "-" * (1 + len(text[text.index("|"):])))

    ch = ""
    for el in chart:
        for i in el:
            ch = ch + str(i)
        ch = ch + "\n"
        chart = ch

    names = []
    for ins in instances:
        name = list(str(ins))
        names.append(name)

    lst = names
    mxm = 0
    for el in lst:
        if len(el) > mxm:
            mxm = len(el)
        continue

    inner_list = []
    for el in lst:
        els = list(el)
        inner_list.append(els)

    for el in inner_list:
        if len(el) < mxm:
            for i in range(mxm - len(el)):
                el.append(" ")
        continue

    nl = inner_list

    nls = []
    nlb = []
    for i in range(len(nl[0])-1):
        for lis in nl:
            nls.append(lis[i])
    nlb.append(nls)
    nlb = nlb[0]
    nln = [nlb[i: i+len(instances)] for i in range(0, len(nlb), len(instances))]
    nl = nln


    string = ""
    for lis in nl:
        string = string + 5 * " "
        for el in lis:
            string = string + el + 2 * " "
        string = string + "\n"

    return "Percentage spent by category" + "\n" + chart + string


food = Category("Food")
utils = Category("Utils")
food.deposit(1000, "first deposit")
food.withdraw(90, "loan")
# print(food.ledger)
utils.deposit(190, "second Dep")
utils.deposit(10, "Allocated")
food.transfer(20, "Utility")
utils.withdraw(50, "fast_expence")
holiday = Category("Holidays")
holiday.deposit(200, "Deposit")
holiday.withdraw(100, "Urgency")
holiday.withdraw(30, "Mother")
food.withdraw(250, "something")
utils.withdraw(20, "some")
fun = Category("Fun Stuff")
fun.deposit(500, "Initial")
fun.withdraw(100, "Carosel")
fun2 = Category("Travels")
fun2.deposit(500, "Initial")
fun2.withdraw(300, "Carosel")



print(food.ledger)
print("Food funds: " ,food.get_balance())


food.budget()
utils.budget()
print("\n \n ")
print(create_spent_chart(Category))














#food.get_balance()




