import csv
import os

# Data for the CSV
tasks = [
    {"Sl No.": 1, "taskId": "5f127f6f26831d0010e985e5"},
    {"Sl No.": 2, "taskId": "5f127f6c3a6b1000172320ad"},
    {"Sl No.": 3, "taskId": "5f127f699740b80017f9b170"},
    {"Sl No.": 4, "taskId": "5f127f671ab28b001762c204"},
    {"Sl No.": 5, "taskId": "5f127f643a6b1000172320a5"},
    {"Sl No.": 6, "taskId": "5f127f5f3a6b100017232099"},
    {"Sl No.": 7, "taskId": "5f127f5ab1cb1300109e4ffc"},
    {"Sl No.": 8, "taskId": "5f127f55fdc4150010e37244"},
]

# File path for the CSV file
current_directory = os.getcwd()
file_path = f"{current_directory}\ tasks.csv"
print(file_path)
# Writing data to CSV
with open(file_path, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Sl No.", "taskId"])
    writer.writeheader()
    writer.writerows(tasks)

print("CSV file has been created at:", file_path)
