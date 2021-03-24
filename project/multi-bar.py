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
dates = []
citrus = []
grapefruits = []
plantains = []
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row=next(csv_reader)
    for row in csv_reader:
        years.append(row[2])
        dates.append(float(row[4]))
        citrus.append(float(row[5]))
        grapefruits.append(float(row[10]))
        plantains.append(float(row[12]))

barWidth=.25

br1 = np.arange(len(years)) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 
br4 = [x + barWidth for x in br3] 
br5 = [x + barWidth for x in br4]

plt.bar(br1, dates, color ='brown', width=barWidth, label="Dates") 
plt.bar(br2, citrus, color="orange",  width=barWidth, label="Other Citrus")
plt.bar(br3, grapefruits, color="pink", width=barWidth,  label="Grapefruits")
plt.bar(br4, plantains, color ='yellow', width=barWidth, label="Plantains") 

plt.ylabel('Consumption in KG')
plt.xlabel('Year 2000s')
plt.title('Average US Consumption: Other Fruits')
plt.legend(loc="best")
plt.grid()
plt.show()