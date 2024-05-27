from constans import MSG_INPUT_NAME_OF_THE_DISH, MSG_INPUT_NAME_OF_THE_RESIPE

head = '$' * 50
name_of_the_dish = input(MSG_INPUT_NAME_OF_THE_DISH ) .upper() .strip()
name_dish = f"{'&' * 10} {name_of_the_dish} {'&' * 10}"
name_of_the_resipe = input(MSG_INPUT_NAME_OF_THE_RESIPE) .lower() .strip()
name_recipe = f"{name_of_the_resipe} {'🌟'}"

print(head)
print(name_dish)
print(name_recipe)

meat = name_of_the_resipe .count("м'ясо")
print(f"Кількість слів 'м'ясо' в рецепті: {meat}")
