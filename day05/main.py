import sys
filename = "input.txt"
if len(sys.argv) > 1 and sys.argv[1] == "sample":
    filename = "sample_input.txt"

#open file, parse lines 
with open(filename, "r") as f:
    lines = f.read().split("\n")

def print_soln(arr): print("".join([c[-1] for c in arr]))
def col_num(c): return 1 + 4 * c
def get_qty_src_dest(l):
    spl = l.split(" ")
    return int(spl[1]), int(spl[3]), int(spl[5])

cols = None
idx_line = None
for i, line in enumerate(lines):
    if line.strip().startswith("1"):
        cols = int(line.split("   ")[-1])
        idx_line = i

cols_arr = [[] for _ in range(cols)]
for line in lines[:idx_line][::-1]:
    for col in range(cols):
        if col_num(col) < len(line) and line[col_num(col)] != ' ':
            cols_arr[col].append(line[col_num(col)])

cols_dupe = [c[:] for c in cols_arr]

for line in lines[idx_line+2:-1]:
    qty, src, dest = get_qty_src_dest(line)
    for _ in range(qty):
        removed = cols_arr[src - 1].pop()
        cols_arr[dest - 1].append(removed)
print("".join([c[-1] for c in cols_arr]))

cols_arr = cols_dupe
for line in lines[idx_line+2:-1]:
    qty, src, dest = get_qty_src_dest(line)
    state = []
    for _ in range(qty):
        removed = cols_arr[src - 1].pop()
        state.append(removed)
        cols_arr[dest - 1] += state[::-1]
print("".join([c[-1] for c in cols_arr]))
