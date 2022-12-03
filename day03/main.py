# helpers
def get_prio_set(s): return get_prio(list(s)[0])
def get_prio(c):
    return 1 + ord(c) - (ord('a') if c.islower() else (ord('A') - 26))

#open file, parse lines 
with open("sample_input.txt", "r") as f:
    lines = f.read().strip().split("\n")

# part 1 
res = 0
for line in lines:
    comp_a = set(line[:len(line) // 2])
    comp_b = set(line[len(line) // 2:])
    res += get_prio_set(comp_a & comp_b)
print(res)

# part 2
res = 0
from itertools import zip_longest
for (line_a, line_b, line_c) in zip_longest(*([iter(lines)] * 3)):
    res += get_prio_set(set(line_a) & set(line_b) & set(line_c))
print(res)
