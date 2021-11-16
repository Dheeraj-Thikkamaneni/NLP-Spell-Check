# edit operations,    insert, delete, swap, replace

def split(word):
    return[(word[:i], word[i:]) for i in range(len(word) + 1)] 
  
def delete(word):
    return [l + r[1:] for l,r in split(word) if r] # l,r left, right for above  
  
# all the above words printed will be suggested, but we need only valid words that in the textfile

def swap(word):
    return [l + r[1] + r[0] + r[2:] for l,r in split(word) if len(r)>1]
  
def replace(word):
    letters = string.ascii_lowercase
    return [l + c + r[1:] for l,r in split(word) if r for c in letters]
  
def insert(word):
    letters = string.ascii_lowercase
    return [l + c + r for l,r in split(word) for c in letters]  
