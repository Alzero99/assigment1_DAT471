#!/bin/bash

echo "System information"

echo "Hostname: $(hostname)"

echo "CPU details:"

lscpu
echo


echo "System RAM"
grep MemTotal /proc/meminfo
echo

echo "GPU details"
nvidia-smi
echo


echo "Filesystem"
df -T /data
echo "Disk usage"
df -h /data

echo

echo "linux kernel details"
lsb_release -a

echo
echo "Python3 details"
which python
python3 --version

