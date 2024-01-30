# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)


# Access Items
print(band(["vocals"])) # return the key 'guitar', associated the value 'vocals'
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
