word = "hippo runs to us!"
liste = []
for i in word:
    count = word.count(i)
    liste.append(count)
birles = zip(word, liste)    
birles = set(birles)
birles = dict(birles)
print(birles)