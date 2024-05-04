import csv
import os

def text_to_csv(input_folder, output_csv):
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for filename in os.listdir(input_folder):
            if filename.endswith(".txt"):
                file_path = os.path.join(input_folder, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read().strip()  # Read the entire file contents
                    writer.writerow([text])  # Write the contents as a single row

# Example usage:
input_folder = ""
output_csv = "output.csv"
text_to_csv(input_folder, output_csv)
