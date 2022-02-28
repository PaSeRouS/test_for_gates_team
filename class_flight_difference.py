from general_functions import fill_flight_classes
from general_functions import fill_flight_data


def display_diff_flight_classes(first_json, second_json):

    flight_classes_data_in_first_json = fill_flight_data(first_json, fill_flight_classes)
    flight_classes_data_in_second_json = fill_flight_data(second_json, fill_flight_classes)

    print('ОТЛИЧИЯ В УСЛОВИЯХ. \n')

    print('Типы перелёта, которые есть только в файле №1:')
    for flight_class in flight_classes_data_in_first_json:
        if flight_class not in flight_classes_data_in_second_json:
            print(flight_class)

    print('')

    print('Типы перелёта, которые есть только в файле №2:')
    for flight_class in flight_classes_data_in_second_json:
        if flight_class not in flight_classes_data_in_first_json:
            print(flight_class)

    print('')

    print('Типы перелёта, которые есть в обоих файлах:')
    for flight_class in flight_classes_data_in_first_json:
        if flight_class in flight_classes_data_in_second_json:
            print(flight_class)