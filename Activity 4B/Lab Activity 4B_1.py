a = {"a","g","b","c","d","f"}
b = {"l","m","o","b","c","h"}
c = {"h","i","j","c","d","f","k"}

ab = a.union(b)
howMany = len(ab)
print("a. There are about " + str(howMany) + " elements inside set a and b")

Notpart = b.difference(a, c)
howManyNotpart = len(Notpart)
print("b. There are " + str(howManyNotpart) + " " +str(Notpart) + " in b that are not part of a and c")

i = c.difference(a)
print (i)

ii = c.intersection(a)
print (ii)

iii = b.intersection(a).union(b.intersection(c))
print (iii)

iv = a.intersection(c).difference(b)
print (iv)

v = a.intersection(c,b)
print (v)
 
vi = b.difference(a, c)
print (vi)