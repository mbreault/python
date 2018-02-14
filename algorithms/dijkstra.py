## Dijkstra's https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
## Written based on pseudo code in wiki page
## 2/14/2018  Know it can be improved.  WIP


import sys
import operator

def get_path(steps,start,end,path = []):
    if start == end:
        path.append(start)
        path.reverse()
        return path
    else:
         path.append(end)
         path = get_path(steps,start,steps[end],path)
         return path

## method 1 non-recursive
def dijkstra(graph,start,end,dist,prev,unvisited):

    comparisons = 0
    while unvisited:
        comparisons += 1

        ## set starting point
        if start in unvisited:
            vertex = start
            unvisited.remove(start)
        else:
            vertex = unvisited.pop(0)

        neighbors = graph[vertex]    

        for neighbor in neighbors:
            print(vertex,neighbor,dist,prev)
            if neighbor in unvisited:
                distance = neighbors[neighbor]
                comparisons += 1
                alt = dist[vertex] + distance
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prev[neighbor] = vertex
    
    print (comparisons)
    return dist, prev   

graph = {
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            's': {'a': 2, 'b': 1},
            't': {'c': 3, 'd': 5}
        }

## init
start = 'a'
end = 't'
dist = {}
prev = {}
unvisited = []

## init
for vertex in graph:
    dist[vertex] = sys.maxsize
    prev[vertex] = None
    unvisited.append(vertex)

dist[start] = 0

distances, steps =  dijkstra(graph,start,end,dist,prev,unvisited)

print("The shortest distance from {0} to {1} is {2} following the path {3}".format(start,end,distances[end],get_path(steps,start,end)))

