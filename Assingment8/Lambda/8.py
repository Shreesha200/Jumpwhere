validate = lambda s: (
    any(c.isupper() for c in s) and
    any(c.islower() for c in s) and
    any(c.isdigit() for c in s) and
    len(s) >= 10
)

s = "PaceWisd0m"
print("valid string" if validate(s) else "invalid string")
