#C7114-Ertu
right_hand = set("yuıopğühjklşinmöç")
left_hand =  set("qwertasdfgzxcvb")
right = set()
left = set()
words = input("Write a word = ")
words=set(words)
for i in words:
  if i in right_hand:
    right.add(i)
  else:
    left.add(i)
if any(left) and any(right):
  print(any(left) and any(right))
else:
  print(any(left) and any(right))