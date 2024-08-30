import random
print("HANGMAN GAME\n")
print("Rules:\n1.You have to guess the letters for a randomly chosen word.\n2.There are 6 total chances\n3.Each wrong guess will lead you closer to be hanged")
words=["ANDHRA PRADESH","ARUNACHAL PRADESH","ASSAM","BIHAR","CHHATTISGARH","GOA","GUJARAT","HARYANA","HIMACHAL PRADESH","JHARKHAND","KARNATAKA","KERALA","MADHYA PRADESH","MAHARASHTRA","MANIPUR","MEGHALAYA","MIZORAM","NAGALAND","ODISHA","PUNJAB","RAJASTHAN","SIKKIM","TAMIL NADU","TELANGANA","TRIPURA","UTTAR PRADESH","UTTARAKHAND","WEST BENGAL","CHANDIGARH","LAKSHADWEEP","DELHI","PUDUCHERRY","LADAKH","JAMMU AND KASHMIR"]
while True:
  word=random.choice(words)
  total_chances=6
  guessed_word=""
  for i in word:
    if i==" ":
      guessed_word+=" "
    else:
      guessed_word+="_"
  display=0
  Graphics = ['''
    +---+
    |   |
        |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
  /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
  /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
  /|\  |
  /    |
        |
  =========''', '''
    +---+
    |   |
    O   |
  /|\  |
  / \  |
        |
  =========''']

  print(Graphics[display])
  print("Your word is:\n")
  while(total_chances!=0):
      print(guessed_word)
      letter=input("Guess a letter: ").upper()
      if letter in word:
          for i in range(len(word)):
              if word[i]==letter:
                  guessed_word=guessed_word[:i]+letter+guessed_word[i+1:]
          if(guessed_word==word):
              print(word)
              print("Congratulations, you won !!!")
              break
      else:
          total_chances-=1
          print("Incorrect guess\nChances left: ",total_chances)
          display+=1
          print(Graphics[display])
  else:
      print("You lose\nAll chances exhausted\nThe correct word is : ",word)
  x=input("Another round?(Yes/No) : ").upper()
  if(x=="NO"):
    break


