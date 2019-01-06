import networkx as nx

"""
Computes DISTANCE AND PATH from startNode to the every other node in graph using Dijkstras Algorithm.

Arguments: G - reference to networkx graph, startNode - node from which search starts
Return: visited - dictionary of all nodes and their distance from startNode 
        path - dictionary of visited nodes and path to the from startNode

Note: G must be
        - weighted (weights must be positive)
        - weights of edges can't be large number (using 1000 instead of infinity)
      If G has more components
        - unreachable components won't appear in path dictionary
        - values of unreachable components in visited dictionary is 1000 (my infinity)
"""
def dijkstrasAlgorithm(G, startNode):
    # initialize dictionaries
    visited = {startNode : 0}
    distance = {}
    path = dict()
    path[startNode] = [startNode]

    # assign "infinity" values to all nodes, except startNode
    for node in G.nodes():
        if node == startNode:
            continue
        distance[node] = 1000

    # select first node
    node = startNode
    # repeat while every node hasn't been visited
    while True:
        # update values of node’s neighbors
        for neighbor in G.neighbors(node):
            # check if neighbor has not been visited
            nodeVisited = True
            for n in distance:
                if n == neighbor:
                    nodeVisited = False
                    break
            if nodeVisited == True:
                continue
            # compute new distance
            newDistance = visited[node] + G.edges[node, neighbor]['weight']
            if newDistance < distance[neighbor]:
                distance[neighbor] = newDistance
                # compute new path
                newPath = path[node].copy()
                newPath.append(neighbor)
                path[neighbor] = newPath

        # exit when every node has been visited
        if bool(distance) == False:
            break
        # choose new node
        smallestValue = 1000
        for n in distance:
            if distance[n] <= smallestValue:
                smallestValue = distance[n]
                node = n
        # move node to visited
        visited.update({node : smallestValue})
        # delete node in distance
        del distance[node]

    print(visited)
    print(path)

    return (visited, path)
