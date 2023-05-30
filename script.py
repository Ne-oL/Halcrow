import os
import csv

# Set the folder path and output file path
folder_path = os.path.dirname(os.path.abspath(__file__))
output_file_path = os.path.join(folder_path, "lithology_table.csv")

# Create the output CSV file and write the header row
with open(output_file_path, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["Borehole_ID", "From", "To", "Lithology_Description"])

    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a CSV file
        if filename.endswith(".csv"):
            # Extract the borehole ID from the file name
            borehole_id = filename.split("_")[0]

            # Open the file and read the lithology data
            with open(os.path.join(folder_path, filename), 'r') as input_file:
                reader = csv.reader(input_file)
                header = next(reader, None)  # get header row, if any
                if header is not None:  # check if file is not empty
                    for row in reader:
                        writer.writerow([borehole_id, row[0], row[1], row[2]])

