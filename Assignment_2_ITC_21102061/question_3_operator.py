"""
3. For a=56 and b=10 with the help of bitwise operators calculate the following:
a. a&b
b. a|b
c. a^b
d. Left shift both a and b with 2 bits.
e. Right shift a with 2 bits and b with 4 bits.
"""
a=56
b=10
print("a & b=", (a & b))
print("a | b=", (a | b))
print("a ^ b=", (a ^ b))
print("Left shift both a and b with 2 bits : a=",a<<2, "b=", b<<2)
print("Right shift a with 2 bits and b with 4 bits : a=", a>>2, "b=", b>>4)
