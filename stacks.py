class stack():
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return self.stack == []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        data = self.stack[-1] # returns the last element added, -2 would give second last etc
        del self.stack[-1]
        return data
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
#instantiate stack and call methods 
