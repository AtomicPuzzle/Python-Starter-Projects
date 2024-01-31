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
print(band)