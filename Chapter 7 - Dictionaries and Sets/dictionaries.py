# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)


# Access Items
# print(band(["vocals"])) # return the key 'guitar', associated the value 'vocals'
print(band.get("guitar")) # return the value 'vocals', associated with the key 'guitar'

# List all keys
print(band.keys())

# List all values
print(band.values())

# List of key-value pairs as tuples
print(band.items())

# Verify that a key exists
print("guitar" in band) # True
print("triangle" in band) # False

# Change values in a dictionary
band["vocals"] = "Coverdale" # Key-value pair becomes ==> "vocals": "Coverdale"

# We can use the update() function to update an existing key-value pair or create a new one in the dictionary
band.update({"bass": "JPJ"})

# Remove items from the dictionary
print(band.pop("bass")) # returns the value associated with the key "bass" and removes the key-value pair from the dictionary

band["drums"] = "Bonham" # Adding a new key-value pair to the dictionary, "drums": "Bonham"
print(band.popitem()) # Returns a tuple of the most recent/last item/key-value pair added to the dictionary and removes it from the dictionary. In this case, it is returned as ('drums', 'Bonham')


# Delete and clear the dictionary
band["drums"] = "Bonham"
del band["drums"]
print(band)


# Copy dictionaries
# band2 = band 
# This creates a reference, not a new dictionary. We would call this a "bad copy". Now, any "changes" made to `band2` would be reflected in `band`.
band2 = band.copy() # This is the proper way to copy a dictionary, creating a new dictionary in the process.

# We can also make a copy using the `dict()` constructor function:
band3 = dict(band);


# Nested dictionaries
# The value for a key-value pair can be another dictionary.
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2= {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}