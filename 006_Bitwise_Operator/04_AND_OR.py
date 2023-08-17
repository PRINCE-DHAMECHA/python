
# ~ The & operator will perform a binary AND, where a bit is copied if it exists in both operands. That means:

# 60 = 0b111100
# 30 = 0b011110
print(60 & 30)
# Out: 28
# 28 = 0b11100
print(bin(60 & 30))
# Out: 0b11100

# ~ The | operator will perform a binary "or," where a bit is copied if it exists in either operand. That means:

# 0 | 0 = 0
# 0 | 1 = 1
# 1 | 0 = 1
# 1 | 1 = 1
# 60 = 0b111100
# 30 = 0b011110
print(60 | 30)
# Out: 62
# 62 = 0b111110
print(bin(60 | 30))
# Out: 0b111110
