import sys
sys.path.insert(0, ".")

from src.core.matching import name_similarity, verify

print(name_similarity("Adeola", "Adeola"))
print(name_similarity("Adeola", "Adaola"))
print(name_similarity("Peter", "James"))

print(verify(
    {"name": "Adeola Bello", "dob": "01/01/1990"},
    {"name": "Adeola Bello", "dob": "01/01/1990"}
))

print(verify(
    {"name": "Adeola Belo", "dob": "01/01/1990"},
    {"name": "Adeola Bello", "dob": "01/01/1990"}
))

print(verify(
    {"name": "James Okafor", "dob": "01/01/1990"},
    {"name": "Adeola Bello", "dob": "01/01/1990"}
))
