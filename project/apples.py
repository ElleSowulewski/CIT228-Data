import csv
import matplotlib.pyplot as plt
import numpy as np

filename = 'fruit-type.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

years = []
apples = []
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row=next(csv_reader)
    for row in csv_reader:
        years.append(row[2])
        apples.append(float(row[7]))

print(years)
print(apples)

plt.bar(years, apples, color ='red', width = 0.5) 
plt.title("Average US Apple Consumption")
plt.xlabel("Year")
plt.ylabel("Consumption in KG")

plt.show()