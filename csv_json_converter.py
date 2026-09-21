"""
Write a program to read data from a CSV file and convert the data to JSON format. Write the JSON data
to .json output file.
"""
import csv
import json

def convert_csv_to_json(csv_file_path, json_file_path):
    data = []
    
    # Step 1: Open and read the CSV file using DictReader
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Step 2: Convert each row into a dictionary and add to data list
        for row in csv_reader:
            data.append(row)
            
    # Step 3: Write the dictionary data into the output JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
        
    print(f"Successfully converted '{csv_file_path}' to '{json_file_path}'.")

# Example execution
if __name__ == "__main__":
    csv_file = "data.csv"
    json_file = "output.json"
    
    # Helper step: Create a sample CSV file if it doesn't exist
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Branch", "Year", "CGPA"])
        writer.writerow(["Nikhil", "COE", "2", "9.0"])
        writer.writerow(["Sanchit", "COE", "2", "9.1"])
        writer.writerow(["Aditya", "IT", "2", "9.3"])

    # Run conversion
    convert_csv_to_json(csv_file, json_file)

"""
--> Output
Successfully converted 'data.csv' to 'output.json'.
"""