#!/bin/bash

# Check if filename is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# Assign the filename to a variable
filename="$1"

# Check if the file exists
if [ ! -f "$filename" ]; then
    echo "Error: File '$filename' not found."
    exit 1
fi

# Define an array of substitutions
substitutions=(
    's/POPC/POP /g'
    's/1H   HOH/ H1  HOH/g'
    's/2H   HOH/ H2  HOH/g'
    's/OW  HOH/O   HOH/g'
    's/CD  ILE/CD1 ILE/g'
    's/HISH/HIP /g'
    's/HISD/HID /g'
    's/HISE/HIE /g'
)

# Perform substitutions using sed and redirect output to a temporary file
temp_file=$(mktemp)
cp "$filename" "$temp_file"

for substitution in "${substitutions[@]}"; do
    sed "$substitution" "$temp_file" > "$filename"
    mv "$filename" "$temp_file"
done

# Replace the original file with the modified one
mv "$temp_file" "$filename"

echo "Substitutions done."
