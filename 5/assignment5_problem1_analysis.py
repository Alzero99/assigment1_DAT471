from assignment5_problem1 import murmur3_32
from collections import Counter
import statistics
import matplotlib.pyplot as plt

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

plt.bar(range(m), [freq.get(i, 0) for i in range(m)])
plt.xlabel("Hash value using lowest 7 bits")
plt.ylabel("Frequency")
plt.title("Frequency distribution of Murmur3_32 hash values")
plt.savefig("problem1b_histogram.png")