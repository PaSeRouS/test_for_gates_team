from general_functions import merge_values


def get_route(flights):
    flag_source = False

    for flight in flights['OnwardPricedItinerary']['Flights']['Flight']:
        if type(flight) == str:
            if flight == 'Source' and not flag_source:
                flight_source = flights['OnwardPricedItinerary']['Flights']['Flight']['Source']
                flag_source = True
            elif flight == 'Destination':
                flight_destination = flights['OnwardPricedItinerary']['Flights']['Flight']['Destination']
        else:
            if not flag_source:
                flight_source = flight['Source']
                flag_source = True

            flight_destination = flight['Destination']
    
    return merge_values(flight_source, flight_destination)


def fill_routes(json):
    routes = []

    for flights in json['AirFareSearchResponse']['PricedItineraries']['Flights']:
        route = get_route(flights)

        if route not in routes:
            routes.append(route)

    return routes


def display_has_added_new_route(first_json, second_json):
    flag_added_new_route = False

    new_routes = []

    routes_in_first_json = fill_routes(first_json)
    routes_in_second_json = fill_routes(second_json)

    for route in routes_in_first_json:
        if route not in routes_in_second_json:
            flag_added_new_route = True
            new_routes.append(route)

    print('ДОБАВИЛСЯ ЛИ НОВЫЙ МАРШРУТ?\n')

    if flag_added_new_route:
        print('Да, новый(-ые) маршрут(-ы) добавлен(-ы):')
        print(new_routes)
    else:
        print('Нет, новых маршрутов нет')
