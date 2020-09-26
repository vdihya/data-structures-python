class Node(object):
    def __init__(self,name):
        self.name = name
        self.adjacencylist = []
        self.visited = False
        self.predecessor = None #previous vertex in the bfs order
        #use bfs to calc shortest path

class BFS(object):
    def bfs(self,startnode):
        
        queue = [] #bfs uses a queue!
        queue.append(startnode)
        startnode.visited = True

        while queue: #while it's not empty
            actualnode = queue.pop(0) #pop the first item/fifo
            print(actualnode.name) # print the node data since it's equivalent to visiting it
            for n in actualnode.adjacencylist :#go through neighbors of popped node and visit them if unvisited
                if not n.visited:
                    n.visited = True
                    queue.append(n) 
"""enqueue first node onto the queue, print the data and consider it visited,
dequeue the node, go through the adjacency list of the dequeued node, visiting
all the neighboring nodes of the dequeued node, enqueue those nodes onto the queue,
dequeue them and repeat until you empty the queue"""

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node1.adjacencylist.append(node2)
node1.adjacencylist.append(node3)
node2.adjacencylist.append(node4)
node4.adjacencylist.append(node5)
bfs1 = BFS()
bfs1.bfs(node1)