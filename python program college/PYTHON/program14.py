#a program that reads a CSV file and prints the data in a tabular format
import csv
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
#output
#['Name', 'Age', 'City']
#['John Doe', '25', 'San Francisco']
#['Jane Smith', '30', 'New York']
