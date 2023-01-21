#!/bin/bash

# Find the 10 biggest files
biggest_files=$(find / -type f -exec du -Sh {} + 2>/dev/null | sort -rh | head -n 10)

# Write the output to a file
echo "$biggest_files" > biggest_files.txt

# Print the output
echo "The 10 biggest files are:"
echo "$biggest_files"