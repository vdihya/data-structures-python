#uses stack with recursion
class Node(object):
    def __init__(self,name):
        self.name = name
        self.adjacencylist = []
        self.predecessor = None # not used but important ig??
        self.visited = False
        
class DFS(object):

    def dfs(self,node):
        node.visited = True
        print(node.name)

        for n in node.adjacencylist:
            if not n.visited:
                self.dfs(n)


"""
class DFS(object):
    def dfs(self,startnode):
        stack = []
        stack.append(startnode)
        startnode.visited = True
        while stack:
            temp = stack.pop()
            print(temp.name)

            for n in temp.adjacencylist:
                if not n.visited:
                    n.visited = True
                    stack.append(n)
"""
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node1.adjacencylist.append(node2)
node1.adjacencylist.append(node3)
node2.adjacencylist.append(node4)
node4.adjacencylist.append(node5)
dfs = DFS()
dfs.dfs(node1)