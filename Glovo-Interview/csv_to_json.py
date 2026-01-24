import csv
import json
import sys
import os

csv_file = 'Event-Registration.csv'
json_file = 'Event-Registration.json'
def csv_to_json(csv_file, json_file):
    data = []

    with open(csv_file, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    with open(json_file, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"[+] Successfully converted {csv_file} to {json_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python csv_to_json.py input.csv output.json")
        sys.exit(1)

    csv_file = sys.argv[1]
    json_file = sys.argv[2]

    if not os.path.exists(csv_file):
        print(f"[!] Error: File '{csv_file}' does not exist")
        sys.exit(1)

    csv_to_json(csv_file, json_file)
