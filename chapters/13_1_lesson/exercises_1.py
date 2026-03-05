import string
from operator import itemgetter
word_list = ['']
def moby_remove_whitespaces_punctuation(fin):
    
    count = 0
    d = dict()
    for line in fin:
        for c in string.punctuation:
            line.replace(c, " ")
        word = line.strip().lower()
        # word = word.translate(str.maketrans('', '', string.punctuation))
        word = word.replace(string.punctuation, "")
        line.strip
        line = line.replace("\n", "") 
        line = line.replace("  ", " ")
        words = line.split(" ")
    
        for w in words:
          if w not in d:
             d[w] = 1
          else:
                d[w] += 1
        # print(d)
    return d
      #  for w in words:
       #     word_list.append(w)
        #    count = count + 1
     #   print(f"{word} ")
    
    #return count
    
# count = moby_remove_whitespaces_punctuation(open('shared\Moby_Dick.txt'))
#print(f"Word list: {word_list}")
#
f_name = 'shared/Moby_Dick.txt'
d = moby_remove_whitespaces_punctuation(open(f_name))
# print(f"Count: {count}")
# print(string.punctuation)
# for k, v in d.items():
    # print(f"{k} {v}")
sv = dict(sorted(d.items(), key=itemgetter(1)))
print(sv)
