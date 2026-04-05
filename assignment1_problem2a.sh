#!/bin/bash
#SBATCH -p core
#SBATCH -n 1
#SBATCH -t 00:05:00
#SBATCH -J problem2a
echo "System information"
echo "Hostname: $(hostname)"


CONTAINER_IMAGE="/data/courses/2026_dat471_dit066/containers/assignment1.sif"

echo
echo "kernel version:"
apptainer exec "$CONTAINER_IMAGE" uname -r
echo



echo "CPU model"
apptainer exec "$CONTAINER_IMAGE" bash -c "lscpu | grep 'Model name:'"

echo "Python3 details:"
apptainer exec "$CONTAINER_IMAGE" which python3
apptainer exec "$CONTAINER_IMAGE" python3 --version
