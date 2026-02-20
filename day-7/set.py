# Set operations in Python
a={1,3,5,7,9}
b={3,6,9,12}
a.add(11)
a.remove(1)
a.discard(2)
b.clear()
length=len(a)
minimum=min(a)
maximum=max(a)
sorted_a=sorted(a)
any_value=any(a)
all_values=all(a)
enumerate_a=enumerate(a)
print(a,length,minimum,maximum,sep="\n")
print("Enumerated set:", list(enumerate_a))
#set operations
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print(set1.intersection)
print("Difference (set1 - set2):", set1 - set2)
#frozenset
fset=frozenset([1,2,3,4,5])
another_set=frozenset([4,5,6,7,8])
print(fset&another_set)
print(fset|another_set)
print(fset- another_set)
print(fset^another_set)
