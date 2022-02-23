#############################################################################
#       PROJECT 1:     SAVVY TRAVELLER
#       GROUP MEMBERS: Shivangi Shakya, Saoni Mustafi, Nick Bidler
#
#       PURPOSE: to compute:
#               (i) what route will maximize the probability to arrive on
#                   time between A and F, and
#               (ii) what city among {A, B, C, D, E, F, G, H} is the most
#                    reliable travel destination.
#
############################################################################
from importlib.resources import contents
import pprint
import ast

# Class Graph encapsulates the functions and helper functions required for
# the computation
class Graph:
    #Initialize the Class
    def __init__(self, graph, visited = {}, path = [], list1 = {}) -> None:
        self.graph = graph
        self.path = path
        self.list1 = list1
        # Set the visited as False for all vertices
        for i in self.graph:
            visited[i] = False
        self.visited = visited

    # Function to print the Graph as an Adjacency List with probabalities
    # of each path
    def printGraph(self):
        pprint.pprint(self.graph)

    # Function to find the Best route for a pair of vertices.
    # Input A as source and F as Destination.
    def BestRoute(self, src, dest):
        self.visited[src]= True
        self.path.append(src)
        prod = 1 # Initialize product with 1

        # If destination is found
        if src == dest:
            #print(path)
            # Loop to compute the product of the probability of paths
            for i in range(1,len(self.path)):
                prod = prod * float(graph[self.path[i-1]][self.path[i]])
            # Join path list to print in the manner
            PathString = '->'.join(self.path)
            # Save the product in the list1 dict for a particular path
            self.list1[PathString] = prod
            prod = 1
        else:
            # Continue Recursion if destination is not found
            for a in graph[src]:
                if self.visited[a] == False and self.graph[src][a] != '0':
                    self.BestRoute(a, dest) # Recursion with next vertex as source
    

        # Pop out one vertex from path to check for another path
        self.path.pop()
        # Set visited to False for another path
        self.visited[src]= False

    # Function to print the Best Route among the list of routes for a
    # pair of vertices.
    def printBestRoute(self, src, dest):
        self.BestRoute(src, dest)

        
        
        print(self.list1)
        # Get the key with maximum value and maximum value
        max_path = max(self.list1, key=self.list1.get)
        max_value = max(self.list1.values())
        print("Max Path: "+ max_path + " === "+ str(max_value))

    # Function to find the most Reliable Destination among all the vertices.
    def ReliableDest(self):
        dict = {}
        vertices = []
        # Save keys in vertices[] list to access those easily
        for key in graph:
            vertices.append(key)

        # Looping to access all the vertices one by one for destination
        for i in range(0,len(vertices)):
            sum = 0
            print()
            print(vertices[i] + ": ") # Print the destination vertex

            # Looping to access all the vertices one by one for source
            for j in range(0, len(vertices)):
                # Check if destination vertex is in the dict of source
                # vertex and source != destination
                if vertices[i] in self.graph[vertices[j]] and i != j:
                    self.BestRoute(vertices[j], vertices[i])
                    print(vertices[j]+" : "+ str(max(self.list1.values())) + " ### route: " + max(self.list1, key=self.list1.get))
                    self.visited[vertices[j]] = False
                    self.list1 = {} # Clearing the contents of list1 dict
                    self.path = [] # Clearing the contents of path list
            # Save the sum of probability of paths in dict of destination
            dict[vertices[i]] = sum 
        print()
        print(dict)
        # Print the Reliable Destination
        print("\nReliable Destination: "+ max(dict, key=dict.get) + " ==> "+ str(max(dict.values())))
        print()

# Main Function
if __name__ == '__main__':
    # graph = {}
    # visited = {}
    # v = int(input("Enter number of vertices: "))

    # print("Enter vertices(keys) : ")
    # for i in range(v):
    #     graph.setdefault(input())

    # print()
    # edges = {}
    # for x in graph:
    #     edges.setdefault(x)

    # for i in graph:
    #     graph[i] = edges.copy()
    #     visited[i] = False

    # print("Enter probability: ")
    # for i in graph:
    #     print("Vertex "+ i + " : ")
    #     for j in graph[i]:
    #         if i==j:
    #             print(j+": 0")
    #             graph[i][j] = 0
    #         else:
    #             var = input(j+": ")
    #             graph[i][j] = var
    #     print()
    # printGraph(graph)

    flname = input("Enter the graph file (graph1.txt/ graph2.txt/ graph3.txt) you want to process: ")
    fl = open(flname, "r")
    graphinput = fl.read()
    graph = ast.literal_eval(graphinput)
    fl.close()
    print(graph)
#     graph = {'A': {'A': 0,
#        'B': '0.8',
#        'C': '0.6',
#        'D': '0',
#        'E': '0',
#        'F': '0.8',
#        'G': '0'},
#  'B': {'A': '0.8',
#        'B': 0,
#        'C': '0',
#        'D': '0.6',
#        'E': '0.9',
#        'F': '0',
#        'G': '0'},
#  'C': {'A': '0.6',
#        'B': '0',
#        'C': 0,
#        'D': '0.7',
#        'E': '0',
#        'F': '0.5',
#        'G': '0'},
#  'D': {'A': '0',
#        'B': '0.6',
#        'C': '0.7',
#        'D': 0,
#        'E': '0',
#        'F': '0',
#        'G': '0'},
#  'E': {'A': '0',
#        'B': '0.9',
#        'C': '0',
#        'D': '0',
#        'E': 0,
#        'F': '0.8',
#        'G': '0.7'},
#  'F': {'A': '0.8',
#        'B': '0',
#        'C': '0.5',
#        'D': '0',
#        'E': '0',
#        'F': 0,
#        'G': '0.9'},
#  'G': {'A': '0',
#        'B': '0',
#        'C': '0',
#        'D': '0',
#        'E': '0.7',
#        'F': '0.9',
#        'G': 0},
#  }

    # for i in graph:
    #     visited[i] = False
    # path=[]
    # list1 = {}
    src = str(input("Enter source vertex: ")).upper() #Input A as per example
    dest = str(input("Enter destination vertex: ")).upper() #Input F as per example

    g = Graph(graph)
    g.printBestRoute(src, dest)
    g.ReliableDest()