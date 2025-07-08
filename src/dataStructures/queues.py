from collections import deque
from time import process_time_ns

queue = deque([1,2,3])
queue.pop()
queue.appendleft(5)
queue.append(5)
print(queue)

