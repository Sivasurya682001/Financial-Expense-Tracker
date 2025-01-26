import json
import csv

def save_data(text_fields, name_fields, text1_input, result_text):
    data = {
        "initial_value": text1_input.value,
        "result": result_text.value,
        "fields": []
    }
    for name_field, text_field in zip(name_fields, text_fields):
        data["fields"].append({
            "name": name_field.value,
            "amount": text_field.value
        })
    
    # Save data in JSON format
    with open("saved_data.json", "a") as f_json:
        f_json.write(json.dumps(data) + '\n')

    # Save data in CSV format
    with open("saved_data.csv", "a", newline='') as f_csv:
        writer = csv.writer(f_csv)
        for field in data["fields"]:
            writer.writerow([field["name"], field["amount"]])
