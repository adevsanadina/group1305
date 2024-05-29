
ticket_price_per_person = 500
taxi_to_park = 600
taxi_from_park = taxi_to_park * 1.2
pizza_price = 250
pizza_discount = 0.15
pizza_quantity = 2
air_hockey_price_per_game = 80
air_hockey_games = 8
number_of_people = 4

total_ticket_price = ticket_price_per_person * number_of_people
total_taxi_price = taxi_to_park + taxi_from_park
total_pizza_price = pizza_price * pizza_quantity * (1 - pizza_discount)
total_air_hockey_price = air_hockey_price_per_game * air_hockey_games

total_expense = total_ticket_price + total_taxi_price + total_pizza_price + total_air_hockey_price
expense_per_person = total_expense / number_of_people

print(f"Кожен із вас повинен заплатити: {expense_per_person} грн")