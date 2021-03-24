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
grapes = []
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row=next(csv_reader)
    for row in csv_reader:
        years.append(row[2])
        grapes.append(float(row[10]))

print(years)
print(grapes)

plt.scatter(years, grapes, color = "purple", label = "grapes")
plt.ylabel('Consumption in KG')
plt.xlabel('Year')
plt.title('Average US Grape Consumption')
plt.grid()
plt.show()