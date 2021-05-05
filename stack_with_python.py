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


st = Stack()
s = 'Yesterday'
r = ""
for i in range(len(s)):
  st.push(s[i])
while st.size() > 0:
  r += st.pop()
print(r)

list = [1, 2, 3, 4, 5]
new_list = []
for i in list:
  st.push(i)
while not st.is_empty():
  new_list.append(st.pop())
print(new_list)