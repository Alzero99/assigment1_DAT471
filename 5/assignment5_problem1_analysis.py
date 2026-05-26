from assignment5_problem1 import murmur3_32
from collections import Counter
import statistics


file_path = "/data/courses/2026_dat471_dit066/datasets/words"

seed = 0xee418b6c
m = 128
mask = m - 1

values = []

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        key = line.strip()
        h = murmur3_32(key, seed)
        value = h & mask
        values.append(value)

freq = Counter(values)

mean = statistics.mean(values)
std = statistics.stdev(values)

collisions = 0
for count in freq.values():
    collisions += count * (count - 1) // 2

n = len(values)
key_pairs = n * (n - 1) // 2
collision_probability = collisions / key_pairs

print("Number of keys:", n)
print("Mean:", mean)
print("Standard deviation:", std)
print("Collisions:", collisions)
print("Collision probability:", collision_probability)

with open("histogram_data.txt", "w") as out:
    for i in range(m):
        out.write(f"{i} {freq.get(i,0)}\n")

with open("problem1b_stats.txt", "w") as out:
    out.write(f"Number of keys: {n}\n")
    out.write(f"Mean: {mean}\n")
    out.write(f"Standard deviation: {std}\n")
    out.write(f"Collisions: {collisions}\n")
    out.write(f"Collision probability: {collision_probability}\n")