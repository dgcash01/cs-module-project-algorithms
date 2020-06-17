#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(value, weight, capacity):
    # Your code here

    n = len(value) - 1

    m = [[-1]*(capacity + 1) for _ in range(n + 1)]

    return knapsack_solver(value, weight, m, n, capacity)

def knapsack_solver(value, weight, m, i, w):

    if m[i][w] >= 0:
        return m[i][w]
 
    if i == 0:
        q = 0
    elif weight[i] <= w:
        q = max(knapsack_solver(value, weight,
                                m, i - 1 , w - weight[i])
                + value[i],
                knapsack_solver(value, weight,
                                m, i - 1 , w))
    else:
        q = knapsack_solver(value, weight,
                            m, i - 1 , w)
    m[i][w] = q
    return q
 
 
n = int(input('Enter number of items: '))
value = input('Enter the values of the {} item(s) in order: '
              .format(n)).split()
value = [int(v) for v in value]
value.insert(0, None) # so that the value of the ith item is at value[i]
weight = input('Enter the positive weights of the {} item(s) in order: '
               .format(n)).split()
weight = [int(w) for w in weight]
weight.insert(0, None) # so that the weight of the ith item is at weight[i]
capacity = int(input('Enter maximum weight: '))
 
ans = knapsack(value, weight, capacity)
print('The maximum value of items that can be carried:', ans)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')