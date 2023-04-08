# ITM 200 - Optional Project
# Anthony Ly - 500905642

import csv
import matplotlib.pyplot as plt

# Reads file and calculates the total sales for each year
with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    sales_data = list(csv_reader)

total_sales = []
years = []
for i in range(len(sales_data)):
    year_sales = sum([int(sales_data[i][j]) for j in range(1, len(header))])
    total_sales.append(year_sales)
    years.append(int(sales_data[i][0]))

# Write total sales for each year to stats.txt
with open('stats.txt', mode='w') as file:
    for i in range(len(total_sales)):
        file.write(f"{years[i]}: {total_sales[i]}\n")

# Plot total sales for each year
plt.bar(years, total_sales)
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.title('Total Sales per Year')
plt.show()

# Calculate and write total sales for first 6 months of 2021 and 2022 to stats.txt
sales_2021 = [int(sales_data[9][i]) for i in range(1, 7)]
sales_2022 = []
for i in range(1, 7):
    try:
        sales_2022.append(int(sales_data[10][i]))
    except:
        sales_2022.append(0)

total_sales_2021 = sum(sales_2021)
total_sales_2022 = sum(sales_2022)

with open('stats.txt', mode='a') as file:
    file.write(f"Total Sales in first 6 months of 2021: {total_sales_2021}\n")
    file.write(f"Total Sales in first 6 months of 2022: {total_sales_2022}\n")

# Calculate and write sales growth rate to stats.txt
SGR = (total_sales_2022 - total_sales_2021) / total_sales_2022
with open('stats.txt', mode='a') as file:
    file.write(f"Sales Growth Rate: {SGR:.2%}\n")

# Calculate and plot estimated sales for last 6 months of 2022
sales_2022_estimated = []
for i in range(7, 13):
    sales_2022_estimated.append(int(sales_data[9][i]) + int(sales_data[9][i]) * SGR)

months = header[1:]
months_2022 = [f"{m} 2022" for m in months[6:]]

plt.barh(months_2022, sales_2022_estimated)
plt.xlabel('Estimated Sales')
plt.title('Estimated Sales for Last 6 Months of 2022')
plt.show()

# Write estimated sales for last 6 months of 2022 to stats.txt
with open('stats.txt', mode='a') as file:
    file.write("Estimated Sales for Last 6 Months of 2022:\n")
    for i in range(6):
        file.write(f"{months_2022[i]}: {sales_2022_estimated[i]:.0f}\n")
