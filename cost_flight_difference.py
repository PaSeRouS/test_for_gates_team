from terminaltables import SingleTable

from general_functions import fill_cost_flights
from general_functions import fill_cost_info
from general_functions import fill_flight_airports
from general_functions import fill_flight_data
from general_functions import get_cost_flight
from general_functions import merge_values
from general_functions import splitting_list


def display_single_table(results, title):
    table_data = [
        [
            'Маршрут', 
            'Минимальная стоимость', 
            'Максимальная стоимость', 
            'Средняя стоимость'
        ]
    ]

    for route in results:
        route_result = []
        route_result.append(route)
        route_result.append(results[route]['min_value'])    
        route_result.append(results[route]['max_value'])
        route_result.append(results[route]['average_value'])

        table_data.append(route_result)

    table_instance = SingleTable(table_data, title)
    print(table_instance.table)
    print()


def display_double_table(results, title):
    table_data = [
        [
            'Маршрут', 
            'Минимальная стоимость в файле №1', 
            'Максимальная стоимость в файле №1', 
            'Средняя стоимость в файле №1',
            'Минимальная стоимость в файле №2', 
            'Максимальная стоимость в файле №2', 
            'Средняя стоимость в файле №2',
        ]
    ]

    for route in results:
        route_result = []
        route_result.append(route)
        route_result.append(results[route]['first_json_min_value'])    
        route_result.append(results[route]['first_json_max_value'])
        route_result.append(results[route]['first_json_average_value'])
        route_result.append(results[route]['second_json_min_value'])    
        route_result.append(results[route]['second_json_max_value'])
        route_result.append(results[route]['second_json_average_value'])

        table_data.append(route_result)

    table_instance = SingleTable(table_data, title)
    print(table_instance.table)
    print()


def display_diff_cost_flight(first_json, second_json):
    cost_flights_only_in_first_json = {}
    cost_flights_only_in_second_json = {}
    cost_flights_only_in_both_jsons = {}

    flight_airports_in_first_json = fill_flight_data(first_json, fill_flight_airports)
    flight_airports_in_second_json = fill_flight_data(second_json, fill_flight_airports)

    flight_costs_in_first_json = fill_cost_flights(first_json, get_cost_flight)
    flight_costs_in_second_json = fill_cost_flights(second_json, get_cost_flight)

    flights_only_in_first_json, flights_only_in_second_json, flights_in_both_jsons = splitting_list(flight_airports_in_first_json, flight_airports_in_second_json)

    for flight_route in flights_only_in_first_json:
        cost_info = {}

        min_cost, max_cost, average_cost, route = fill_cost_info(flight_costs_in_first_json, flight_route)

        cost_info['min_value'] = min_cost
        cost_info['max_value'] = max_cost
        cost_info['average_value'] = average_cost

        cost_flights_only_in_first_json.update({route: cost_info})

    for flight_route in flights_only_in_second_json:
        cost_info = {}

        min_cost, max_cost, average_cost, route = fill_cost_info(flight_costs_in_second_json, flight_route)

        cost_info['min_value'] = min_cost
        cost_info['max_value'] = max_cost
        cost_info['average_value'] = average_cost

        cost_flights_only_in_second_json.update({route: cost_info})

    for flight_route in flights_in_both_jsons:
        cost_info = {}

        min_cost, max_cost, average_cost, route = fill_cost_info(flight_costs_in_first_json, flight_route)

        cost_info['first_json_min_value'] = min_cost
        cost_info['first_json_max_value'] = max_cost
        cost_info['first_json_average_value'] = average_cost

        min_cost, max_cost, average_cost, route = fill_cost_info(flight_costs_in_second_json, flight_route)

        cost_info['second_json_min_value'] = min_cost
        cost_info['second_json_max_value'] = max_cost
        cost_info['second_json_average_value'] = average_cost

        cost_flights_only_in_both_jsons.update({route: cost_info})

    print('ОТЛИЧИЯ В СТОИМОСТИ РЕЙСОВ. \n')
    display_single_table(cost_flights_only_in_first_json, 'Стоимость маршрутов, которые есть только в первом файле')
    display_single_table(cost_flights_only_in_second_json, 'Стоимость маршрутов, которые есть только во втором файле')
    display_double_table(cost_flights_only_in_both_jsons, 'Стоимость маршрутов, которые есть в обоих файлах')