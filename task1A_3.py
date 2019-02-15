fin1 = open('Book1.txt')
fin2 = open('Book2.txt')
fin3 = open('Book3.txt')
def sorted_words():
  a1 = []
  a2 = []
  a3 = []
  d1 = {}
  d2 = {}
  d3 = {}
  count1 = 0
  count2 = 0
  count3 = 0
  for line in fin1:
    line= line.strip().lower()
    for word in line.split():
      for count_word_number in word:
        count1 = count1+1
      if count1 in d1:
        d1[count1].append(word)
      else:
        d1[count1]=[word]
  a1 = sorted(d1.items(),key = lambda x:x[0], reverse = True)

  for line in fin2:
    line= line.strip().lower()
    for word in line.split():
      for count_word_number in word:
        count2 = count2+1
      if count2 in d2:
        d2[count2].append(word)
      else:
        d2[count2]=[word]
  a2 = sorted(d2.items(),key = lambda x:x[0], reverse = True)

  for line in fin3:
    line= line.strip().lower()
    for word in line.split():
      for count_word_number in word:
        count3 = count3+1
      if count3 in d3:
        d3[count3].append(word)
      else:
        d3[count3]=[word]
  a3 = sorted(d3.items(),key = lambda x:x[0], reverse = True)


  print(a1,a2)
sorted_words()
