def print_repeat(word, times):
  if times < 0:                #1 end_condition　終了条件
    return
  print(word)
  times -= 1                  #2 stage_change　状態変化
  print_repeat(word, times)   #3 recursive_calling　再帰呼び出し

print_repeat('Chihaya', 12)