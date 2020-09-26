class Node(object):
    def __init__(self,data):
        self.data = data
        self.height = 0 # height parameter to store the height of the node so that we can check whether the tree is balanced at every rotation
        self.leftchild = None
        self.rightchild = None
class AVL(object):
    def __init__(self):
        self.root = None
    
    def calcheight(self,node):
        if not node: # if it's a leaf node/ it's a null pointer
            return -1 
        return node.height
    
    def calcbalance( self,node): 
        # if this returns a value > 1, it's a left heavy tree, right rot needed
        # if it returns value < -1, it's a right heavy tree, left rot needed
        if not node:
            return 0
        return self.calcheight(node.leftchild) - self.calcheight(node.rightchild)
    def rotateright(self,node):
        print("rotating the tree to the right at node ",node.data)
        templeftchild = node.leftchild
        tempchild = templeftchild.rightchild
        templeftchild.rightchild = node
        node.leftchild = tempchild

        node.height = max(self.calcheight(node.leftchild),self.calcheight(node.rightchild)) + 1
        #calculating the new height parameter after rotation 
        templeftchild = max(self.calcheight(templeftchild.leftchild),self.calcheight(templeftchild.rightchild)) + 1
        #calculating height of templeftchild that has now become the root child
        return  templeftchild
    
    def rotateleft(self,node):
        print("rotating the tree to the right at node ",node.data)
        temprightchild = node.rightchild
        tempchild = temprightchild.leftchild
        temprightchild.leftchild = node
        node.rightchild = tempchild

        node.height = max(self.calcheight(node.leftchild),self.calcheight(node.rightchild)) + 1
        #calculating the new height parameter after rotation 
        temprightchild = max(self.calcheight(temprightchild.leftchild),self.calcheight(temprightchild.rightchild)) + 1
        #calculating height of templeftchild that has now become the root child
        return temprightchild

    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertnode(data,self.root)
    

    def insertnode(self,data,node):
        if not node:
            return Node(data)

        if data < node.data:
            node.leftchild = self.insertnode(data, node.leftchild)
        else: 
            node.rightchild = self.insertnode(data,node.rightchild)
        
        node.height = max(self.calcheight(node.leftchild),self.calcheight(node.rightchild)) + 1

        return self.settleviolation(data,node)

    def settleviolation(self,data,node):
        balance = self.calcbalance(node)

        if balance > 1 and data < node.leftchild.data: #case 1 : left left heavy
            print("left left heavy situation ...")
            return self.rotateright(node)
        if balance < -1 and data > node.rightchild.data: #case 2 : right right heavy
            print("right right heavy situation ...")
            return self.rotateleft(node)
        if balance > 1 and data > node.leftchild.data:
            print("left right heavy situation ...")
            node.leftchild = self.rotateleft(node.leftchild)
            return self.rotateright(node)
        if balance < -1 and data < node.leftchild.data:
            print("right left heavy situation...")
            node.rightchild = self.rotateleft(node.rightchild)
            return self.rotateright(node)
        return node
    def traverse(self):
        if self.root:
            self.traversal(self.root)

    def traversal(self,node):
        if node.leftchild:
            self.traversal(node.leftchild)
        print(node.data)
        if node.rightchild:
            self.traversal(node.rightchild)
    
    def remove(self,data):
        if self.root:
            self.root = self.removenode(data,self.root)
    def removenode(self,data,node):
        if not node: # if node is a leaf node itself/ root only 
            return node
        if data < node.data:
            node.leftchild = self.removenode(data,node.leftchild)
        elif data > node.data:
            node.rightchild = self.removenode(data,node.rightchild)
        else: #we are AT the node we want to get rid of_ this has three subcases 1) is a leaf node 2) has 1 child 3) has 2 children

            if not node.leftchild and not node.rightchild: #case 1)
                print("removing a leaf node...")
                del node
                return None

            if not node.leftchild: #case 2
                print("removing a node with a right child...")
                temp = node.rightchild
                del node
                return temp
            elif not node.rightchild:#case 3
                print("removing a node with a left child...")
                temp = node.rightchild
                del node
                return temp
            print("removing node with two children...")
            temp = self.getpredecessor(node.leftchild)
            node.data = temp.data # swapping the predecessor data with the node data
            node.leftchild = self.removenode(temp.data,node.leftchild)
        #code to check for balance and settleviolation
    def getpredecessor(self,node):
        if node.rightchild:
            return self.getpredecessor(node.rightchild)
        return node

avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(30)
avl.insert(40)


