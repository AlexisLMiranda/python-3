from pprint import pprint

def build_car_list():
    # Read car IDs from car-ids.txt
    with open('car-ids.txt', 'r') as f:
        car_ids = {int(line.strip()) for line in f}

    # Read car data from input.txt
    car_list = []
    with open('input2.txt', 'r') as f:
        for line in f:
            data = line.strip().split(',')
            car_id = int(data[0])
            if car_id in car_ids:
                try:
                    miles = int(data[1])
                    model = data[2]
                    car_list.append({'id': car_id, 'miles': miles, 'model': model})
                except (ValueError, IndexError):
                    pass  # Skip lines with invalid data format

    return car_list

def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()
