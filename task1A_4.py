fin1 = open('Book1.txt')
fin2 = open('Book2.txt')
fin3 = open('Book3.txt')
def character_word_count():
  d1={}
  d2={}
  d3={}
  for line in fin1:
    line=line.strip().lower()
    for word in line.split():
      if word not in d1:
        d1[word] = len(word)
  #this is book2
  for line in fin2:
    line=line.strip().lower()
    for word in line.split():
      if word not in d2:
        d2[word] = len(word)
  #this is book3
  for line in fin3:
    line=line.strip().lower()
    for word in line.split():
      if word not in d3:
        d3[word] = len(word)


  print(d1)
  print(d2)
  print(d3)

character_word_count()

