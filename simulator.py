import csv
import numpy as np
import math

def stepDay(nodes):
    for x in nodes:
        x[2] = x[2]+x[1]
    return nodes

def makeStockQueue(nodes, region):
    stockQueue = []
    for x in range(len(nodes)):
        if (nodes[x][1] < 0):
            stockQueue.append([x, abs(nodes[x][2]/nodes[x][1])])
    sortedStockQueue = sorted(stockQueue, key=lambda y: y[1])
    return sortedStockQueue

def makeEmptyQueue(nodes, region):
    emptyQueue = []
    for x in range(len(nodes)):
        if (nodes[x][1] > 0):
            emptyQueue.append([x, nodes[x][2]])
    sortedEmptyQueue = sorted(emptyQueue, key=lambda y: 1/y[1])
    return sortedEmptyQueue

#format: Name, diffday, quantity, region
nodes = []

with open('station.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None) # skip headers
    for row in reader:
        nodes.append([row[0], float(row[12]), 500.0/58.0, -1])

going = 1
days = 0
while(going):
    days = days+1
    nodes = stepDay(nodes)
    stockQueue = makeStockQueue(nodes, -1)
    emptyQueue = makeEmptyQueue(nodes, -1)

    print(stockQueue)
    print(emptyQueue)

    if nodes[stockQueue[0][0]][2] < 0:
        going = 0
    #print nodes
    stockStops = 15
    emptyStops = 15
    stock = 0.0

    for x in range(min(len(emptyQueue), emptyStops)):
        stock = stock + (nodes[emptyQueue[x][0]][2]-3)
        nodes[emptyQueue[x][0]][2] = 3
    for x in range(min(len(stockQueue), stockStops)):
        stock = stock - (stock/min(len(stockQueue), stockStops))
        nodes[stockQueue[x][0]][2] =  nodes[stockQueue[x][0]][2] + stock/min(len(stockQueue), stockStops)

    print(stock)

print(days)
