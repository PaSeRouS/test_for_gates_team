from general_functions import fill_flight_airports
from general_functions import fill_flight_data


def display_diff_flight_airports(first_json, second_json):

    flight_airports_in_first_json = fill_flight_data(first_json, fill_flight_airports)
    flight_airports_in_second_json = fill_flight_data(second_json, fill_flight_airports)

    print('ОТЛИЧИЯ В РЕЙСАХ. \n')

    print('Рейсы, которые есть только в файле №1:')
    for flight in flight_airports_in_first_json:
        if flight not in flight_airports_in_second_json:
            print(flight)

    print('')

    print('Рейсы, которые есть только во файле №2:')
    for flight in flight_airports_in_second_json:
        if flight not in flight_airports_in_first_json:
            print(flight)

    print('')

    print('Рейсы, которые есть в обоих файлах:')
    for flight in flight_airports_in_first_json:
        if flight in flight_airports_in_second_json:
            print(flight)