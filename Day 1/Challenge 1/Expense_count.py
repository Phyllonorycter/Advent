external_file = open('Expense_report.txt')

expense = list(external_file.readlines())

crutch = expense[-1]

expense.pop()
expense = [int(entry[:-1]) for entry in expense]

expense.insert(0, int(crutch))

print(len(expense))

num1 = 0
num2 = 1
i = 0
while expense[num1] + expense[num2] != 2020:
     if num2 == len(expense) - 1:
        num1 += 1
        num2 = num1
     else:
         num2 += 1
print(expense[num1] + expense[num2])
mult = expense[num1] * expense[num2]
print(expense[num1], expense[num2])
print(mult)
