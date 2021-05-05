def is_anagram(word1, word2):
  word1 = word1.lower()
  word2 = word2.lower()
  return sorted(word1) == sorted(word2)

print(is_anagram('Iceman', 'Cinema'))
print(is_anagram('Ookinakuri', 'Kiokunairo'))
print(is_anagram('Abcc', 'Cabb'))