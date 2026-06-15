t1 = ()
print(t1)
print(type(t1))
print(len(t1))

t2 = (1, 2, 3, 4)
print(t2)

t3 = (10, "Ram", 8.5, True)
print(t3)

t4 = 1, 2, 3, 4
print(t4)
print(type(t4))

t = (10, 20, 30, 40, 50)

print(t[0])  # First element
print(t[-1])  # Last element

print(t[1:4])  # From index 1 to 3
print(t[:3])  # First 3 elements
print(t[-3:])  # Last 3 elements


t5 = (10,)
print(type(t5))


t1 = (1, 2, 3)
t2 = (4, 5, 6)
r = t1 + t2
print(r)
print(t1 * 3)

print(1 in t1)
print(11 in t1)
print(1 not in t1)
print(11 not in t1)


print(len(t1))
print(max(t1))
print(min(t1))
print(sum(t1))

li = [1, 2, 3, 4, 5]

t = tuple(li)
print(t)

s = "Hello"
t = tuple(s)
print(t)

print(t.count("l"))
print(t.index("l"))


t = 1, "Ram", 8.5, 1, 2, 3, 4, 5
print(t)

roll, name, marks, *other = t
print(roll)
print(name)
print(marks)
print(other)
