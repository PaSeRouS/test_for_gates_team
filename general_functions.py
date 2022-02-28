def fill_flight_airports(flights):
    flight_ways = []

    for flight in flights['OnwardPricedItinerary']['Flights']['Flight']:
        if type(flight) == str:
            if flight == 'Source':
                flight_source = flights['OnwardPricedItinerary']['Flights']['Flight']['Source']
            elif flight == 'Destination':
                flight_destination = flights['OnwardPricedItinerary']['Flights']['Flight']['Destination']
                flight_ways.append(merge_values(flight_source, flight_destination))
        else:
            flight_source = flight['Source']
            flight_destination = flight['Destination']
            flight_ways.append(merge_values(flight_source, flight_destination))
    
    return flight_ways


def merge_values(source, destination):
    return f'{source}-{destination}'


def merge_flight_time(departure, arrival):
    return f'{departure} : {arrival}'


def fill_flight_classes(flights):
    flight_classes = []

    for flight in flights['OnwardPricedItinerary']['Flights']['Flight']:
        if type(flight) == str:
            if flight == 'Class':
                flight_classes.append(flights['OnwardPricedItinerary']['Flights']['Flight']['Class'])
        else:
            flight_classes.append(flight['Class'])
    
    return flight_classes


def fill_flight_data(json, func):
    returned_data = []

    for flights in json['AirFareSearchResponse']['PricedItineraries']['Flights']:
        flight_data = func(flights)

        if flight_data not in returned_data:
            returned_data.append(flight_data)

    return returned_data


def get_cost_flight(flights):
    flight_price_info = {}
    flight_ways = []

    for flight in flights['OnwardPricedItinerary']['Flights']['Flight']:
        if type(flight) == str:
            if flight == 'Source':
                flight_source = flights['OnwardPricedItinerary']['Flights']['Flight']['Source']
            elif flight == 'Destination':
                flight_destination = flights['OnwardPricedItinerary']['Flights']['Flight']['Destination']
                flight_ways.append(merge_values(flight_source, flight_destination))
        else:
            flight_source = flight['Source']
            flight_destination = flight['Destination']
            flight_ways.append(merge_values(flight_source, flight_destination))

    flight_price_info['flight'] = flight_ways

    for price in flights['Pricing']['ServiceCharges']:
        if price['@type'] == 'SingleAdult' and price['@ChargeType'] == 'TotalAmount':
            flight_price_info['price'] = price['#text']
    
    return flight_price_info


def fill_cost_flights(json, func):
    cost_flights = []

    for flights in json['AirFareSearchResponse']['PricedItineraries']['Flights']:
        cost_flight = func(flights)
        cost_flights.append(cost_flight)

    return cost_flights


def splitting_list(first_list, second_list):
    data_only_in_first_list = []
    data_only_in_second_list = []
    data_in_both_lists = []

    for elem in first_list:
        if elem not in second_list:
            data_only_in_first_list.append(elem)

    for elem in second_list:
        if elem not in first_list:
            data_only_in_second_list.append(elem)

    for elem in first_list:
        if elem in second_list:
            data_in_both_lists.append(elem)

    return data_only_in_first_list, data_only_in_second_list, data_in_both_lists


def compare_numbers_for_min(min_number, new_number):
    if not min_number or new_number < min_number:
        return new_number
    else:
        return min_number


def compare_numbers_for_max(max_number, new_number):
    if not max_number or new_number > max_number:
        return new_number
    else:
        return max_number


def fill_cost_info(flight_costs, flight_route):
    min_cost, max_cost, sum_cost, total_flights = 0, 0, 0, 0

    for cost in flight_costs:
        if cost['flight'] == flight_route:
            route = ','.join(flight_route)
            route_cost = float(cost['price'])

            min_cost = compare_numbers_for_min(min_cost, route_cost)
            max_cost = compare_numbers_for_max(max_cost, route_cost)
            sum_cost += route_cost
            total_flights += 1

    average_cost = sum_cost/total_flights

    return min_cost, max_cost, average_cost, route


def fill_flights_times(json):
    flights_times = []

    for flights in json['AirFareSearchResponse']['PricedItineraries']['Flights']:
        flight_time = get_flights_times(flights)
        flights_times.append(flight_time)

    return flights_times


def get_flights_times(flights):
    flight_time_info = {}
    flight_ways = []

    flag_dep = False

    for flight in flights['OnwardPricedItinerary']['Flights']['Flight']:
        if type(flight) == str:
            if flight == 'Source':
                flight_source = flights['OnwardPricedItinerary']['Flights']['Flight']['Source']
            elif flight == 'Destination':
                flight_destination = flights['OnwardPricedItinerary']['Flights']['Flight']['Destination']
                flight_ways.append(merge_values(flight_source, flight_destination))
            elif flight == 'DepartureTimeStamp':
                if not flag_dep:
                    flight_departure= flights['OnwardPricedItinerary']['Flights']['Flight']['DepartureTimeStamp']
                    flag_dep = True
            elif flight == 'ArrivalTimeStamp':
                flight_arrival = flights['OnwardPricedItinerary']['Flights']['Flight']['ArrivalTimeStamp']
        else:
            flight_source = flight['Source']
            flight_destination = flight['Destination']
            flight_ways.append(merge_values(flight_source, flight_destination))

            if not flag_dep:
                flight_departure = flight['DepartureTimeStamp']
                flag_dep = True

            flight_arrival = flight['ArrivalTimeStamp']

    flight_time = merge_flight_time(flight_departure, flight_arrival)

    flight_time_info['Flight'] = flight_ways
    flight_time_info['Times'] = flight_time
    
    return flight_time_info