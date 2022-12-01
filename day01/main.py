# open file, parse lines as integers
f = open("input.txt", "r").read().strip().split("\n\n")
# compute total number of calories for each elf
elf_sums = map(lambda chunk: sum(map(int, chunk)), [c.split("\n") for c in f])
# sort calories descending
elf_sums_sorted = sorted(elf_sums, reverse=True)
# part 1
print(elf_sums_sorted[0])
# part 2 
print(sum(elf_sums_sorted[0:3]))

