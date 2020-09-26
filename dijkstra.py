import sys
import heapq

class Edge(object):
    def __init__(self,weight,startvertex,targetvertex):
        self.weight = weight
        self.startvertex = startvertex
        self.targetvertex = targetvertex

class Node(object):
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.predecessor = None
        #to keep track from WHICH vertex the path is coming from to the targext vertex
        self.adjacencylist = []
        self.mindistance = sys.maxsize
        #min distance from source vertex is initially infinity

    def __cmp__(self,othervertex): #method to select the minimum distance from the heap
        return __cmp__(self.mindistance,othervertex.mindistance)
    
    def __lt__(self,other):
        selfpriority = self.mindistance
        otherpriority = other.mindistance
        return selfpriority < otherpriority