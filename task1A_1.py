fin1 = open('Book1.txt')
fin2 = open('Book2.txt')
fin3 = open('Book3.txt')
def unique_words():
  a1_list=[]
  a2_list=[]
  a3_list=[]
  d1={}
  d2={}
  d3={}
  for line in fin1:
    line = line.strip().lower()
    for word in line.split():
      d1[word]=d1.get(word,0)+1
  for word,freq in d1.items():
    a1_list.append(word)
  for line in fin2:
    line = line.strip().lower()
    for word in line.split():
      d2[word]=d2.get(word,0)+1
  for word,freq in d2.items():
    a2_list.append(word)
  for line in fin3:
    line = line.strip().lower()
    for word in line.split():
      d3[word]=d3.get(word,0)+1
  for word,freq in d3.items():
    a3_list.append(word)
  print(a1_list,a2_list,a3_list)

unique_words()
