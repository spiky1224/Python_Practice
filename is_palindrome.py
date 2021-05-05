def is_palindrome(word):
  word = word.lower()
  return word[::-1] == word


s1 = "Abcdeedcba"
s2 = "Abedeedcba"
print(is_palindrome(s1))
print(is_palindrome(s2))