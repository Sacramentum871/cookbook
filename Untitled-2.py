import os
current = os.getcwd()
folder_name = 'Ingredients'
file_name = 'ingr.txt'
full_path = os.path.join(current, folder_name, file_name)
with open(full_path, 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingr_count = int(f.readline())
        dish = []
        for i in range(ingr_count):
            dishes = f.readline().strip()
            ingredient_name, quantity, measure = dishes.split(" | ")
            dish.append({
                'ingredient_name':  ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        cook_book[dish_name] = dish


def get_shop_list_by_dishes(dishes, person_count):
    asd = {}
    for dish in dishes:
        if dish in cook_book:
            for a in cook_book[dish]:
                if a['ingredient_name'] not in asd:
                    asd[a['ingredient_name']] = {'quantity': int(a['quantity']) * person_count, 'measure': a['measure']}
                else:
                    asd[a['ingredient_name']]['quantity'] += int(a['quantity']) * person_count
    return asd               


            
print(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 3))

                