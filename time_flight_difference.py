from terminaltables import SingleTable

from general_functions import fill_flight_airports
from general_functions import fill_flight_data
from general_functions import fill_flights_times
from general_functions import merge_values
from general_functions import splitting_list

from pprint import pprint


def display_single_table(results, title):
    table_data = [
        [
            'Маршрут', 
            'Время начала и конца маршрута'
        ]
    ]

    for time in results:
        time_result = []
        time_result.append(results[time]['Route'])
        time_result.append(results[time]['Times'])

        table_data.append(time_result)

    table_instance = SingleTable(table_data, title)
    print(table_instance.table)
    print()


def display_double_table(results, title):
    table_data = [
        [
            'Маршрут', 
            'Время начала и конца маршрута в файле №1',
            'Время начала и конца маршрута в файле №2'
        ]
    ]

    for time in results:
        time_result = []
        time_result.append(results[time]['Route'])
        time_result.append(results[time]['Time_in_first_file'])
        time_result.append(results[time]['Time_in_second_file'])

        table_data.append(time_result)

    table_instance = SingleTable(table_data, title)
    print(table_instance.table)
    print()


def display_diff_route_times(first_json, second_json):
    flight_times_only_in_first_json = {}
    flight_times_only_in_second_json = {}
    flight_times_only_in_both_jsons = {}

    flight_airports_in_first_json = fill_flight_data(first_json, fill_flight_airports)
    flight_airports_in_second_json = fill_flight_data(second_json, fill_flight_airports)

    flight_times_in_first_json = fill_flights_times(first_json)
    flight_times_in_second_json = fill_flights_times(second_json)

    flights_only_in_first_json, flights_only_in_second_json, flights_in_both_jsons = splitting_list(flight_airports_in_first_json, flight_airports_in_second_json)

    number_of_record = 0

    for flight_route in flights_only_in_first_json:
        route = ','.join(flight_route)
        flag_route = False

        for flight_time in flight_times_in_first_json:
            if flight_time['Flight'] == flight_route:
                flight_times_info = {}

                flight_times_info['Route'] = route

                if not flag_route:
                    route = ''
                    flag_route = True

                flight_times_info['Times'] = flight_time['Times']
                flight_times_only_in_first_json.update({number_of_record:flight_times_info})

                number_of_record += 1

    number_of_record = 0

    for flight_route in flights_only_in_second_json:
        route = ','.join(flight_route)
        flag_route = False

        for flight_time in flight_times_in_second_json:
            if flight_time['Flight'] == flight_route:
                flight_times_info = {}

                flight_times_info['Route'] = route

                if not flag_route:
                    route = ''
                    flag_route = True

                flight_times_info['Times'] = flight_time['Times']
                flight_times_only_in_second_json.update({number_of_record:flight_times_info})

                number_of_record += 1

    number_of_record = 0

    for flight_route in flights_in_both_jsons:
        records_in_first_file, records_in_second_file = 0, 0

        for flight_time in flight_times_in_first_json:
            if flight_time['Flight'] == flight_route:
                records_in_first_file += 1

        for flight_time in flight_times_in_second_json:
            if flight_time['Flight'] == flight_route:
                records_in_second_file += 1

        route = ','.join(flight_route)
        flag_route = False

        if records_in_first_file > records_in_second_file:
            max_value = records_in_first_file
        else:
            max_value = records_in_second_file

        value_of_record = 0
        while value_of_record < max_value:
            number_of_record += 1
            value_of_record += 1

            flight_times_info = {}

            flight_times_info['Route'] = route

            if not flag_route:
                route = ''
                flag_route = True

            number_of_record_in_loop = 0
            for flight_time in flight_times_in_first_json:
                if flight_time['Flight'] == flight_route:
                    number_of_record_in_loop += 1

                    if number_of_record_in_loop == value_of_record:
                        flight_times_info['Time_in_first_file'] = flight_time['Times']

            if number_of_record_in_loop < value_of_record:
                flight_times_info['Time_in_first_file'] = ''

            number_of_record_in_loop = 0
            for flight_time in flight_times_in_second_json:
                if flight_time['Flight'] == flight_route:
                    number_of_record_in_loop += 1

                    if number_of_record_in_loop == value_of_record:
                        flight_times_info['Time_in_second_file'] = flight_time['Times']

            if number_of_record_in_loop < value_of_record:
                flight_times_info['Time_in_second_file'] = ''

            flight_times_only_in_both_jsons.update({number_of_record:flight_times_info})

        number_of_record += 1

        flight_times_info = {}
        flight_times_info['Route'] = '---------------'
        flight_times_info['Time_in_first_file'] = '---------------------------------'
        flight_times_info['Time_in_second_file'] = '---------------------------------'
        flight_times_only_in_both_jsons.update({number_of_record:flight_times_info})

    print('ОТЛИЧИЯ ВО ВРЕМЕНИ НАЧАЛА И КОНЦА МАРШРУТА.\n')
    display_single_table(flight_times_only_in_first_json, 'Время начала и конца маршрутов, которые есть только в первом файле')
    display_single_table(flight_times_only_in_second_json, 'Время начала и конца маршрутов, которые есть только во втором файле')
    display_double_table(flight_times_only_in_both_jsons, 'Время начала и конца маршрутов, которые есть в обоих файлах')