import os
import csv


def csv_reader(rel_file_path: str):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_file_path = os.path.abspath(os.path.join(root_dir, rel_file_path))

    areas = []
    with open(csv_file_path, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            areas.append(row)

    return areas
