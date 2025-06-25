from collections import deque

queue=deque(['Heer','Meet','Shobhana'])
print(queue)
queue.append('Kiran') 
print(queue)
queue.popleft()

print(queue)