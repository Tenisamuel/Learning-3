import csv
import json

def csv_to_json('Event-Registration.csv', 'Event-Registration.json'):
    data = []

    with open('Event-Registration.csv', mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            data.append(row)

    with open(json_file_path, mode='w', encoding='utf-8') as json_file_path:
        json.dump(data, json_file, indent=4)

    return data