import random

def hungman():
  hungman = [
    "-----     ",
    "     |    ",
    "     O    ",
    "    /|\\   ",
    "     |    ",
    "    / \\   ",
    "GAME OVER!"
  ]
  words = ['faa', 'foo', 'ufo', 'git', 'zoo']
  word = words[random.randint(0, 4)]

  print('Guess the mystery word before the Hungman is killed!')

  remain_chars = list(word)      #word_letter ワードを管理
  passed_chars = list('_'*len(word))   #word長分の_を入れる変数
  limit = len(hungman)
  win = False

  for idx in range(0, limit): #hungmanが完成するまで
    print(''.join(passed_chars))         #回答進捗を表示
    for i in range(0, idx):     #Hungmanを表示
      print(hungman[i])
    guess_char = input("Type a letter you guessed : ")
    if guess_char in remain_chars:
      print("Correct!")
      correct_idx = remain_chars.index(guess_char)
      passed_chars[correct_idx] = guess_char
      remain_chars[correct_idx] = '#'
      if '_' not in passed_chars:
        win = True
    else:
      print("Incorrect!")
    if win:
      break
    print('\n')

  if win:
    print("You Win!")
  else:
    print("You Lose!")
    print("Answer : {}".format(word))
    for h in hungman:
      print(h)