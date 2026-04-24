import matplotlib.pyplot as plt
workers = [1,2,4,8,16,32,64]
#times = [144.24 , 65.93 , 47.54 , 42.24 , 39.78 , 41.04 , 43.52] # part d
#times = [84.08 , 54.98 , 39.33 , 31.93 , 30.05 , 29.77 , 29.03] # part e
times = [67.75, 40.13, 25.49, 25.35, 25.54, 26.12, 27.52] # part f
speedups = []
theoretical_speedups = 2.71
for t in times:
        speedup = 69.77 / t
        speedups.append(speedup)
        print(f'Speedup: {speedup}')

plt.figure(figsize=(10, 6))
plt.plot(workers, speedups, marker='o', label='Actual Speedup')
plt.axhline(y=theoretical_speedups, color='r', linestyle='--', label='Theoretical Speedup (2.71)')
plt.xscale('log', base=2)
plt.xticks(workers)
plt.xlabel('Number of Workers')
plt.ylabel('Speedup')
plt.title('Speedup vs Number of Workers')
plt.legend()
plt.grid()
plt.savefig('plot_part_f.png')
plt.show()