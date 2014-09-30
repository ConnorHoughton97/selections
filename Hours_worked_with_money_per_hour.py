#Connor Houghton
#30.09.14
#Amount of money earned compared to how many hours worked.
hours = int(input("please enter how many hours you work: "))
money_per_hour = float(input("Please enter your hourly pay: "))

if hours < 40:
    total_money1 = hours * money_per_hour
    print("you will get £{0} a week.".format(total_money1))
elif 40 < hours <= 60:
    extra_hours = hours - 40
    extra_rate = money_per_hour * 1.5
    extra_cash = extra_hours * money_per_hour
    total_money2 = (40 * money_per_hour) + extra_cash
    print("You will get £{0} a week.".format(total_money2))
else:
    print("Invalid amount of hours worked.")
