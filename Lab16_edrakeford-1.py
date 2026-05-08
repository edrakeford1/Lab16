"""
Program Name: Lab16_edrakeford-1.py

Author: Elijah Drakeford

Purpose: This program that reads the OHRU.csv file, which contains Ohio's unemployment rate since 1976.
and parses the data to create a time-series line plot using matplotlib.

Starter Code: None

Date: May 8, 2026
""" 

import csv
from datetime import datetime
import matplotlib.pyplot as plt

# data lists
dates = []
unemp_rates = []

# reading CSV file
try:
    with open("OHUR.csv", "r", newline="") as csv_file:
        reader = csv.reader(csv_file)

        header = next(reader)

        # enumerate() for header
        for index, column_name in enumerate(header):
            print(f"Column {index}: {column_name}")

        # remaining rows
        for row in reader:
            try:
               
                # convertinb date string and unemployement rate
                date = datetime.strptime(row[0], "%Y-%m-%d")
                rate = float(row[1])

                # store data in lists
                dates.append(date)
                unemp_rates.append(rate)

            except ValueError:
                print(f"Skipping invalid row: {row}")

except FileNotFoundError:
    print("Error: OHUR.csv file not found.")
    exit()

# creating the plot
plt.plot(dates, unemp_rates, color="blue")

# title and labels
plt.title("Ohio Unemployment (by Month): 1976 - 2022")
plt.xlabel("Date")
plt.ylabel("Unemp Rate")

plt.grid(True)

# save plot
plt.savefig("ohio_unemployment.png")

# display plot
plt.show()