import json
import xmltodict


def parse_xml_to_json(filename):
    with open(f'{filename}.xml', 'r') as xml_file:
        json_dict = xmltodict.parse(xml_file.read())
        xml_file.close()

    json_data = json.dumps(json_dict)

    with open(f"{filename}.json", "w") as json_file:
        json_file.write(json_data)
        json_file.close()
    
    json_file = open(f'{filename}.json')
    json_data = json.load(json_file)
    json_file.close()

    return json_data