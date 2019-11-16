def translate(arr):
    
	total_food = {}
    food_types = list()

    for row in arr:

        city = row[0]
        food_type = row[1]
        amount = int(row[2])

        if city not in total_food:
            total_food[city] = dict()

        if food_type not in total_food[city]:
            total_food[city][food_type] = 0

        if food_type not in food_types:
            food_types.append(food_type)

        total_food[city][food_type] += amount

    food_types = sorted(food_types)

    sorted_total_food = list()
    for city_name in total_food:
        sorted_total_food.append([city_name, total_food[city_name]])

    sorted_total_food = sorted(sorted_total_food)

    to_return = list()
    for city, food_data in sorted_total_food:

        new_row = list()
        for food in food_types:
            new_row.append(food_data.get(food, 0))

        to_return.append(new_row)

    return to_return