#!/bin/bash

#SBATCH -p core
#SBATCH -n 1
#SBATCH -t 00:05:00
#SBATCH -J problem2c

echo "Submitting assignment 1 problem 2c"
CONTAINER_IMAGE="/data/courses/2026_dat471_dit066/containers/assignment1.sif"
CSV_FILE="/data/courses/2026_dat471_dit066/datasets/bike_sharing_hourly.csv"

apptainer exec \
    --bind /data \
    "$CONTAINER_IMAGE" \
    python3 assignment1_problem2c.py \
    "$CSV_FILE"