from heapq import heappop,heapify,heappush
heap = []
nums = [1,2,3,4,-1,-2,-3,-4,0]

for num in nums:
    heappush(heap,num)

while heap:
    print(heappop(heap))

heapify(nums)
print(nums)