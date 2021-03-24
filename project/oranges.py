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
oranges = []
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row=next(csv_reader)
    for row in csv_reader:
        years.append(row[2])
        oranges.append(float(row[6]))

print(years)
print(oranges)

plt.plot(years, oranges, marker = "o", c = "orange")
plt.title("Average US Orange Consumption")
plt.xlabel("Year")
plt.ylabel("Consumption in KG")

plt.show()