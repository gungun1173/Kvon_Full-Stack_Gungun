print("hello,world")
x=5
print(x)

fruits = ["mango", "orange", "banana"]
p,y,z = fruits
print(p+" "+y+" "+z)
print(p, y, z)

print(y)
print(z)

dictionary = dict(name = "John", age = 36)
print(dictionary.get("name"), dictionary.get("age"))
print(type(dictionary))

tup = tuple(("apple", "banana", "mango"))
print(tup)
print(type(tup))

set = set(("good", "better", "best"))
set.add("bad")
print(set)
print(type(set))

frozenset = frozenset(("good", "better", "best"))
print(frozenset)
print(type(frozenset))
