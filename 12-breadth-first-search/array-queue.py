# python3

from collections import deque

class Queue:
  # constructor creates a list
  def __init__(self):
    self.queue = list()

  # adding elements to queue
  def enqueue(self, data):
    if data not in self.queue:
      self.queue.insert(0, data)
      print("%s %s" %(data, 'queued!',))
    return False

  def dequeue(self):
    if len(self.queue) > 0:
      item = self.queue.pop()
      print("%s %s" %(item, 'dequeued!',))
    return ("Queue Empty!")

  # getting the size of the queue
  def size(self):
    return len(self.queue)

myQueue = Queue()

for i in range(1, 11):
  myQueue.enqueue(i)

while myQueue.size() > 0:
  myQueue.dequeue()
