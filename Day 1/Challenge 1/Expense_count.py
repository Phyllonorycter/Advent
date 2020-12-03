external_file = open('Expense_report.txt')

expense = list(external_file.readlines())

crutch = expense[-1]

expense.pop()
expense = [int(entry[:-1]) for entry in expense]

expense.insert(0, int(crutch))

num1 = 0
num2 = 1
num3 = 2

while expense[num1] + expense[num2] + expense[num3] != 2020:
    if num3 == len(expense) - 1:
        num2 += 1
        num3 = num1
        if num2 == len(expense)-1:
            num1 += 1
            num2 = num1
    else:
        num3 += 1
print(expense[num1] + expense[num2] + expense[num3])
mult = expense[num1] * expense[num2] * expense[num3]
print(expense[num1], expense[num2], expense[num3])
print(mult)
