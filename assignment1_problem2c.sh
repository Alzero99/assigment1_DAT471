#!/bin/bash
echo "Submitting assignment 1 problem 2c"
apptainer exec \
    --bind /data \
    /data/courses/2026_dat471_dit066/containers/assignment1.sif \
    python3 assignment1_problem2c.py \
    /data/courses/2026_dat471_dit066/datasets/bike_sharing_hourly.csv