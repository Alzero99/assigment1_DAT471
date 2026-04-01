#!/bin/bash
echo "System information"
echo "Hostname: $(hostname)"

source ~/miniforge3/bin/activate
apptainer run /data/courses/2026_dat471_dit066/containers/assignment1.sif  

echo
echo "kernel version:"
uname -r

echo "CPU model"
lscpu | grep "Model name:"

echo "Python3 details:"
which python
python3 --version
