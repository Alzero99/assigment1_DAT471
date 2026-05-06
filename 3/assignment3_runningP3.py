import time
import subprocess
import matplotlib.pyplot as plt

cores = [1,2,4,8,16,32]
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
plt.plot(cores, speedups, marker='o')
plt.xlabel('Number of Cores')
plt.ylabel('Speedup')
plt.title('Scalability of Twitter Data Processing')
plt.savefig('scalability_plot.png')  # Save the plot as a PNG file
plt.show()