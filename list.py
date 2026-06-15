"""
list : It is collection of multiple type of data and also ordered
It is mutable -> You can add,delete,update element
"""

# li = [1, 2, 3, 4, 5]
# print(li)
# print(type(li))

# l2 = [1, 3.14, "Hello", True]
# print(l2)

# l3 = []
# print(l3)

# l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
    1   2   3   4   5   6   7   8   9   10
i   0   1   2   3   4   5   6   7   8   9
-  -10  -9  -8  -7  -6  -5  -4  -3  -2  -1

"""
# print(l4)
# print(len(l4))

# l4[4] = 500
# print(l4)
# print(l4[0])
# print(l4[4])
# print(l4[-8])
# print(l4[-1])

# l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# slicing : To extract sub list from list
# print(l4[1:9])
# print(l4[:6])
# print(l4[2:])
# print(l4[:])
# print(l4[1:9:2])
# print(l4[1:9:4])
# print(l4[-7:-1])
# print(l4[-1:-7:-1])
# print(l4[-1:-7:-2])
# print(l4[2:-4])


# using indexing :
# for i in range(0, len(l4)):
#     print(i, "->", l4[i])

# for i in range(len(l4) - 1, -1, -1):
#     print(i, "->", l4[i])


# direct element access

# for i in l4:
#     print(i)

# i = 0

# while i < len(l4):
#     print(l4[i])
#     i += 1


# l5 = [1, 2, 3, 4, 5, 3, 2, 4, 7, 2, 5, 3, 6, 7, 8, 9, 10]
# print(l5)
# print(len(l5))
# l5.append(300)
# print(l5)

# l5.insert(4, 400)
# print(l5)

# l6 = [11, 12, 13]
# l5.extend(l6)
# print(l5)

# print(l6 * 5)

# elm = l5.pop()
# elm = l5.pop(7)
# elm = l5.pop(20)
# print(elm)
# print(l5)

# l5.remove(3)
# # l5.remove(333)
# print(l5)

# l6 = []
# l6.pop()

# del l5[4]
# print(l5)

# l5.clear()
# print(l5)

# print(l5.index(3))
# print(l5.index(3, 6))
# print(l5.index(3, 6, 8))

# print(l5.count(3))
# l5.reverse()
# print(l5)
# print(l5[::-1])

# l5.sort()
# l5.sort(reverse=True)
# print(l5)

# l6 = l5.copy()
# print(l6)
# l6[4] = 4000
# print(l5)
# print(l6)

# print(sum(l5))
# print(max(l5))
# print(min(l5))
# # l7 = [1, 2, 3, "Hello"]
# # l7 = [1, 2, 3, True]
# # l7 = [1, 2, 3, False]
# # print(sum(l7))


# # del l5
# # print(l5)

# new_li = l5
# print(new_li)
# new_li[1] = 10000
# print(new_li)
# print(l5)


# li = []

# no = int(input("Enter a list length : "))

# for i in range(1, no + 1):
#     n = int(input("Enter a number : "))
#     li.append(n)

# print(li)

l1 = [[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11]]]

print(l1[2][2][2])


"""
r and c -> scan
r - 2
c - 3

[[1,2,3],[4,5,6]]
"""


l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# l3 = [2,4,6,8,10,12,14,16,18]
l3 = []
"""
l3 = [[2,4,6],[8,10,12],[14,16,18]]
"""


# for i in l1:
#     for j in i:
#         print(j)


# for i in range(0, len(l1)):
#     print(i, "->", l1[i])
#     for j in range(0, len(l1[i])):
#         print(j, "->", l1[i][j])
#         l3.append(l1[i][j] + l2[i][j])

# print(l3)


for i in range(0, len(l1)):
    print(i, "->", l1[i])
    il = []
    for j in range(0, len(l1[i])):
        print(j, "->", l1[i][j])
        il.append(l1[i][j] + l2[i][j])
    l3.append(il)
print(l3)


"""
    l1 = [
        [1,2,3,4],
        [4,5,6,5],
        [7,8,9,8],
        [7,8,9,8]
    ]
"""

l1 = [[1, 2, 3, 10], [4, 5, 6, 5], [7, 8, 9, 8], [7, 8, 9, 18]]

leftDiagonalSum = 0
rightDiagonalSum = 0


for i in range(0, len(l1)):
    for j in range(0, len(l1[i])):
        if i == j:
            leftDiagonalSum = leftDiagonalSum + l1[i][j]
        if i + j == len(l1) - 1:
            rightDiagonalSum = rightDiagonalSum + l1[i][j]

print("Left Diagonal Sum is : ", leftDiagonalSum)
print("Right Diagonal Sum is : ", rightDiagonalSum)
