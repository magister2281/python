class CoffeMachine:
    consist = {'water': 400, 'milk': 540, 'coffebeans': 120, 'cups': 9, 'money': 550}
    espresso = {'water': 250, 'milk': 0, 'coffebeans': 16, 'cups': 1, 'money': 4}
    latte = {'water': 350, 'milk': 75, 'coffebeans': 20, 'cups': 1, 'money': 7}
    cappuccino = {'water': 200, 'milk': 100, 'coffebeans': 12, 'cups': 1, 'money': 6}
    count = []
    var = []

    def amount(value):
        min_value = []
        summ_c = {'water': CoffeMachine.consist['water'] - value['water'],
                  'milk': CoffeMachine.consist['milk'] - value['milk'],
                  'coffebeans': CoffeMachine.consist['coffebeans'] - value['coffebeans'],
                  'cups': CoffeMachine.consist['cups'] - value['cups'],
                  'money': CoffeMachine.consist['money'] + value['money']}
        for key, i in summ_c.items():
            if i <= 0:
                min_value.append(key)
        if len(min_value) == 1:
            print(f"Sorry, not enough {min_value[0]}!")
            CoffeMachine.var.clear()
        elif len(min_value) == 2:
            print(f"Sorry, not enough {min_value[0]}, {min_value[1]}!")
            CoffeMachine.var.clear()
        elif len(min_value) == 3:
            print(f"Sorry, not enough {min_value[0]}, {min_value[1]}, {min_value[2]}!")
            CoffeMachine.var.clear()
        elif len(min_value) == 4:
            print(f"Sorry, not enough {min_value[0]}, {min_value[1]}, {min_value[2]}, {min_value[3]}!")
            CoffeMachine.var.clear()
        else:
            print("I have enough resources, making you a coffee!")
            CoffeMachine.var.append("True")

    def buy():
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        type = input()
        if type == "1":
            value = CoffeMachine.espresso
            sum_c = {'water': CoffeMachine.consist['water'] - value['water'],
                     'milk': CoffeMachine.consist['milk'] - value['milk'],
                     'coffebeans': CoffeMachine.consist['coffebeans'] - value['coffebeans'],
                     'cups': CoffeMachine.consist['cups'] - value['cups'],
                     'money': CoffeMachine.consist['money'] + value['money']}
            CoffeMachine.amount(value)
            if len(CoffeMachine.var) > 0:
                CoffeMachine.consist.update(sum_c)
        if type == '2':
            value = CoffeMachine.latte
            sum_c = {'water': CoffeMachine.consist['water'] - value['water'],
                     'milk': CoffeMachine.consist['milk'] - value['milk'],
                     'coffebeans': CoffeMachine.consist['coffebeans'] - value['coffebeans'],
                     'cups': CoffeMachine.consist['cups'] - value['cups'],
                     'money': CoffeMachine.consist['money'] + value['money']}
            CoffeMachine.amount(value)
            if len(CoffeMachine.var) > 0:
                CoffeMachine.consist.update(sum_c)

        if type == '3':
            value = CoffeMachine.cappuccino
            sum_c = {'water': CoffeMachine.consist['water'] - value['water'],
                     'milk': CoffeMachine.consist['milk'] - value['milk'],
                     'coffebeans': CoffeMachine.consist['coffebeans'] - value['coffebeans'],
                     'cups': CoffeMachine.consist['cups'] - value['cups'],
                     'money': CoffeMachine.consist['money'] + value['money']}
            CoffeMachine.amount(value)
            if len(CoffeMachine.var) > 0:
                CoffeMachine.consist.update(sum_c)

    def beautiful_print():
        print(f'''The coffee machine has:
    {CoffeMachine.consist['water']} of water
    {CoffeMachine.consist['milk']} of milk
    {CoffeMachine.consist['coffebeans']} of coffee beans
    {CoffeMachine.consist['cups']} of disposable cups
    {CoffeMachine.consist['money']} of money''')

    def fill():
        print("Write how many ml of water do you want to add:")
        water = int(input())
        print("Write how many ml of milk do you want to add:")
        milk = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        coffebeans = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        cups = int(input())
        sum_c = {'water': CoffeMachine.consist['water'] + water,
                 'milk': CoffeMachine.consist['milk'] + milk,
                 'coffebeans': CoffeMachine.consist['coffebeans'] + coffebeans,
                 'cups': CoffeMachine.consist['cups'] + cups,
                 'money': CoffeMachine.consist['money']}
        CoffeMachine.consist.update(sum_c)

    def take():
        print(f"I gave you ${CoffeMachine.consist['money']}")
        sum_c = {'water': CoffeMachine.consist['water'],
                 'milk': CoffeMachine.consist['milk'],
                 'coffebeans': CoffeMachine.consist['coffebeans'],
                 'cups': CoffeMachine.consist['cups'],
                 'money': CoffeMachine.consist['money'] - CoffeMachine.consist['money']}
        CoffeMachine.consist.update(sum_c)
        print("")

    def action_choose():
        while len(CoffeMachine.count) != 1:
            print("Write action (buy, fill, take, remaining, exit):")
            action = input()
            if action == "buy":
                CoffeMachine.buy()
            if action == "fill":
                CoffeMachine.fill()
            if action == "take":
                CoffeMachine.take()
            if action == "remaining":
                CoffeMachine.beautiful_print(CoffeMachine.consist)
            if action == "exit":
                CoffeMachine.count.append("end")

act = CoffeMachine.action_choose()
