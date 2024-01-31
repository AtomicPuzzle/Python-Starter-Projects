# Sets
# Can be created using brackets or the constructor:
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

# A set does not allow duplicate values. True is a duplicate of 1, False is a duplicate of 0:
nums = {1, True, 2, False, 3, 4, 0}
print(nums) # Outputs {False, 1, 2, 3, 4}

# You cannot refer to an element in the set with an index position or a key


# We can add a new element to a set:
nums.add(8)

# And we can add elements from one set to another:
morenums = {5, 6, 7}
nums.update(morenums)

# update() can be used with lists, tuples, and dictionaries as well.


# Merging two sets to create a new set:
setone = {1, 2, 3}
settwo = {5, 6, 7}
mynewset = setone.union(settwo)
print(mynewset) # outputs {1, 2, 3, 5, 6, 7}



# Keeping only the duplicates from two sets:
# This does not create a new set, rather it updates the first set selected.
setthree = {1, 2, 3}
setfour = {2, 3, 4}
mynewsettwo = setthree.intersection_update(setfour)
print(setthree) # will output {2, 3}



# Keeping everything except the duplicates:
setthree = {1, 2, 3}
setfour = {2, 3, 4}
setthree.symmetric_difference_update(setfour)
print(setthree) # will output {1, 4}