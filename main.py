class Food(object):
    def __init__(self, name: str, value: int, calories: int):
        self.name = name
        self.value = value
        self.calories = calories

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_calories(self):
        return self.calories

    def density(self):
        return self.get_value()/self.get_calories()

    def __str__(self):
        return self.name + ': <' + str(self.value) \
               + ', ' + str(self.calories) + '>'


def build_menu(names: list, values: list, calories: list):
    #assert len(names) == len(values) and len(values) == len(calories), "namea, values, and calories lists must be of the same size"
    menu = []
    for column in range(len(values)):
        menu.append(Food(names[column], values[column], calories[column]))
    return menu


def greedy(items: list, constraint: int, key_function):
    items_copy = sorted(items, key = key_function, reverse= True)
    taken = []
    total_value, total_cost = 0, 0
    for i in range(len(items_copy)):
        if total_cost + Food.get_calories(items_copy[i]) <= constraint :
            taken.append(items_copy[i])
            total_cost += Food.get_calories(items_copy[i])
            total_value += Food.get_value(items_copy[i])
    return taken, total_value


def print_greedy(items, constraint, key_function):
    taken, total_value = greedy(items, constraint, key_function)
    print("Total value taken " , total_value)
    for item in taken:
        print("     " , item)


def which_is_best(items, constraint):
    print('Use greedy by value to allocate', constraint,
          'calories')
    print_greedy(items, constraint, Food.get_value)

    print('\nUse greedy by cost to allocate', constraint,
          'calories')
    print_greedy(items, constraint, lambda x : 1/Food.get_calories(x))
    print('\nUse greedy by density to allocate', constraint,
          'calories')
    print_greedy(items, constraint, Food.density)



names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = build_menu(names, values, calories)
which_is_best(foods, 1000)


