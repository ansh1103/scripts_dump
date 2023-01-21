#!/bin/bash

# Define the log file
log_file="resource_usage.log"

# Create the header for the table
echo "Time,CPU Usage,Memory Usage,Disk Usage" >> $log_file

# Loop to collect and log the resource usage every 60 seconds
while true
do
    # Get the current time
    current_time=$(date +"%Y-%m-%d %T")

    # Get the CPU usage
    cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')

    # Get the memory usage
    mem_usage=$(free -m | awk 'NR==2{printf "%.2f%%", $3*100/$2 }')

    # Get the disk usage
    disk_usage=$(df -h | awk '$NF=="/"{printf "%s", $5}')

    # Write the resource usage to the log file
    echo "$current_time,$cpu_usage,$mem_usage,$disk_usage" >> $log_file

    # Sleep for 60 seconds before collecting the next resource usage
    sleep 60
done
