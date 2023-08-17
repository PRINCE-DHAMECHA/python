
# ~ The ^ operator will perform a binary XOR in which a binary 1 is copied if and only if it is the value of exactly one operand. Another way of stating this is that the result is 1 only if the operands are different.

# 60 = 0b111100
# 30 = 0b011110
print(60 ^ 30)
# Out: 34
# 34 = 0b100010
print(bin(60 ^ 30))
