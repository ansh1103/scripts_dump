#!/bin/bash

# Define the input and output files
input_file="access.log"
output_file="ip_addresses.txt"

# Use grep to find all the IP addresses in the log file
ip_addresses=$(grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" $input_file)

# Write the IP addresses to the output file
echo "$ip_addresses" > $output_file

# Print the output
echo "The IP addresses are:"
echo "$ip_addresses"