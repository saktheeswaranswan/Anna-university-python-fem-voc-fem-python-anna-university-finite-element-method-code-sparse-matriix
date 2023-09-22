import csv
import random

# Define the input and output file names
input_file = 'NCAcsv.csv'
output_file = 'Ncaaaoutput.csv'

# Read the CSV file and store data
data = []
with open(input_file, 'r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        data.append(row)

# Shuffle values in the 2nd and 3rd columns for each row
for row in data:
    if len(row) >= 3:
        row[1:3] = random.sample(row[1:3], 2)

# Write the shuffled data to a new CSV file
with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)

print("Shuffling complete. Check 'output.csv'")

