import string
fin1 = open('Book1.txt')
fin2 = open('Book2.txt')
fin3 = open('Book3.txt')

def top_20_words():
  d1={}
  d2={}
  d3={}

  for line in fin1:
    line=line.strip().lower()
    for s in line:
      #this is delet punctuation
      if s in string.punctuation:
        line = line.replace(s,'')
    # break into words
    for word in line.split():
      d1[word]=d1.get(word,0)+1
  t1 = sorted(d1.items(),key = lambda x:x[1],reverse =True)

  for line in fin2:
    line=line.strip().lower()
    for s in line:
      #this is delet punctuation in book2
      if s in string.punctuation:
        line = line.replace(s,'')
    # break into words in book2
    for word in line.split():
      d2[word]=d2.get(word,0)+1
  t2 = sorted(d2.items(),key = lambda x:x[1],reverse =True)

  for line in fin3:
    line=line.strip().lower()
    for s in line:
      #this is delet punctuation
      if s in string.punctuation:
        line = line.replace(s,'')
    # break into words
    for word in line.split():
      d3[word]=d3.get(word,0)+1
  t3 = sorted(d3.items(),key = lambda x:x[1],reverse =True)



  print(t1[:20])
  print(t2[:20])
  print(t3[:20])

top_20_words()
