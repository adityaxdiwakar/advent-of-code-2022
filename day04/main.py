import sys
filename = "input.txt"
if len(sys.argv) > 1 and sys.argv[1] == "sample":
    filename = "sample_input.txt"

#open file, parse lines 
with open(filename, "r") as f:
    lines = f.read().strip().split("\n")
lines = [[[int(x) for x in i.split("-")] for i in p.split(",")] for p in lines]

res = 0
for ((al, ar), (bl, br)) in lines:
    if al >= bl and ar <= br or bl >= al and br <= ar: res += 1
print(res)

res = 0
for ((al, ar), (bl, br)) in lines:
    set_a = set(range(al, ar + 1))
    set_b = set(range(bl, br + 1))
    if (len(set_a | set_b) != len(set_a) + len(set_b)):
        res += 1
print(res)
