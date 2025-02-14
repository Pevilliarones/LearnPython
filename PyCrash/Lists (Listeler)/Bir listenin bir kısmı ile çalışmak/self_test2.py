pizzas = ["margarita", "pepperoni", "meksikan"]

friend_pizzas = pizzas [:]

pizzas.append("kavurmalı")

friend_pizzas.append("sucuklu")

print (f"sevdiğimiz pizzalar şunlardır : {pizzas}")
print (f"Arkadaşım ise bunları sever: {friend_pizzas}")

for pizzas in pizzas:
    print(pizzas)
for friend_pizzas in friend_pizzas:
    print(friend_pizzas)
    