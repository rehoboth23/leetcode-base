from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.connections = []

    def connect(self, connection):
        self.connections.append(connection)


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        nodes = {}
        freq = {}
        for c in connections:
            x, y = c[0], c[1]

            if x not in nodes:
                x_node = Node(x)
                nodes[x] = x_node
            if y not in nodes:
                y_node = Node(y)
                nodes[y] = y_node

            nodes[x].connect(c)
            freq[x] = 1 if x not in freq else freq[x] + 1
            nodes[y].connect(c)
            freq[y] = 1 if y not in freq else freq[y] + 1

        res = []
        print(freq)
        for node in freq:
            if freq[node] == 1:
                res.append(nodes[node].connections[0])
        return res



