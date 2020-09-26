class Node(object):
    def __init__(self,character):
        self.character = character #every node is assigned a character
        self.leftnode = None
        self.middlenode = None
        self.rightnode = None
        self.value = 0

class TST(object):

    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self.putitem(self.root, key, value, 0)

    def putitem(self, node, key, value, index): #key is what youre inserting #index keeps track of char of key
        
        c = key[index]

        if node == None: #creating a node for the character if it doesnt exist
            node = Node(c)

        if c < node.character:
            node.leftnode = self.putitem(node.leftnode,key,value,index)

            # recursive to insert each char in key within
        elif c > node.character:
            node.rightnode = self.putitem(node.rightnode,key,value,index)

        elif index < len(key) - 1: #index of last character so as to add in the middle node
            node.middlenode = self.putitem(node.middlenode,key,value,index+1)
            # the index is incremented only when traversing in the middle
             #index is not incremented when traversing to left or right !
        else: 
            node.value = value # adding value at the end after reaching last node
        
        return node

    def get(self,key):
        
        node = self.getitem(self.root,key,0)
        
        if node == None: #if the returned node from the function is null then the key being looked for is not present
            return -1 #given key is not present in the dictionary
        
        return node.value
    
    def getitem(self,node,key,index):
        
        if node == None:
            return None
        
        c = key[index]

        if c < node.character:
            return self.getitem(node.leftnode,key,index)
        
        elif c > node.character:
            return self.getitem(node.rightnode,key,index)
        
        elif index < len(key) - 1: # c == node.character means u have to recursively mmove through the middle and then move after that 
            return self.getitem(node.middlenode,key,index+1)
        
        else: # youre AT the node required, so return the value since the key has been found and does exits
            return node
            
            
            
if __name__ == "__main__":
    tst = TST()
    tst.put('apple',100)
    tst.put('orange',200)
    print(tst.get("apple"))

