import csv

# Read in the CSV file as a list of lists
with open('edgeList3.csv', 'r') as f:
    reader = csv.reader(f)
    edges = [list(map(int, row)) for row in reader]

    #print(edges)

    egdes_as_tuples = [tuple(elem) for elem in edges]
    #print(egdes_as_tuples)