class heap(object):
    heap_size = 10
    def __init__(self):
        self.heap = [0] * heap.heap_size
        self.currentposition = -1
    def insert(self,item):
        if self.isFull():
            print("heap is full.")
            return
        self.currentposition += 1
        self.heap[self.currentposition] = item
        self.fixup(self.currentposition) # to check if heap properties are valid

    def fixup(self,index):
        parentindex = int(index - 1)/2 # from 2i+1
        while parentindex >= 0 and self.heap[parentindex] > self.heap[index]:
            # parentindex >=0 is to iterate until we reach root node
            temp = self.heap[index]
            self.heap[index] = self.heap[parentindex]
            self.heap[parentindex] = temp
            parentindex = int((index -1)/2) #changing value of index because root node changes with each iteration

    def heapsort(self):
        for i in range(0,self.currentposition + 1):
            temp = self.heap[0]
            print(temp)
            self.heap[0] = self.heap[self.currentposition-i] # - i bc items keep decreasing
            self.heap[self.currentposition-i] = temp
            self.fixdown(0,self.currentposition-i-1)
    def fixdown(self,index,upto):
        while index <=upto:
            leftchild = 2*index+1
            rightchild = 2*index+2

            if leftchild < upto:
                childtoswap = None

                if rightchild > upto:
                    childtoswap = leftchild
                else:
                    if self.heap[leftchild] > self.heap[rightchild]:
                        childtoswap = leftchild
                    else: 
                        childtoswap = rightchild
                if self.heap[index] < self.heap[childtoswap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childtoswap]
                    self.heap[childtoswap] = temp
                else:
                    break
                index = childtoswap
            else:
                break





               


    def isFull(self):
        if self.currentposition == heap.heap_size:
            return True
        else: 
            return False
    