class Node(object):
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertnode(data,self.root)
    
    def insertnode(self,data,node):
        if data < node.data:
            if node.leftchild:
                self.insertnode(data,node.leftchild)
            else:
                node.leftchild = Node(data)
        else:
            if node.rightchild:
                self.insertnode(data,node.rightchild)
            else:
                node.rightchild = Node(data)
    def getminvalue(self):
        if self.root:
            return self.getmin(self.root)

    def getmin(self,node):
        if node.leftchild:
            return self.getmin(node.leftchild)
        return node.data
    def getmaxvalue(self):
        if self.root:
            return self.getmax(self.root)
    def getmax(self,node):
        if node.rightchild:
            return self.getmax(node.rightchild)
        return node.data

    def intraversal(self):
        if self.root:
            return self.inorder(self.root)
    def inorder(self,node):
        if node.leftchild:
            self.inorder(node.leftchild)
        print(node.data)
        if node.rightchild:
            self.inorder(node.rightchild)
    def potraversal(self):
        if self.root:
            return self.postorder(self.root)
    def postorder(self,node):
        if node.leftchild:
            self.postorder(node.leftchild)
        if node.rightchild:
            self.postorder(node.rightchild)
        print(node.data)
    def pretravsersal(self):
        if self.root:
            return self.preorder(self.root)
    def preorder(self,node):
        print(node.data)
        if node.leftchild:
            self.preorder(node.leftchild)
        if node.rightchild:
            self.preorder(node.rightchild)
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
    def getpredecessor(self,node):
        if node.rightchild:
            return self.getpredecessor(node.rightchild)
        return node

bst = BST()
bst.insert(10)
bst.insert(12)
bst.insert(-1)
bst.insert(34)
bst.insert(100)
print(bst.getmaxvalue())
print(bst.getminvalue())
print("inorder:")
bst.intraversal()
print("postorder:")
bst.potraversal()
print("preorder:")
bst.pretravsersal()
bst.remove(10)
bst.remove(34)
bst.remove(100)


