import csv
import matplotlib.pyplot as plt

filename = 'fruit-type.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

years = []
oranges = []
citrus = []
lemons = []
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row=next(csv_reader)
    for row in csv_reader:
        years.append(row[2])
        oranges.append(float(row[7]))
        citrus.append(float(row[6]))
        lemons.append(float(row[9]))

plt.scatter(years, oranges, color='orange',label="Oranges")
plt.scatter(years, lemons, color='yellow',label="Lemons/Limes")
plt.scatter(years, citrus, color='green', label="Other Citrus")
plt.ylabel('Consumption in Kg')
plt.xlabel('Year')
plt.title('US Citrus Consumption')
plt.legend(loc='best')
plt.grid()

plt.show()