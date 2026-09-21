"""
Write a program to read data from a CSV file and convert the data to JSON format. Write the JSON data
to .json output file.
"""
import csv
import json

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    with open(csvFilePath, encoding="utf-8") as csvf:
        csvReader = csv.DictReader(csvf)

        for row in csvReader:
            jsonArray.append(row)

    with open(jsonFilePath, "w", encoding="utf-8") as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


csvFilePath = "data.csv"
jsonFilePath = "data.json"

csv_to_json(csvFilePath, jsonFilePath)

print("CSV file successfully converted to JSON.")
"""
--> Output
CSV file successfully converted to JSON.

[In data.json file, the output will be:]
[
    {
        "a": "25",
        "b": "84",
        "c": "com"
    },
    {
        "a": "41",
        "b": "52",
        "c": "org"
    },
    {
        "a": "58",
        "b": "79",
        "c": "io"
    },
    {
        "a": "93",
        "b": "21",
        "c": "co"
    }
]
"""