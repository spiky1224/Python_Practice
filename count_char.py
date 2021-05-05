def count_char(s):
  cnt_dict = {}
  s = s.lower()
  for c in s:
    if c in cnt_dict:
      cnt_dict[c] += 1
    else:
      cnt_dict[c] = 1
  return cnt_dict

result = count_char("MyNameIsNobuyukiTsuboi")
print(result)