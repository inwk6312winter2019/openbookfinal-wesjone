fin1 = open('Book1.txt')
fin2 = open('Book2.txt')
fin3 = open('Book3.txt')

def starts_with_vow():
  count_vow1=0
  count_vow2=0
  count_vow3=0
  vow_list = ['a','e','i','o','u']
  for line in fin1:
    line=line.strip().lower()
    for word in line.split():
      if word[0] in vow_list:
        count_vow1+=1
  #this is for book2
  for line in fin2:
    line=line.strip().lower()
    for word in line.split():
      if word[0] in vow_list:
        count_vow2+=1
  #this is for book3
  for line in fin3:
    line=line.strip().lower()
    for word in line.split():
      if word[0] in vow_list:
        count_vow3+=1


  print('this number of word start with vow in book1 is :%d, in book2 is :%d, in book3 is :%d' %(count_vow1,count_vow2,count_vow3))

starts_with_vow()

