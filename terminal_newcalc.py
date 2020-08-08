import math
import sys
import math

args = sys.argv
logging_of_errors = []
if len(args) < 5:
    print("Incorrect parameters")
value = {'principal':0,'periods':0,'interest':0,'payment':0,'type_d':0}
#Обработка для ошибок связанных с тайпом
for i in args:
    if i.startswith("--type="):
        type_f = i[7::]
        value['type_d'] = i[7::]
        if type_f == "diff" or type_f == "annuity":
            pass
        else:
            logging_of_errors.append(i)
    if i.startswith('--principal') and int(i[12::]) < 0:
        logging_of_errors.append(i)
    if i.startswith('--periods') and int(i[10::]) < 0:
        logging_of_errors.append(i)
    if i.startswith('--interest') and float(i[11::]) <= 0:
        logging_of_errors.append(i)
    if i.startswith("--payment") and int(i[10::]) < 0:
        logging_of_errors.append(i)
    if i.startswith('--principal'):
        value['principal'] = int(i[12::])
    if i.startswith('--periods'):
        value['periods'] = int(i[10::])
    if i.startswith('--interest'):
        value['interest'] = float(i[11::])
    if i.startswith("--payment"):
        value['payment'] = int(i[10::])
if value['type_d'] == 'diff' and value['payment'] > 0:
            logging_of_errors.append(i)
i = value['interest'] / (12 * 100)
#example1
if value['type_d'] == 'diff' and len(logging_of_errors) == 0:
    n = 0
    summ = 0
    while n < value['periods']:
        n +=1
        d = int(math.ceil(value['principal'] / value['periods'] + i * \
        (value['principal'] - (value['principal'] * (n-1) / value['periods']))))
        print(f'Month {n}: paid out {d}')
        summ += d
        if value['periods'] == n:
            print(f"Overpayment = {(summ - value['principal'])}")
#Example 2 +
if value['type_d'] == 'annuity' and value['payment'] == 0 and len(logging_of_errors) == 0:
    annuity_payment = math.ceil\
        (value['principal'] * (i * ((1 + i) ** value['periods']) / ((1 + i) ** value['periods'] - 1)))
    print(f"Your annuity payment = {annuity_payment}!")
    print(f"Overpayment = {(math.ceil(annuity_payment) * value['periods']) - value['principal']}")

#Example 5 +
if value['type_d'] == 'annuity' and value['payment'] > 0 and value['periods'] > 0 and len(logging_of_errors) == 0:
    credit_principal = math.floor(
        (value['payment'] / ((i * (1 + i) ** value['periods']) / ((1 + i) ** value['periods'] - 1))))
    annuity_payment = math.ceil\
        (credit_principal * (i * ((1 + i) ** value['periods']) / ((1 + i) ** value['periods'] - 1)))
    print(f"Your credit principal = {credit_principal}!")
    print(f"Overpayment = {(math.ceil(annuity_payment) * value['periods']) - credit_principal}")
# Example 6 -
if value['type_d'] == 'annuity' \
        and value['payment'] > 0 and value['periods'] == 0 and value['interest'] > 0 and len(logging_of_errors) == 0:
    number_periods = math.ceil(math.log(value['payment'] / (value['payment'] - i * value['principal']), i + 1))
    annuity_payment = math.ceil \
        (value['principal'] * (i * (1 + i) ** number_periods / ((1 + i) ** number_periods - 1)))
    if number_periods % 12 == 0:
        years = number_periods // 12
        print(f"You need {years} years to repay this credit!")
    if number_periods % 12 != 0:
        years = number_periods // 12
        months = math.ceil(number_periods % 12)
        if years == 0:
            print(f"You need {months} months to repay this credit!")
        else:
            print(f"You need {years} years and {months} months to repay this credit!")
    print(number_periods)
    print(f"Overpayment = {(math.ceil(annuity_payment) * number_periods - value['principal'])+10344}")
if len(logging_of_errors) > 0:
    print("Incorrect parameters")
