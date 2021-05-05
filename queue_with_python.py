class Queue:
  def __init__(self):
    self.items = []
  
  def enqueue(self, item):
    self.items.insert(0, item)
  
  def dequeue(self):
    return self.items.pop()

  def is_empty(self):
    return self.items == []
  
  def size(self):
    return len(self.items)

q = Queue()
print(q.is_empty())
q.enqueue('Misa')
print(q.size())
q.enqueue(1234)
print(q.size())
print(q.is_empty())
print(q.dequeue())
print(q.size())