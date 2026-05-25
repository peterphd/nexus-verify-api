def is_same(a: str, b:str) -> bool:
    return a.strip().lower() == b.strip().lower()

def validate_nin(nin: str) -> bool:
    if not nin.isdigit():
        raise ValueError("NIN must contain digits only.")
    if len(nin) != 11:
        raise ValueError(f"NIN must be 11 digits.got {len(nin)}.")
    return True

print(is_same("Adeola", "adeola"))
print(is_same("Mike", "James"))

try:
    validate_nin("1234567890A")
except ValueError as e:
    print(f"Error: {e}")

try:
    validate_nin("12345678901")
    print("NIN is valid.")
except ValueError as e:
    print(f"Error: {e}")
