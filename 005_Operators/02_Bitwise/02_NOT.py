
# * ~n = -n - 1

print(~0)  # -1
print(~1)  # -2
# 0000 0010 -> 1111 1101(-3) (2's complement representation)
# 0 0011(+3) -> 1 1100 -> 1 1101(-3)
print(~2)  # -3
print(~555)  # -556
print(~-555)  # -556

# ~n -> -|n+1| For positive number
# * ~1 == -|1+1| = -2
# ~n -> |-n-1| For negative number
# * ~(-1) == | -(-1) - 1 | = 0
