import time
import random

class Queue:
  def __init__(self):
    self.persons = []
  
  def is_empty(self):
    return self.persons == []

  def enqueue(self, person):
    self.persons.insert(0, person)
  
  def dequeue(self):
    return self.persons.pop()
  
  def size(self):
    return len(self.persons)


def simulate_line(to_start, tp_max):  #to_start:映画が始まるまでの時間　tp_max:チケット購入最大時間
  line = Queue()
  num = 10                            #行列の人数
  t_sold = 0
  for i in range(0, num):
    line.enqueue('person' + str(i))
  now = int(time.time())
  limit = now + to_start

  while int(time.time()) < limit and not(line.is_empty()):
    print(line.dequeue())
    time.sleep(random.randint(1, tp_max))
    t_sold += 1

  if line.is_empty():
    print("Sold out!")
  else:
    print("{} copies sold.".format(t_sold))

simulate_line(30, 8)