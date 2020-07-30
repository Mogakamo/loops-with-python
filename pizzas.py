pizza = ['dominos', 'kfc', 'Wing a Ding']
friend_pizza = pizza[:]

pizza.append('peperoni')
friend_pizza.append('freshas')

print("My favorite pizzas are: ")
for pizza in range(0, 4):
    print(pizza.title() + "pizza.")

