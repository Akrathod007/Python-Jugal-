# s = {}
# print(s)
# print(type(s))
"""
s = set()
print(s)
print(type(s))

s1 = {1, 2, 3, 4, 5}
print(s1)

li = [10, 2, 2, 3, 4, 1, 2]
s2 = set(li)
print(s2)

"""

# print(s2[0])
"""
fruit = {"Apple", "Mango", "Banana", "Kiwi"}
print(fruit)

fruit.add("Watermelon")
print(fruit)


fruit.remove("Kiwi")
# fruit.remove("Kiwii")
# fruit.discard("Kiwi")
fruit.discard("Kiwii")
elm = fruit.pop()
print(elm)
fruit.clear()
print(fruit)

"""


a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}
print(a.union(b))  # same
c = a.union(b)
print(c)
print(a)

print("---------------------------------------------------")
print(a & b)  # {3}
print(a.intersection(b))  # same

print("---------------------------------------------------")

print(a - b)  # {1, 2}
print(b.difference(a))  # same
print("---------------------------------------------------")

print(a ^ b)  # {1, 2, 4, 5}
print(a.symmetric_difference(b))

print("---------------------------------------------------")

a = {1, 2}
b = {1, 2, 3}

print(a <= b)  # True
print(a.issubset(b))  # True

print("---------------------------------------------------")

print(b >= a)  # True
print(b.issuperset(a))  # True

print("---------------------------------------------------")

x = {1, 2}
y = {3, 4}

print(x.isdisjoint(y))  # True


print("---------------------------------------------------")

a = {1, 2}
b = {3, 4}

a.update(b)
print(a)  # {1, 2, 3, 4}
print(b)
print("---------------------------------------------------")


a = {1, 2, 3}
b = {2, 3, 4}

a.intersection_update(b)
print(a)  # {2, 3}

print("---------------------------------------------------")

a = {1, 2, 3}
b = {2}

a.difference_update(b)
print(a)  # {1, 3}
print("---------------------------------------------------")

a = {1, 2, 3}
b = {3, 4}

a.symmetric_difference_update(b)
print(a)  # {1, 2, 4}

fs = frozenset([1, 2, 3])
# fs.add(4)  # Error (immutable)

print(sum(a))
print(max(a))
print(min(a))
