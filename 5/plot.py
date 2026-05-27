import matplotlib.pyplot as plt

x = []
y = []

with open("histogram_data.txt") as f:
    for line in f:
        bucket, freq = line.split()
        x.append(int(bucket))
        y.append(int(freq))

plt.bar(x, y)

plt.xlabel("Hash value (lowest 7 bits)")
plt.ylabel("Frequency")
plt.title("Murmur3_32 distribution")

plt.show()
