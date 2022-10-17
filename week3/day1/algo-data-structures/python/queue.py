class Queue:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
  def __init__(self):
    self.total = None
    self.queue = []


  def enqueue(self, data):
    # write your code to add data to the Queue following FIFO and return the Queue
    self.queue.append(data)

  def dequeue(self):
    # write your code to removes the data to the Queue following FIFO and return the Queue
    del self.queue[0]

  def size(self):
    # write your code that returns the size of the Queue
    self.total = len(self.queue)


new_queue = Queue()

new_queue.enqueue(3)
new_queue.enqueue(1)
new_queue.enqueue(8)
new_queue.enqueue(4)
new_queue.dequeue()
new_queue.size()

print(new_queue.queue)
print(new_queue.total)