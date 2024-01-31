# A `for` loop completes a loop for a given sequence:
# Example 1:
names = ["Dave", "Sara", "John"]
for x in names:
    print(x)

# This will output:
# 	Dave
# 	Sara
# 	John

# Example 2:
for x in "Canada":
    print(x)
# This will print every letter of the word (as though iterating through an array) and will output:
# 	C
#   a
#   n
#   a
#   d
#   a
    

# Example 3:
for x in names:
    if x == "Sara":
        break
    print(x)
# This will only print 'Dave', breaking the loop when it reaches 'Sara'.
    

# Example 4:
for x in names:
    if x == "Sara":
        continue
    print(x)
# This will only print 'Dave' and 'John', skipping 'Sara'
    


# Example 5, ranges:
# print 0, 1, 2, 3
for x in range(4):
    print(x)

# print 1, 2, 3
for x in range(1, 4):
    print(x)

# start at 0, go up to 10, increment by 2
# print 0, 2, 4, 6, 8
for x in range(0, 10, 2):
    print(x)