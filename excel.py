import os
import csv
# dir = (r'C:\Users\Tyler\Downloads')
# os.chdir(r'C:\Users\Tyler\Downloads')
with open(r"C:\Users\Tyler\Downloads\dataplay.csv") as f:
    reading_file = csv.reader(f)
    list = []
    for line in reading_file:
        list += line
