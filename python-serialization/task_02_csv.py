import json
import csv


def convert_csv_to_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)

        with open("data.json", 'w', encoding='utf-8') as jf:
            json.dump(data, jf, indent=4)


        return True

    except FileNotFoundError:
        print(f"File {filename} not Found!")
        return False
