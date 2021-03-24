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
bananas = []
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row=next(csv_reader)
    for row in csv_reader:
        years.append(row[2])
        bananas.append(float(row[3]))

print(years)
print(bananas)

plt.scatter(years, bananas, color = "yellow", label = "bananas")
plt.ylabel('Consumption in KG')
plt.xlabel('Year')
plt.title('Average US Banana Consumption')
plt.grid()
plt.show()