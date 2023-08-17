
# ~ All of the Bitwise operators (except ~) have their own in place versions

a = 0b001
a &= 0b010
# a = 0b000
a = 0b001
a |= 0b010
# a = 0b011
a = 0b001
a <<= 2
# a = 0b100
a = 0b100
a >>= 2
# a = 0b001
a = 0b101
a ^= 0b011
# a = 0b110
