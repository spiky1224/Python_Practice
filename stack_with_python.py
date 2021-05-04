class Stack:
  def __init__(self):
    self.items = []
  
  def is_empty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)
  
  def pop(self):
    return self.items.pop()
  
  def peek(self):
    return self.items[-1]
  
  def size(self):
    return len(self.items)


flase = 'Galaxi Express 999'
esalf = ''
s = Stack()
for f in flase:
  s.push(f)
while s.size() > 0:
  esalf += s.pop()
print(esalf)