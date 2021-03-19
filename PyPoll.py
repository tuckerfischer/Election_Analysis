import csv
import os.path
import os

file_to_load = os.path.join("resources", "election_results.csv")

#with open(file_to_load) as election_data:
#    print(election_data)

dash = []

x= "Counties in the Election"
for i in x:
    dash.append("-")
dash2 = ''.join(dash)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)