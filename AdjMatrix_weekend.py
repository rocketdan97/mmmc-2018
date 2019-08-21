import csv
import numpy as np

graph = []

with open('station.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        # fill first row with headers
        graph.append([row[0]])

# fill rest of graph with zero
for x in range(len(graph)):
    graph[x].extend([0]*(len(graph)))

with open('trip.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None) # skip headers

    count = 0
    for row in reader:
        for x in range(len(graph)):
            if(row[8] != "Female"): # P A R A M E T E R S
                count = count + 1
                if row[5] == graph[x][0]:
                    for y in range(len(graph)):
                        if row[6] == graph[y][0]:
                            graph[x][y+1] = graph[x][y+1]+1
                            break
                    break

with open('outputAdjacency_male.csv', mode='w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"')
    row1 = [0]

    # write header
    for col in range(len(graph)):
        row1.append(graph[col][0])
    writer.writerow(row1)

    # write body
    for row in range(len(graph)):
        newRow = [graph[row][0]]
        for col in range(1, len(graph)+1):
            newRow.append(graph[row][col])
        writer.writerow(newRow)
