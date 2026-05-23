import time
import subprocess
import matplotlib.pyplot as plt

cores = [1,2,4,8,16,32, 64]
times = []

for num_cores in cores:
    start = time.time()
    # run the program with num_cores workers, e.g. using subprocess.run()
    subprocess.run(["python3", "assignment3_problem3.py", "-r", "local[{}]".format( num_cores), "/data/courses/2026_dat471_dit066/datasets/twitter/twitter_10M.txt"])
    
    
    end = time.time()

    timerun = end - start
    times.append(timerun)

# Measure scalability by comparing to 1 core
speedups = []
one_core_runtime = times[0]  
for runtime in times:
    speedup = one_core_runtime / runtime
    speedups.append(speedup)
    print(f"Speedup with {num_cores} cores: {speedup:.2f}")


# Plotting the results
# speedups = [1, 1.24, 2.33, 3.33, 3.63, 3.74] # Part 3
# speedups = [1, 1.80, 2.85, 4.06, 4.62, 4.29]  # part 4
# speedups = [1, 1.59, 2.20, 2.82, 2.86, 2.72, 2.74] # assignment 4 results
speedups = [1, 1.90, 3.08, 4.66, 5.91, 6.53, 6.92]
plt.plot(cores, speedups, marker='o')
plt.xlabel('Number of Cores')
plt.ylabel('Speedup')
plt.title('Scalability of Twitter Data Processing')
plt.savefig('Assignment4_ScalabilityD.png')  # Save the plot as a PNG file
plt.show()