import argparse

from pprint import pprint

from class_flight_difference import display_diff_flight_classes
from cost_flight_difference import display_diff_cost_flight
from has_added_new_route import display_has_added_new_route
from parse_xml_to_json import parse_xml_to_json
from route_flight_difference import display_diff_flight_airports
from time_flight_difference import display_diff_route_times


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("first_filename")
    parser.add_argument("second_filename")
    args = parser.parse_args()

    json_data_for_first_file = parse_xml_to_json(args.first_filename)
    json_data_for_second_file = parse_xml_to_json(args.second_filename)

    display_diff_flight_airports(json_data_for_first_file, json_data_for_second_file)
    print()
    display_diff_route_times(json_data_for_first_file, json_data_for_second_file)
    display_diff_cost_flight(json_data_for_first_file, json_data_for_second_file)
    display_diff_flight_classes(json_data_for_first_file, json_data_for_second_file)
    print()
    display_has_added_new_route(json_data_for_first_file, json_data_for_second_file)
