import matplotlib.pyplot as plt
import csv

names = []
amounts = []

with open('saved_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        if not row:  # Skip any empty rows
            continue
        if row[0] == 'Income':  # Stop processing before Income/Result
            break
        names.append(row[0])
        amounts.append(float(row[1]))

plt.bar(names, amounts)
plt.xlabel('Name')
plt.ylabel('Amount')
plt.title('Bar Chart of Names and Amounts')
plt.show()
