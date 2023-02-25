
# #2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, 
# автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), 
# цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.  ###

import json


def read_orders_from_json():
    with open('orders.json') as f_n:
        orders = json.load(f_n)
        return orders


def write_order_to_json(orders, item, quantity, price, buyer, date):
    new_data = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }
    orders["orders"].append(new_data)
    with open('orders.json', 'w') as o_j:
        o_j.write(json.dumps(orders, indent=4))



orders_list = read_orders_from_json()
# print(": ", orders_list)

# write_order_to_json(orders_list, 'fork', 5, 124, 'Jane', '25.10.2018')
# write_order_to_json(orders_list, 'table', 2, 2099, 'Mark', '16.10.2018')
write_order_to_json(orders_list, 'spoon', 5, 125, 'James', '23.10.2018')
write_order_to_json(orders_list, 'table', 200, 2099, 'Natalie', '19.10.2018')
