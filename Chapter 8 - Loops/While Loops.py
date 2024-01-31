# While loops
# Execute a block of code while a condition is true
value = 1
while value <= 10:
    print(value)
    value += 1


# We can use the `break` statement to break the loop under certain conditions:
value = 1
while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1


 # We can also use the `continue` statement to proceed to the next loop, ignoring all else inside the current loop:
value = 1
while value <= 10:
    print(value)
    if value == 5:
        continue
    value += 1